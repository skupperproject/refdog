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

        type = other.__class__.__name__.lower()

        lines.append(f"  - name: {capitalize(other.rename)} {type}")
        lines.append(f"    url: /{plural(type)}/{other.id}.html")

    match obj:
        case Concept():
            resource = obj.model.resource_model.resources_by_name.get(capitalize(obj.name))
            command = obj.model.command_model.commands_by_name.get(obj.name)

            add_link(resource)
            add_link(command)
        case Resource():
            concept = obj.model.concept_model.concepts_by_name.get(obj.name.lower())
            command = obj.model.command_model.commands_by_name.get(obj.name.lower())

            add_link(concept)
            add_link(command)
        case Command():
            concept = obj.model.concept_model.concepts_by_name.get(obj.name.lower())
            resource = obj.model.resource_model.resources_by_name.get(capitalize(obj.name))

            add_link(concept)
            add_link(resource)

    for link_data in obj.links:
        lines.append(f"  - name: {link_data['name']}")
        lines.append(f"    url: {link_data['url']}")

    if not lines:
        return

    lines.insert(0, "links:")

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

class ModelObjectAttribute:
    name = object_property("name", required=True)
    description = object_property("description")
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
