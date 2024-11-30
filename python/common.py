from plano import *

import html
import mistune

named_links = read_yaml("config/links.yaml")

def indent(text, spaces):
    return "\n".join(f"{' ' * spaces}{line}" for line in text.split("\n"))

def get_fragment_id(name):
    return name.lower().replace(" ", "-")

def get_object_links(obj):
    from concepts import Concept
    from resources import Resource
    from commands import Command

    data = list()

    def add_link(other):
        data.append({
            "title": other.title,
            "url": other.href.removeprefix("{{site_prefix}}"),
        })

    for other in obj.corresponding_objects:
        add_link(other)

    for concept in obj.related_concepts:
        add_link(concept)

    for resource in obj.related_resources:
        add_link(resource)

    for command in obj.related_commands:
        add_link(command)

    for link_data in obj.links:
        data.append(link_data)

    return data

def generate_attribute_fields(attr):
    rows = list()

    # No default for status fields
    if attr.default is not None and getattr(attr, "group", None) != "status":
        default = attr.default

        if default is True:
            default = str(default).lower()
        elif isinstance(default, str):
            if not default.startswith("_"):
                default = f"`{default}`"

            default = mistune.html(default)

        rows.append(f"<tr><th>Default</th><td>{default}</td>")

    if attr.choices:
        rows.append(f"<tr><th>Choices</th><td>{generate_attribute_choices(attr)}</td>")

    if attr.platforms:
        rows.append(f"<tr><th>Platforms</th><td>{', '.join(attr.platforms)}</td>")

    if attr.updatable:
        rows.append(f"<tr><th>Updatable</th><td>{attr.updatable}</td>")

    links = generate_attribute_links(attr)

    if links:
        rows.append(f"<tr><th>See also</th><td>{links}</td>")

    if rows:
        return f"<table class=\"fields\">{''.join(rows)}</table>"

    return ""

def generate_attribute_choices(attr):
    rows = list()

    for choice_data in attr.choices:
        name = choice_data["name"]
        description = choice_data["description"].replace("\n", " ").strip()
        description = mistune.html(description)

        rows.append(f"<tr><th><code>{name}</code></th><td>{description}</td></tr>")

    return "<table class=\"choices\">{}</table>".format("".join(rows))

def generate_attribute_links(attr):
    out = list()

    for link in attr.gather_links():
        out.append(f"<a href=\"{link[1]}\">{link[0]}</a>")

    return ", ".join(out)

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

    def __init__(self, model, data):
        self.model = model
        self.data = data

        debug(f"Loading {self}")

    def __repr__(self):
        return f"{self.__class__.__name__} '{self.name}'"

    @property
    def id(self):
        return get_fragment_id(self.name)

    @property
    def rename(self):
        return self.data.get("rename", self.name)

    @property
    def title(self):
        type = self.__class__.__name__.lower()
        return f"{capitalize(self.rename)} {type}"

    @property
    def href(self):
        type = self.__class__.__name__.lower()
        return f"{{{{site_prefix}}}}/{plural(type)}/{self.id}.html"

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

        if not isinstance(self, Command):
            try:
                yield self.model.command_model.commands_by_id[name.lower()]
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
                yield self.model.command_model.commands_by_id[name]
            except KeyError:
                fail(f"Related command '{name}' on {self} not found")

class ModelObjectAttribute:
    name = object_property("name", required=True)
    group = object_property("group")
    description = object_property("description")
    platforms = object_property("platforms", default=["Kubernetes", "Docker", "Podman", "Linux"])
    updatable = object_property("updatable", default=False)
    links = object_property("links", default=[])
    notes = object_property("notes")
    hidden = object_property("hidden", default=False)

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
    def group(self):
        if self.required:
            return "required"

        return self.data.get("group")

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

    def gather_links(self):
        links = list()

        for concept in self.related_concepts:
            links.append((concept.title, concept.href))

        # XXX Other related things here?

        for link_data in self.links:
            if "name" in link_data:
                title = named_links[link_data["name"]]["title"]
                url = named_links[link_data["name"]]["url"]
            else:
                title = link_data["title"]
                url = link_data["url"]

            links.append((title, url))

        return links
