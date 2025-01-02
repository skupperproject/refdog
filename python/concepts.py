from common import *

def generate(model):
    notice("Generating concepts")

    make_dir("input/concepts")

    append = StringBuilder()

    append("---")
    append("refdog_links:")
    append("  - title: Skupper resources")
    append("    url: /resources/index.html")
    append("  - title: Skupper commands")
    append("    url: /commands/index.html")
    append("---")
    append()
    append("# Skupper concepts")
    append()
    append("[Overview](overview.html)")
    append()

    for group in model.groups:
        append(f"#### {group.title}")
        append()
        append("<table class=\"objects\">")

        for concept in group.concepts:
            append(f"<tr><th><a href=\"{concept.href}\">{concept.title}</a></th><td>{concept.summary}</td></tr>")

        append("</table>")
        append()

    append.write("input/concepts/index.md")

    for concept in model.concepts:
        generate_concept(concept)

def generate_concept(concept):
    notice(f"Generating {concept}")

    append = StringBuilder()

    append("---")
    append(generate_object_metadata(concept))
    append("---")
    append()
    append(f"# {concept.title_with_type}")
    append()

    if concept.description:
        append(concept.description.strip())
        append()

    append.write(concept.input_file)

class ConceptModel:
    def __init__(self):
        debug(f"Loading {self}")

        self.concepts = list()
        self.concepts_by_name = dict()
        self.groups = list()

        for yaml_file in list_dir("config/concepts"):
            if yaml_file == "index.yaml":
                continue

            concept_data = read_yaml(join("config/concepts", yaml_file))
            concept = Concept(self, concept_data)

            self.concepts.append(concept)
            self.concepts_by_name[concept.name] = concept

        index_data = read_yaml("config/concepts/index.yaml")

        for group_data in index_data["groups"]:
            self.groups.append(ConceptGroup(self, group_data))

    def __repr__(self):
        return self.__class__.__name__

class Concept(ModelObject):
    pass

class ConceptGroup(ModelObjectGroup):
    def __init__(self, model, data):
        super().__init__(model, data)

        self.concepts = list()

        for concept_name in self.data.get("concepts", []):
            try:
                self.concepts.append(self.model.concepts_by_name[concept_name])
            except KeyError:
                fail(f"{self}: Concept '{concept_name}' not found")
