#!/usr/bin/env python3
"""
sync_yaml_descriptions.py

Sync *all* `description` fields from a CRD's openAPIV3Schema to a site.yaml
while preserving formatting (block scalars, comments) when ruamel.yaml is available.

Default behavior:
- Auto-detect CRD schema at spec.versions[].schema.openAPIV3Schema
- Auto-detect a schema-like mapping in site.yaml
- Copy every `description` by property path from CRD schema -> site schema
- Also copy the CRD root schema description to:
    1) the site schema root's description (if present)
    2) the site doc's top-level `description` (if present)

I/O:
- Reads --from FILE (CRD) and --to FILE (site), or reads target from stdin if --to omitted
- Writes to stdout by default; use --in-place to overwrite the target
- Logs progress to stderr; safe for pipes, tee, GNU Parallel

Examples:
  ./sync_yaml_descriptions.py --from skupper_site_crd.yaml --to site.yaml --in-place --report
"""

import argparse, sys, io
from typing import Any, Dict, List, Tuple, Optional

# Try ruamel for round-trip preservation; fall back to PyYAML.
USE_RUAMEL = False
yaml = None  # will be assigned
try:
    from ruamel.yaml import YAML
    from ruamel.yaml.comments import CommentedMap, CommentedSeq
    RUAMEL = YAML
    USE_RUAMEL = True
except Exception:
    try:
        import yaml as PYYAML
        yaml = PYYAML
        USE_RUAMEL = False
    except Exception as e:
        print(f"[sync] ERROR: Need a YAML library. Install ruamel.yaml (preferred) or PyYAML. ({e})", file=sys.stderr)
        sys.exit(2)

Json = Any
PathT = Tuple[str, ...]


# ---------- YAML IO ----------

def _load_yaml_stream_ruamel(fh: io.TextIOBase) -> List[Json]:
    y = RUAMEL(typ="rt")
    y.preserve_quotes = True
    docs: List[Json] = []
    for doc in y.load_all(fh):
        if doc is not None:
            docs.append(doc)
    return docs

def _dump_yaml_stream_ruamel(docs: List[Json], fh: io.TextIOBase) -> None:
    y = RUAMEL(typ="rt")
    y.preserve_quotes = True
    # Keep indentation friendly for docs
    y.indent(mapping=2, sequence=4, offset=2)
    y.dump_all(docs, fh)

def _load_yaml_stream_pyyaml(fh: io.TextIOBase) -> List[Json]:
    docs = list(yaml.safe_load_all(fh))
    return [d for d in docs if d is not None]

def _dump_yaml_stream_pyyaml(docs: List[Json], fh: io.TextIOBase) -> None:
    yaml.safe_dump_all(docs, fh, sort_keys=False)

def load_yaml_path_or_stdin(path: Optional[str]) -> List[Json]:
    if path:
        with open(path, "r", encoding="utf-8") as fh:
            return _load_yaml_stream_ruamel(fh) if USE_RUAMEL else _load_yaml_stream_pyyaml(fh)
    return _load_yaml_stream_ruamel(sys.stdin) if USE_RUAMEL else _load_yaml_stream_pyyaml(sys.stdin)

def dump_yaml_stream(docs: List[Json], fh: io.TextIOBase) -> None:
    return _dump_yaml_stream_ruamel(docs, fh) if USE_RUAMEL else _dump_yaml_stream_pyyaml(docs, fh)


# ---------- Schema helpers ----------

def is_mapping(x: Json) -> bool:
    if USE_RUAMEL:
        return isinstance(x, (dict, CommentedMap))
    return isinstance(x, dict)

def is_sequence(x: Json) -> bool:
    if USE_RUAMEL:
        return isinstance(x, (list, CommentedSeq))
    return isinstance(x, list)

def find_crd_schema(doc: Json) -> Optional[Json]:
    """Return openAPIV3Schema dict from a CRD, else None."""
    try:
        spec = doc.get("spec") if is_mapping(doc) else None
        versions = spec.get("versions", []) if is_mapping(spec) else []
        for v in versions or []:
            schema = (v.get("schema") or {}).get("openAPIV3Schema") if is_mapping(v) else None
            if is_mapping(schema):
                return schema
    except Exception:
        pass
    return None

def is_schema_like(node: Json) -> bool:
    return is_mapping(node) and any(k in node for k in ("properties","type","description","items"))

def find_first_schema(node: Json) -> Optional[Json]:
    """Heuristically find first schema-like mapping in a document."""
    if is_schema_like(node) and any(k in node for k in ("properties","type")):
        return node
    if is_mapping(node):
        for _, v in list(node.items()):
            r = find_first_schema(v)
            if r is not None:
                return r
    if is_sequence(node):
        for v in list(node):
            r = find_first_schema(v)
            if r is not None:
                return r
    return None

def walk_schema(node: Json, path: PathT = ()) -> List[Tuple[PathT, Dict[str, Any]]]:
    """Yield (path,node) for nodes in a JSON Schema-like tree."""
    out: List[Tuple[PathT, Dict[str, Any]]] = []
    if not is_mapping(node):
        return out
    out.append((path, node))
    props = node.get("properties")
    if is_mapping(props):
        for key, sub in list(props.items()):
            out.extend(walk_schema(sub, path + (str(key),)))
    if "items" in node:
        out.extend(walk_schema(node.get("items"), path + ("items",)))
    if "additionalProperties" in node:
        ap = node.get("additionalProperties")
        if is_mapping(ap):
            out.extend(walk_schema(ap, path + ("additionalProperties",)))
        elif is_sequence(ap):
            for i, sub in enumerate(ap):
                out.extend(walk_schema(sub, path + ("additionalProperties", str(i))))
    for kw in ("allOf","anyOf","oneOf"):
        seq = node.get(kw)
        if is_sequence(seq):
            for i, sub in enumerate(seq):
                out.extend(walk_schema(sub, path + (kw, str(i))))
    return out

def build_desc_map(schema: Json) -> Dict[PathT, str]:
    out: Dict[PathT, str] = {}
    for p, n in walk_schema(schema):
        d = n.get("description") if is_mapping(n) else None
        if isinstance(d, str):
            out[p] = d
    return out

def path_to_str(p: PathT) -> str:
    return "/".join(p) if p else "<root>"

def set_block_style_if_multiline(node_parent: Json, key: str):
    if not USE_RUAMEL:
        return
    try:
        val = node_parent[key]
        if isinstance(val, str) and ("\n" in val):
            # Force block style on multi-line strings
            node_parent.yaml_set_comment_before_after_key  # probe attribute exists
            node_parent[key].fa.set_block_style()  # type: ignore[attr-defined]
    except Exception:
        pass


# ---------- Main ----------

def main():
    ap = argparse.ArgumentParser(description="Sync all description fields CRD -> site.yaml, preserving formatting.")
    ap.add_argument("--from", dest="src", required=True, help="CRD YAML path")
    ap.add_argument("--to", dest="dst", default=None, help="Target YAML path (site). If omitted, read target from stdin and write to stdout.")
    ap.add_argument("--in-place", action="store_true", help="Overwrite target file (requires --to)")
    ap.add_argument("--report", action="store_true", help="Report updated/missing paths to stderr")
    args = ap.parse_args()

    if not USE_RUAMEL:
        print("[sync] NOTE: ruamel.yaml not available; falling back to PyYAML. Output formatting may change (quotes/newlines).", file=sys.stderr)

    # Load
    src_docs = load_yaml_path_or_stdin(args.src)
    if not src_docs:
        print("[sync] ERROR: source YAML is empty", file=sys.stderr); sys.exit(2)
    dst_docs = load_yaml_path_or_stdin(args.dst)
    if not dst_docs:
        print("[sync] ERROR: target YAML is empty", file=sys.stderr); sys.exit(2)

    src_doc = src_docs[0]
    dst_doc = dst_docs[0]

    # Find schemas
    src_schema = find_crd_schema(src_doc)
    if not is_mapping(src_schema):
        print("[sync] ERROR: could not find CRD openAPIV3Schema in source", file=sys.stderr); sys.exit(2)

    dst_schema = find_first_schema(dst_doc)
    if not is_mapping(dst_schema):
        print("[sync] ERROR: could not find a schema-like mapping in target", file=sys.stderr); sys.exit(2)

    # Build map and apply
    src_descs = build_desc_map(src_schema)
    index: Dict[PathT, Dict[str, Any]] = dict(walk_schema(dst_schema))

    updated = 0
    skipped = 0
    for p, d in src_descs.items():
        node = index.get(p)
        if node is None:
            skipped += 1
            if args.report:
                print(f"[miss]  {path_to_str(p)}", file=sys.stderr)
            continue
        old = node.get("description")
        if old != d:
            node["description"] = d
            if USE_RUAMEL:
                # force block style for multi-line
                set_block_style_if_multiline(node, "description")
            updated += 1
            if args.report:
                print(f"[update] {path_to_str(p)}", file=sys.stderr)

    # Also copy root description → schema root and doc top-level description (if present)
    root_updates = 0
    root_desc = src_schema.get("description")
    if isinstance(root_desc, str):
        if dst_schema.get("description") != root_desc:
            dst_schema["description"] = root_desc
            if USE_RUAMEL:
                set_block_style_if_multiline(dst_schema, "description")
            root_updates += 1
            if args.report:
                print("[update] <schema-root description>", file=sys.stderr)
        if "description" in dst_doc and dst_doc.get("description") != root_desc:
            dst_doc["description"] = root_desc
            if USE_RUAMEL:
                set_block_style_if_multiline(dst_doc, "description")
            root_updates += 1
            if args.report:
                print("[update] <document-top-level description>", file=sys.stderr)

    print(f"[sync] crd->site: updated {updated} (+{root_updates} root), skipped {skipped}", file=sys.stderr)

    # Write
    if args.in_place:
        if not args.dst:
            print("[sync] ERROR: --in-place requires --to FILE", file=sys.stderr); sys.exit(2)
        with open(args.dst, "w", encoding="utf-8") as fh:
            dump_yaml_stream(dst_docs, fh)
    else:
        dump_yaml_stream(dst_docs, sys.stdout)


if __name__ == "__main__":
    main()
