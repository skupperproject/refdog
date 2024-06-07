from plano import *

def indent(text, spaces):
    return "\n".join(f"{' ' * spaces}{line}" for line in text.split("\n"))

def get_fragment_id(name):
    return name.lower().replace(" ", "-")

def generate_object_links(obj):
    links = list()

    if obj.concept:
        name = capitalize(obj.concept.rename)
        links.append((f"{name} concept", f"/concepts/{obj.concept.id}.html"))

    if obj.resource:
        name = capitalize(obj.resource.rename)
        links.append((f"{name} resource", f"/resources/{obj.resource.id}.html"))

    if obj.command:
        name = capitalize(obj.command.rename)
        links.append((f"{name} command", f"/commands/{obj.command.id}.html"))

    for link_data in obj.links:
        links.append((link_data["name"], link_data["url"]))

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
    elif isinstance(attr.default, str) and not attr.default.startswith("_"):
        default = f"`{default}`"

    return f"_Default:_ {default}"

def generate_attribute_choices(attr):
    lines = list()

    lines.append(f"_Choices:_")
    lines.append("")

    for choice in attr.choices:
        lines.append(f" - `{choice['name']}` - {choice['description']}".rstrip())

    return "\n".join(lines)

class ModelObject:
    def __init__(self, type_name, model, group, data):
        self.type_name = type_name
        self.model = model
        self.group = group
        self.data = data

        debug(f"Loading {self}")

    def __repr__(self):
        return f"{self.type_name} '{self.name}'"

    @property
    def name(self):
        return self.data["name"]

    @property
    def rename(self):
        return self.data.get("rename", self.name)

    @property
    def id(self):
        return get_fragment_id(self.name)

    @property
    def concept(self):
        if "concept" in self.data:
            return self.model.concept_model.concepts_by_name[self.data["concept"]]

    @property
    def resource(self):
        if "resource" in self.data:
            return self.model.resource_model.resources_by_name[self.data["resource"]]

    @property
    def command(self):
        if "command" in self.data:
            return self.model.command_model.commands_by_name[self.data["command"]]

    @property
    def description(self):
        return self.data.get("description")

    @property
    def links(self):
        return self.data.get("links", [])

    @property
    def notes(self):
        return self.data.get("notes")

class ModelObjectAttribute:
    def __init__(self, type_name, model, object, data):
        self.type_name = type_name
        self.model = model
        self.object = object
        self.data = data

        debug(f"Loading {self}")

    def __repr__(self):
        return f"{self.type_name} '{self.name}'"

    @property
    def name(self):
        return self.data["name"]

    @property
    def rename(self):
        return self.data.get("rename", self.name)

    @property
    def links(self):
        return self.data.get("links", [])

    @property
    def notes(self):
        return self.data.get("notes")
