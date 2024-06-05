from common import *

def generate(model):
    debug("Generating resources")

    make_dir("input/resources")

    lines = list()

    def append(line=""):
        if line is None:
            return

        lines.append(line)

    append("# Skupper resources")
    append()

    for group in model.groups:
        # append(f"- [{group.name}](#{group.id})")
        append(f"- {group.name}")

        for resource in group.resources:
            append(f"  - [{resource.name}]({resource.id}.html)")

    write("input/resources/index.md", "\n".join(lines))

    for group in model.groups:
        for resource in group.resources:
            generate_resource(resource)

def generate_resource(resource):
    debug(f"Generating {resource}")

    lines = list()

    def append(line=""):
        if line is None:
            return

        lines.append(line)

    append("---")
    append("body_class: resource")

    if resource.concept or resource.command:
        append("links:")

    if resource.concept:
        append(f"  - name: {capitalize(resource.concept.name)} concept")
        append(f"    url: /concepts/{resource.concept.id}.html")

    if resource.command:
        name = resource.command.name.removeprefix("skupper ")

        append(f"  - name: {capitalize(name)} command")
        append(f"    url: /commands/{resource.command.id}.html")

    if resource.links:
        pass # XXX

    append("---")
    append()
    append(f"# {resource.name}")
    append()
    append("<section>")
    append()

    if resource.description:
        append(resource.description.strip())
        append()

    append("</section>")
    append()

    if resource.examples:
        append("<section>")
        append()
        append("## Examples")
        append()

        for example in resource.examples:
            # XXX An example object
            append(example["description"].strip() + ":")
            append()
            append("~~~ yaml")
            append(example["yaml"].strip())
            append("~~~")
            append()

        append("</section>")
        append()

    if resource.spec_properties:
        append("<section>")
        append()
        append("## Spec properties")
        append()

        for prop in resource.spec_properties:
            generate_property(prop, append)

        append("</section>")
        append()

    if resource.status_properties:
        append("<section>")
        append()
        append("## Status properties")
        append()

        for prop in resource.status_properties:
            generate_property(prop, append)

        append("</section>")
        append()

    if resource.notes:
        append("<section>")
        append()
        append("## Notes")
        append()
        append(resource.notes.strip()) # XXX styling
        append()
        append("</section>")
        append()

    write(f"input/resources/{resource.id}.md", "\n".join(lines))

def generate_property(prop, append):
    debug(f"Generating {prop}")

    name = nvl(prop.rename, prop.name)
    id_ = get_fragment_id(name)
    prop_info = prop.type

    if prop.format:
        prop_info += f" ({prop.format})"

    if prop.required and prop.default is None:
        prop_info += ", required"

    append(f"- <h3 id=\"{id_}\">{name} <span class=\"property-info\">{prop_info}</span></h3>")
    append()

    if prop.description:
        append(indent(prop.description.strip(), 2))
        append()

    if prop.default not in (None, False):
        append(indent(generate_default(prop), 2))
        append()

    if prop.choices:
        append(indent(generate_choices(prop), 2))
        append()

    if prop.links:
        append(indent(generate_links(prop), 2))
        append()

    if prop.notes:
        # XXX styling
        append(indent(prop.notes.strip(), 2))
        append()

class ResourceModel:
    def __init__(self, concept_model):
        debug(f"Loading {self}")

        self.concept_model = concept_model
        self.concept_model.resource_model = self

        self.data = read_yaml("config/resources.yaml")

        self.groups = list()
        self.resources_by_name = dict()
        self.crds_by_name = dict()

        for group_data in self.data["groups"]:
            self.groups.append(Group(self, group_data))

        for group in self.groups:
            for resource in group.resources:
                self.resources_by_name[resource.name] = resource

        with working_dir("crds"):
            for crd_file in list_dir():
                if crd_file == "skupper_cluster_policy_crd.yaml":
                    continue

                crd_data = read_yaml(crd_file)

                if crd_data["kind"] != "CustomResourceDefinition":
                    continue

                kind = crd_data["spec"]["names"]["kind"]

                self.crds_by_name[kind] = crd_data

        self.check_properties()

    def __repr__(self):
        return "resource model"

    def check_properties(self):
        for crd_name, crd_data in self.crds_by_name.items():
            if crd_name not in self.resources_by_name:
                print(f"Missing: resource '{crd_name}'")

            resource = self.resources_by_name[crd_name]

            for name, data in crd_data["spec"]["versions"][0]["schema"]["openAPIV3Schema"]["properties"]["spec"]["properties"].items():
                if name not in resource.spec_properties_by_name:
                    print(f"Missing: {resource}: {name}")

            for name, data in crd_data["spec"]["versions"][0]["schema"]["openAPIV3Schema"]["properties"]["status"]["properties"].items():
                if name not in resource.status_properties_by_name:
                    print(f"Missing: {resource}: {name}")

    def get_schema(self, resource):
        crd = self.crds_by_name[resource.name]

        try:
            return crd["spec"]["versions"][0]["schema"]["openAPIV3Schema"]
        except KeyError:
            return {}

    def get_schema_property(self, prop):
        schema = self.get_schema(prop.resource)

        try:
            return schema["properties"][prop.group]["properties"][prop.name]
        except KeyError:
            return {}

class Group:
    def __init__(self, model, data):
        self.model = model
        self.data = data

        debug(f"Loading {self}")

        self.resources = list()

        for resource_data in self.data.get("resources", []):
            self.resources.append(Resource(self.model, self, resource_data))

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

class Resource:
    def __init__(self, model, group, data):
        self.model = model
        self.group = group
        self.data = data

        debug(f"Loading {self}")

        self.spec_properties = list()
        self.spec_properties_by_name = dict()

        for property_data in self.data.get("spec_properties", []):
            prop = Property(self.model, self, "spec", property_data)

            self.spec_properties.append(prop)
            self.spec_properties_by_name[prop.name] = prop

        self.status_properties = list()
        self.status_properties_by_name = dict()

        for property_data in self.data.get("status_properties", []):
            prop = Property(self.model, self, "status", property_data)

            self.status_properties.append(prop)
            self.status_properties_by_name[prop.name] = prop

    def __repr__(self):
        return f"resource '{self.name}'"

    @property
    def name(self):
        return self.data["name"]

    @property
    def id(self):
        return get_fragment_id(self.name)

    @property
    def concept(self):
        if "concept" in self.data:
            return self.model.concept_model.concepts_by_name[self.data["concept"]]

    @property
    def command(self):
        if "command" in self.data:
            return self.model.command_model.commands_by_name[self.data["command"]]

    @property
    def description(self):
        # XXX Default to CRD description

        description = self.data.get("description")

        if description and self.concept and self.concept.description:
            description = description.replace("@concept_description@", self.concept.description.strip())

        return description

    @property
    def links(self):
        return self.data.get("links", [])

    @property
    def examples(self):
        return self.data.get("examples", [])

    @property
    def notes(self):
        return self.data.get("notes")

class Property:
    def __init__(self, model, resource, group, data):
        self.model = model
        self.resource = resource
        self.group = group # "spec" or "status"
        self.data = data

        debug(f"Loading {self}")

    def __repr__(self):
        return f"property '{self.name}'"

    @property
    def name(self):
        return self.data["name"]

    @property
    def rename(self):
        return self.data.get("rename")

    @property
    def type(self):
        default = self.model.get_schema_property(self).get("type")
        return self.data.get("type", default)

    @property
    def required(self):
        schema = self.model.get_schema(self.resource)
        required_names = schema["properties"][self.group].get("required", [])
        default = self.name in required_names

        return self.data.get("required", default)

    @property
    def format(self):
        default = self.model.get_schema_property(self).get("format")
        return self.data.get("format", default)

    @property
    def default(self):
        default = False if self.type == "boolean" else None
        return self.data.get("default", default)

    @property
    def choices(self):
        return self.data.get("choices", [])

    @property
    def description(self):
        default = self.model.get_schema_property(self).get("description")
        return self.data.get("description", default)

    @property
    def links(self):
        return self.data.get("links", [])

    @property
    def notes(self):
        return self.data.get("notes")
