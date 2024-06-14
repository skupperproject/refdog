from plano import *

def indent(text, spaces):
    return "\n".join(f"{' ' * spaces}{line}" for line in text.split("\n"))

def get_fragment_id(name):
    return name.lower().replace(" ", "-")

def generate_object_links(obj):
    from concepts import Concept
    from resources import Resource
    from commands import Command

    lines = list()

    def add_link(other):
        if not other:
            return

        name = other.rename
        type = other.__class__.__name__.lower()

        if not isinstance(other, Command):
            name = capitalize(name)

        lines.append(f"  - name: {name} {type}")
        lines.append(f"    url: /{plural(type)}/{other.id}.html")

    match obj:
        case Concept():
            add_link(obj.resource)
            add_link(obj.command)
        case Resource():
            # add_link(obj.concept)
            add_link(obj.command)
        case Command():
            # add_link(obj.concept)
            add_link(obj.resource)
            add_link(obj.parent)

    for link_data in obj.links:
        lines.append(f"  - name: {link_data['name']}")
        lines.append(f"    url: {link_data['url']}")

    if not lines:
        return

    lines.insert(0, "links:")

    return "\n".join(lines)

def generate_attribute_fields(attr):
    lines = list()

    # No default for status fields
    if attr.default is not None and getattr(attr, "group", None) != "status":
        default = attr.default

        if attr.default is True:
            default = str(attr.default).lower()
        elif isinstance(attr.default, str) and not attr.default.startswith("_"):
            default = f"`{default}`"

        lines.append(f"| Default | {default} |")

    if attr.choices:
        lines.append(f"| Choices | {generate_choices_table(attr)} |")

    if attr.platforms:
        lines.append(f"| Platforms | {', '.join(attr.platforms)} |")

    if attr.links:
        lines.append(f"| See also | {generate_links(attr)} |")

    if lines:
        lines.insert(0, "| | |")
        lines.insert(1, "|-|-|")
        lines.append("")

    return "\n".join(lines)

def generate_choices_table(attr):
    rows = list()

    for choice_data in attr.choices:
        name = choice_data["name"]
        description = choice_data["description"].replace("\n", " ").strip()

        rows.append(f"<tr><td><code>{name}</code></td><td>{description}</td></tr>")

    return "<table>{}</table>".format("".join(rows))

def generate_links(attr):
    links = list()

    for link in attr.links:
        name = link["name"]
        url = link["url"]

        if url.startswith("/"):
            url = "{{site_prefix}}" + url

        links.append(f"[{name}]({url})")

    return ", ".join(links)

def object_property(name, default=None, required=False):
    def get(obj):
        value = obj.data.get(name, default)

        if required and value is None:
            raise Error(f"Property {name} on {obj} is required")

        return value

    return property(get)

class ModelObjectGroup:
    name = object_property("name", required=True)
    description = object_property("description")

    def __init__(self, model, data):
        self.model = model
        self.data = data

        debug(f"Loading {self}")

    def __repr__(self):
        return f"{self.__class__.__name__} '{self.name}'"

    @property
    def id(self):
        return get_fragment_id(self.name)

class ModelObject:
    hidden = object_property("hidden", default=False)
    name = object_property("name", required=True)
    description = object_property("description")
    links = object_property("links", default=[])
    notes = object_property("notes")

    def __init__(self, model, group, data):
        self.model = model
        self.group = group
        self.data = data

        debug(f"Loading {self}")

    def __repr__(self):
        return f"{self.__class__.__name__} '{self.name}'"

    @property
    def rename(self):
        return self.data.get("rename", self.name)

    @property
    def id(self):
        return get_fragment_id(self.name)

    @property
    def concept(self):
        name = self.data.get("concept", self.name.lower())

        try:
            return self.model.concept_model.concepts_by_name[name]
        except KeyError:
            pass

    @property
    def resource(self):
        name = self.data.get("resource", capitalize(self.name))

        try:
            return self.model.resource_model.resources_by_name[name]
        except KeyError:
            pass

    @property
    def command(self):
        name = self.data.get("command", self.name.lower())

        try:
            return self.model.command_model.commands_by_name[name]
        except KeyError:
            pass

class ModelObjectAttribute:
    hidden = object_property("hidden", default=False)
    name = object_property("name", required=True)
    description = object_property("description")
    platforms = object_property("platforms", default=["Kubernetes", "Docker"])
    links = object_property("links", default=[])
    notes = object_property("notes")

    def __init__(self, model, object, data):
        self.model = model
        self.object = object
        self.data = data

        debug(f"Loading {self}")

    def __repr__(self):
        return f"{self.__class__.__name__} '{self.name}'"

    @property
    def rename(self):
        return self.data.get("rename", self.name)
