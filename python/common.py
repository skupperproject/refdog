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

    for other in obj.corresponding_objects:
        add_link(other)

    for concept in obj.related_concepts:
        add_link(concept)

    for resource in obj.related_resources:
        add_link(resource)

    for command in obj.related_commands:
        add_link(command)

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
        lines.append(f"| Choices | {generate_attribute_choices(attr)} |")

    if attr.platforms:
        lines.append(f"| Platforms | {', '.join(attr.platforms)} |")

    links = generate_attribute_links(attr)

    if links:
        lines.append(f"| See also | {links} |")

    if lines:
        lines.insert(0, "| | |")
        lines.insert(1, "|-|-|")
        lines.append("")

    return "\n".join(lines)

def generate_attribute_choices(attr):
    rows = list()

    for choice_data in attr.choices:
        name = choice_data["name"]
        description = choice_data["description"].replace("\n", " ").strip()

        rows.append(f"<tr><td><code>{name}</code></td><td>{description}</td></tr>")

    return "<table class=\"choices\">{}</table>".format("".join(rows))

def generate_attribute_links(attr):
    links = list()

    for concept in attr.related_concepts:
        name = f"{capitalize(concept.name)} concept"
        url = f"{{{{site_prefix}}}}/concepts/{concept.id}.html"

        links.append(f"[{name}]({url})")

    for link_data in attr.links:
        name = link_data["name"]
        url = link_data["url"]

        if url.startswith("/"):
            url = "{{site_prefix}}" + url

        links.append(f"[{name}]({url})")

    return ", ".join(links)

def object_property(name, default=None, required=False):
    def get(obj):
        value = obj.data.get(name, default)

        if required and value is None:
            raise Exception(f"Property '{name}' on {obj.__class__.__name__} is required")

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
    def corresponding_objects(self):
        from concepts import Concept
        from resources import Resource
        from commands import Command

        name = self.name

        if isinstance(self, Command) and self.parent is not None:
            name = self.parent.name

        if not isinstance(self, Concept):
            try:
                yield self.model.concept_model.concepts_by_name[name.lower()]
            except KeyError:
                pass

        if not isinstance(self, Resource):
            try:
                yield self.model.resource_model.resources_by_name[capitalize(name)]
            except KeyError:
                pass

        if not isinstance(self, Command) or (isinstance(self, Command) and self.parent is not None):
            try:
                yield self.model.command_model.commands_by_name[name.lower()]
            except KeyError:
                pass

    @property
    def related_concepts(self):
        for name in self.data.get("related_concepts", []):
            try:
                yield self.model.concept_model.concepts_by_name[name]
            except KeyError:
                fail(f"Related concept '{name}' on {self} not found")

    @property
    def related_resources(self):
        for name in self.data.get("related_resources", []):
            try:
                yield self.model.resource_model.resources_by_name[name]
            except KeyError:
                fail(f"Related resource '{name}' on {self} not found")

    @property
    def related_commands(self):
        for name in self.data.get("related_commands", []):
            try:
                yield self.model.command_model.commands_by_name[name]
            except KeyError:
                fail(f"Related command '{name}' on {self} not found")

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

    @property
    def related_concepts(self):
        try:
            yield self.model.concept_model.concepts_by_name[self.name.lower()]
        except KeyError:
            pass

        for name in self.data.get("related_concepts", []):
            try:
                yield self.model.concept_model.concepts_by_name[name]
            except KeyError:
                fail(f"Related concept '{name}' on {self} not found")
