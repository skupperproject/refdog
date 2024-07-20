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
        append("<table class=\"objects\">")

        for concept in group.concepts:
            title = concept.title.removesuffix(" concept")
            description = nvl(concept.description, "").replace("\n", " ")
            description = description.split(".")[0]
            description = mistune.html(description)

            append(f"<tr><th><a href=\"{concept.href}\">{title}</a></th><td>{description}</td></tr>")

        append("</table>")
        append()

    write("input/concepts/index.md", "\n".join(lines))

    for concept in model.concepts:
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
    append(f"# {concept.title}")
    append()
    append("<section>")
    append()

    if concept.description:
        append(concept.description.strip())
        append()

    append("</section>")
    append()

    if concept.notes:
        append("<section class=\"notes\">")
        append()
        append("## Notes")
        append()
        append(concept.notes.strip())
        append()
        append("</section>")
        append()

    write(f"input/concepts/{concept.id}.md", "\n".join(lines))

class ConceptModel:
    def __init__(self):
        debug(f"Loading {self}")

        self.data = read_yaml("config/concepts.yaml")

        self.concepts = list()
        self.concepts_by_name = dict()
        self.groups = list()

        for concept_data in self.data["concepts"]:
            concept = Concept(self, concept_data)

            self.concepts.append(concept)
            self.concepts_by_name[concept.name] = concept

        for group_data in self.data["groups"]:
            self.groups.append(ConceptGroup(self, group_data))

    def __repr__(self):
        return "concept model"

class Concept(ModelObject):
    pass

class ConceptGroup(ModelObjectGroup):
    def __init__(self, model, data):
        super().__init__(model, data)

        self.concepts = list()

        for concept_name in self.data.get("concepts", []):
            self.concepts.append(self.model.concepts_by_name[concept_name])
