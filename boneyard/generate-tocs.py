def generate_resource_metadata(resource):
    data = {
        "body_class": "object resource",
        "refdog_object_has_attributes": True,
        "refdog_links": get_object_links(resource),
        "refdog_toc": [
            {
                "title": "Overview",
                "id": "",
            }
        ],
    }

    if resource.examples:
        data["refdog_toc"].append({
            "title": "Examples",
            "id": "examples",
        })

    data["refdog_toc"].extend([
        {
            "title": "Metadata properties",
            "id": "metadata-properties",
            # "children": [{"title": x.name, "id": x.id} for x in resource.metadata_properties if not x.hidden],
        },
        {
            "title": "Spec properties",
            "id": "spec-properties",
            # "children": [{"title": x.name, "id": x.id} for x in resource.spec_properties if not x.hidden],
        },
        {
            "title": "Status properties",
            "id": "status-properties",
            # "children": [{"title": x.name, "id": x.id} for x in resource.status_properties if not x.hidden],
        },
    ])

    return emit_yaml(data).strip()

def generate_command_metadata(command):
    data = {
        "body_class": "object command",
        "refdog_object_has_attributes": True,
        "refdog_links": get_object_links(command),
        "refdog_toc": [
            {
                "title": "Overview",
                "id": "",
            },
        ],
    }

    sections = "Usage", "Output", "Subcommands", "Examples"

    for section in sections:
        items = getattr(command, section.lower())

        if items:
            data["refdog_toc"].append({
                "title": section,
                "id": make_fragment_id(section),
            })

    children = list()

    for group in ("positional", "required", "frequently-used", None, "advanced"):
        children.extend([{"title": x.syntax_name, "id": x.id} for x in command.options
                         if not x.hidden and x.group == group])

    if command.subcommands:
        pass
    else:
        data["refdog_toc"].extend([
            {
                "title": "Primary options",
                "id": "primary-options",
                # "children": children, XXX
            },
        ])

        children = [{"title": x.syntax_name, "id": x.id} for x in command.options
                    if not x.hidden and x.group == "global"]

        data["refdog_toc"].extend([
            {
                "title": "Global options",
                "id": "global-options",
                # "children": children, XXX
            },
        ])

    return emit_yaml(data).strip()
