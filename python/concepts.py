from common import *

def generate(model):
    notice("Generating concepts")

    make_dir("input/concepts")

    append = StringBuilder()

    append("---")
    append("title: Concepts")
    append("refdog_links:")
    append("  - title: Resources")
    append("    url: /resources/index.html")
    append("  - title: Commands")
    append("    url: /commands/index.html")
    append("---")
    append()
    append("# Skupper concepts")
    append()
    append("## Index")
    append()

    for group in model.groups:
        append(f"#### {group.title}")
        append()
        append("<table class=\"objects\">")

        for concept in group.objects:
            append(f"<tr><th><a href=\"{concept.href}\">{concept.title}</a></th><td>{concept.summary}</td></tr>")

        append("</table>")
        append()

    append(read("config/concepts/overview.md"))

    append.write("input/concepts/index.md")

    for concept in model.concepts:
        generate_concept(concept)

def generate_concept(concept):
    notice(f"Generating {concept.input_file}")

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

class ConceptModel(Model):
    def __init__(self):
        super().__init__(Concept, "config/concepts")

        self.init(exclude=["overview.md"])

    @property
    def concepts(self):
        return self.objects

class Concept(ModelObject):
    pass
