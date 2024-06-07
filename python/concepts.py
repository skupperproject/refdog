from common import *

def generate(model):
    debug("Generating concepts")

    make_dir("input/concepts")

    lines = list()

    def append(line=""):
        if line is None:
            return

        lines.append(line)

    append("---")
    append("links:")
    append("  - name: Skupper resources")
    append("    url: /resources/index.html")
    append("  - name: Skupper commands")
    append("    url: /commands/index.html")
    append("---")
    append()
    append("# Skupper concepts")
    append()

    for group in model.groups:
        append(f"#### {group.name}")
        append()

        for concept in group.concepts:
            append(f"  - [{capitalize(concept.rename)}]({concept.id}.html)")

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
    append(generate_object_links(concept))
    append("---")
    append()
    append(f"# {capitalize(concept.rename)} concept")
    append()
    append("<section>")
    append()

    if concept.description:
        append(concept.description.strip())
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

class Concept(ModelObject):
    def __init__(self, model, group, data):
        super().__init__("concept", model, group, data)
