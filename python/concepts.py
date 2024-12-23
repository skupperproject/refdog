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
            title = concept.title.removesuffix(" concept")
            description = nvl(concept.description, "").replace("\n", " ")
            description = re.split(r"\.\s", description)[0]
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
    append(generate_concept_metadata(concept))
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

def generate_concept_metadata(concept):
    data = dict()

    data["body_class"] = "object concept"
    data["refdog_links"] = get_object_links(concept)

    return emit_yaml(data).strip()

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
        return "concept model"

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
