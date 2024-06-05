from common import *

def generate(model):
    debug("Generating concepts")

    make_dir("input/concepts")

    lines = list()

    def append(line=""):
        if line is None:
            return

        lines.append(line)

    append("# Skupper concepts")
    append()

    for group in model.groups:
        # append(f"- [{group.name}](#{group.id})")
        append(f"- {group.name}")

        for concept in group.concepts:
            append(f"  - [{capitalize(concept.name)}]({concept.id}.html)")

    write("input/concepts/index.md", "\n".join(lines))

    for group in model.groups:
        for concept in group.concepts:
            generate_concept(concept)

def generate_concept(concept):
    debug(f"Generating {concept}")

    lines = list()

    def append(line=""):
        if line is None:
            return

        lines.append(line)

    append("---")
    append("body_class: concept")

    if concept.resource or concept.command:
        append("links:")

    if concept.resource:
        append(f"  - name: {capitalize(concept.resource.name)} resource")
        append(f"    url: /resources/{concept.resource.id}.html")

    if concept.command:
        name = concept.command.name.removeprefix("skupper ")

        append(f"  - name: {capitalize(name)} command")
        append(f"    url: /commands/{concept.command.id}.html")

    if concept.links:
        pass # XXX

    append("---")
    append()
    append(f"# {capitalize(concept.name)}")
    append()
    append("<section>")
    append()

    if concept.description:
        append(concept.description.strip())
        append()

    if concept.links:
        append(generate_links(concept))
        append()

    append("</section>")
    append()

    write(f"input/concepts/{concept.id}.md", "\n".join(lines))

class ConceptModel:
    def __init__(self):
        debug(f"Loading {self}")

        self.data = read_yaml("config/concepts.yaml")
        self.concepts_by_name = dict()

        self.groups = list()

        for group_data in self.data["groups"]:
            self.groups.append(Group(self, group_data))

        for group in self.groups:
            for concept in group.concepts:
                self.concepts_by_name[concept.name] = concept

    def __repr__(self):
        return "concept model"

class Group:
    def __init__(self, model, data):
        self.model = model
        self.data = data

        debug(f"Loading {self}")

        self.concepts = list()

        for concept_data in self.data.get("concepts", []):
            self.concepts.append(Concept(self.model, self, concept_data))

    def __repr__(self):
        return f"group '{self.name}'"

    @property
    def id(self):
        return get_fragment_id(self.name)

    @property
    def name(self):
        return self.data["name"]

    @property
    def description(self):
        return self.data.get("description")

class Concept:
    def __init__(self, model, group, data):
        self.model = model
        self.group = group
        self.data = data

        debug(f"Loading {self}")

    def __repr__(self):
        return f"concept '{self.name}'"

    @property
    def name(self):
        return self.data["name"]

    @property
    def id(self):
        return get_fragment_id(self.name)

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
