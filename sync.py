#!/usr/bin/env python3
"""
sync_yaml_descriptions.py

Sync all CRD openAPIV3Schema descriptions into a documentation-style site.yaml.

Features
- Requires ruamel.yaml (round-trip). No fallbacks.
- Auto-detects target style:
  1) JSON Schema (mapping-based properties) → path-to-path sync
  2) Catalog style (properties is a list of {name: ...}) → name-based sync
- Copies CRD root schema description to:
    - target schema root (if present)
    - top-level document 'description' (if present)
- Only updates 'description' fields.

Usage
  ./sync_yaml_descriptions.py --from skupper_site_crd.yaml --to site.yaml --in-place --report
"""

import sys, argparse
from typing import Any, Dict, List, Tuple, Optional

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap, CommentedSeq

Json = Any
PathT = Tuple[str, ...]


# ------------- YAML IO -------------

def load_yaml_stream(path: Optional[str]) -> List[Json]:
    y = YAML(typ="rt")
    y.preserve_quotes = True
    with (open(path, "r", encoding="utf-8") if path else sys.stdin) as fh:
        return [doc for doc in y.load_all(fh) if doc is not None]

def dump_yaml_stream(docs: List[Json], path: Optional[str]) -> None:
    y = YAML(typ="rt")
    y.preserve_quotes = True
    y.indent(mapping=2, sequence=4, offset=2)
    with (open(path, "w", encoding="utf-8") if path else sys.stdout) as fh:
        y.dump_all(docs, fh)


# ------------- helpers -------------

def is_map(x: Json) -> bool:
    return isinstance(x, (dict, CommentedMap))

def is_seq(x: Json) -> bool:
    return isinstance(x, (list, CommentedSeq))

def set_block_style_if_multiline(node_parent: Json, key: str) -> None:
    try:
        val = node_parent[key]
        if isinstance(val, str) and "\n" in val:
            node_parent[key].fa.set_block_style()  # type: ignore[attr-defined]
    except Exception:
        pass


# ------------- CRD extraction -------------

def find_crd_schema(doc: Json) -> Optional[Json]:
    try:
        spec = doc.get("spec") if is_map(doc) else None
        versions = spec.get("versions", []) if is_map(spec) else []
        for v in versions or []:
            schema = (v.get("schema") or {}).get("openAPIV3Schema") if is_map(v) else None
            if is_map(schema):
                return schema
    except Exception:
        pass
    return None

def walk_schema(node: Json, path: PathT = ()) -> List[Tuple[PathT, Dict[str, Any]]]:
    out: List[Tuple[PathT, Dict[str, Any]]] = []
    if not is_map(node):
        return out
    out.append((path, node))
    props = node.get("properties")
    if is_map(props):
        for key, sub in props.items():
            out.extend(walk_schema(sub, path + (str(key),)))
    if "items" in node:
        out.extend(walk_schema(node.get("items"), path + ("items",)))
    if "additionalProperties" in node:
        ap = node.get("additionalProperties")
        if is_map(ap):
            out.extend(walk_schema(ap, path + ("additionalProperties",)))
        elif is_seq(ap):
            for i, sub in enumerate(ap):
                out.extend(walk_schema(sub, path + ("additionalProperties", str(i))))
    for kw in ("allOf", "anyOf", "oneOf"):
        seq = node.get(kw)
        if is_seq(seq):
            for i, sub in enumerate(seq):
                out.extend(walk_schema(sub, path + (kw, str(i))))
    return out

def build_desc_map(schema: Json) -> Dict[PathT, str]:
    out: Dict[PathT, str] = {}
    for p, n in walk_schema(schema):
        d = n.get("description") if is_map(n) else None
        if isinstance(d, str):
            out[p] = d
    return out


# ------------- Target detection -------------

def looks_like_json_schema_root(node: Json) -> bool:
    return is_map(node) and ("properties" in node or "type" in node or "items" in node)

def find_first_schema_like(node: Json) -> Optional[Json]:
    if looks_like_json_schema_root(node) and ("properties" in node or "type" in node):
        return node
    if is_map(node):
        for _, v in node.items():
            r = find_first_schema_like(v)
            if r is not None:
                return r
    if is_seq(node):
        for v in node:
            r = find_first_schema_like(v)
            if r is not None:
                return r
    return None

def is_catalog_properties_block(block: Json) -> bool:
    # In site.yaml, e.g.: spec: { properties: [ {name: linkAccess, description: ...}, ... ] }
    return is_map(block) and is_seq(block.get("properties"))

def find_catalog_sections(doc: Json) -> Dict[str, Json]:
    # return mapping of section name -> section mapping (with 'properties' list)
    sections = {}
    for key in ("spec", "status", "metadata"):
        sec = doc.get(key)
        if is_map(sec) and is_seq(sec.get("properties")):
            sections[key] = sec
    return sections


# ------------- Apply updates -------------

def apply_to_json_schema(dst_schema: Json, src_descs: Dict[PathT, str], report: bool) -> Tuple[int,int]:
    index: Dict[PathT, Dict[str, Any]] = dict(walk_schema(dst_schema))
    updated = 0
    skipped = 0
    for p, d in src_descs.items():
        node = index.get(p)
        if node is None:
            skipped += 1
            if report:
                print(f"[miss]  {'/'.join(p) or '<root>'}", file=sys.stderr)
            continue
        if node.get("description") != d:
            node["description"] = d
            set_block_style_if_multiline(node, "description")
            updated += 1
            if report:
                print(f"[update] {'/'.join(p) or '<root>'}", file=sys.stderr)
    return updated, skipped

def apply_to_catalog(dst_doc: Json, src_descs: Dict[PathT, str], report: bool) -> Tuple[int,int]:
    """
    Map CRD paths like ('spec','linkAccess') or ('status','conditions') to
    catalog entries like dst_doc['spec']['properties'][i]['name']=='linkAccess'.
    """
    sections = find_catalog_sections(dst_doc)
    updated = 0
    skipped = 0

    # Build a quick index: for each section, name -> item mapping
    name_index: Dict[str, Dict[str, Json]] = {}
    for sec_name, sec in sections.items():
        idx: Dict[str, Json] = {}
        for item in sec.get("properties") or []:
            if is_map(item) and isinstance(item.get("name"), str):
                idx[item["name"]] = item
        name_index[sec_name] = idx

    for p, d in src_descs.items():
        # We only attempt simple <section>/<field> matches
        if len(p) != 2:
            continue
        section, field = p
        if section not in name_index:
            continue
        target = name_index[section].get(field)
        if target is None:
            skipped += 1
            if report:
                print(f"[miss]  {section}/{field}", file=sys.stderr)
            continue
        if target.get("description") != d:
            target["description"] = d
            set_block_style_if_multiline(target, "description")
            updated += 1
            if report:
                print(f"[update] {section}/{field}", file=sys.stderr)

    return updated, skipped


# ------------- Main -------------

def main():
    ap = argparse.ArgumentParser(description="Sync CRD descriptions into site.yaml (schema or catalog style).")
    ap.add_argument("--from", dest="src", required=True, help="CRD YAML path")
    ap.add_argument("--to", dest="dst", default=None, help="Target YAML path (site). If omitted, read from stdin and write to stdout.")
    ap.add_argument("--in-place", action="store_true", help="Overwrite target file (requires --to)")
    ap.add_argument("--report", action="store_true", help="Report updates/misses to stderr")
    args = ap.parse_args()

    src_docs = load_yaml_stream(args.src)
    if not src_docs:
        print("[sync] ERROR: source YAML is empty", file=sys.stderr); sys.exit(2)
    dst_docs = load_yaml_stream(args.dst)
    if not dst_docs:
        print("[sync] ERROR: target YAML is empty", file=sys.stderr); sys.exit(2)

    src_doc = src_docs[0]
    dst_doc = dst_docs[0]

    src_schema = find_crd_schema(src_doc)
    if not is_map(src_schema):
        print("[sync] ERROR: could not find openAPIV3Schema in source", file=sys.stderr); sys.exit(2)
    src_descs = build_desc_map(src_schema)

    # Decide target mode
    dst_schema_like = find_first_schema_like(dst_doc)
    catalog_sections = find_catalog_sections(dst_doc)

    total_updated = 0
    total_skipped = 0

    if dst_schema_like and "properties" in dst_schema_like and is_map(dst_schema_like.get("properties")):
        # JSON Schema mode
        u, s = apply_to_json_schema(dst_schema_like, src_descs, report=args.report)
        total_updated += u; total_skipped += s

    if catalog_sections:
        # Catalog mode (this will handle your 'linkAccess' case)
        u, s = apply_to_catalog(dst_doc, src_descs, report=args.report)
        total_updated += u; total_skipped += s

    if not dst_schema_like and not catalog_sections:
        print("[sync] ERROR: target doc does not look like schema or catalog; nothing to update", file=sys.stderr)
        sys.exit(2)

    # Sync root description to schema root and to top-level doc description (if present)
    root_desc = src_schema.get("description")
    root_updates = 0
    if isinstance(root_desc, str):
        if dst_schema_like is not None and dst_schema_like.get("description") != root_desc:
            dst_schema_like["description"] = root_desc
            set_block_style_if_multiline(dst_schema_like, "description")
            root_updates += 1
            if args.report: print("[update] <schema-root description>", file=sys.stderr)
        if "description" in dst_doc and dst_doc.get("description") != root_desc:
            dst_doc["description"] = root_desc
            set_block_style_if_multiline(dst_doc, "description")
            root_updates += 1
            if args.report: print("[update] <document-top-level description>", file=sys.stderr)

    print(f"[sync] updated {total_updated} (+{root_updates} root), skipped {total_skipped}", file=sys.stderr)

    if args.in_place:
        if not args.dst:
            print("[sync] ERROR: --in-place requires --to FILE", file=sys.stderr); sys.exit(2)
        dump_yaml_stream(dst_docs, args.dst)
    else:
        dump_yaml_stream(dst_docs, None)


if __name__ == "__main__":
    main()
