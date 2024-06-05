from plano import *

def indent(text, spaces):
    return "\n".join(f"{' ' * spaces}{line}" for line in text.split("\n"))

def get_fragment_id(name):
    return name.lower().replace(" ", "-")

def generate_object_links(obj):
    links = list()
    concept = getattr(obj, "concept", None)
    resource = getattr(obj, "resource", None)
    command = getattr(obj, "command", None)

    if concept:
        name = capitalize(concept.name)
        links.append((f"{name} concept", f"/concepts/{concept.id}.html"))

    if resource:
        name = capitalize(resource.name)
        links.append((f"{name} resource", f"/resources/{resource.id}.html"))

    if command:
        name = capitalize(command.name.removeprefix("skupper "))
        links.append((f"{name} command", f"/commands/{command.id}.html"))

    if not links:
        return

    lines = list()

    lines.append("links:")

    for name, url in links:
        lines.append(f"  - name: {name}")
        lines.append(f"    url: {url}")

    return "\n".join(lines)

def generate_attribute_links(attr):
    links = ["[{}]({{{{site_prefix}}}}{})".format(x["name"], x["url"]) for x in attr.links]
    return "_See also:_ " + ", ".join(links)

def generate_attribute_default(attr):
    default = attr.default

    if attr.default is True:
        default = str(attr.default).lower()
    elif isinstance(attr.default, str):
        default = f"`{default}`"

    return f"_Default:_ {default}"

def generate_attribute_choices(attr):
    lines = list()

    lines.append(f"_Choices:_")
    lines.append("")

    for choice in attr.choices:
        lines.append(f" - `{choice['name']}` - {choice['description']}".rstrip())

    return "\n".join(lines)
