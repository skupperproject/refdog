from plano import *

def get_fragment_id(name):
    return name.lower().replace(" ", "-")

def generate_links(obj):
    links = ["[{}]({{{{site_prefix}}}}{})".format(x["name"], x["url"]) for x in obj.links]
    return "_See also:_ " + ", ".join(links)

def generate_default(obj):
    default = obj.default

    if obj.default is True:
        default = str(obj.default).lower()
    elif isinstance(obj.default, str):
        default = f"`{default}`"

    return f"_Default:_ {default}"

def generate_choices(obj):
    lines = list()

    lines.append(f"_Choices:_")
    lines.append("")

    for choice in obj.choices:
        lines.append(f" - `{choice['name']}` - {choice['description']}".rstrip())

    return "\n".join(lines)

def indent(text, spaces):
    return "\n".join(f"{' ' * spaces}{line}" for line in text.split("\n"))
