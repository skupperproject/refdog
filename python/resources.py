from common import *

import fnmatch

def generate(model):
    debug("Generating resources")

    make_dir("input/resources")

    lines = list()

    def append(line=""):
        if line is None:
            return

        lines.append(line)

    append("---")
    append("links:")
    append("  - name: Skupper concepts")
    append("    url: ../concepts/index.html")
    append("  - name: Skupper commands")
    append("    url: ../commands/index.html")
    append("---")
    append()
    append("# Skupper resources")
    append()

    for group in model.groups:
        append(f"#### {group.name}")
        append()
        append("<table class=\"objects\">")

        for resource in group.resources:
            description = nvl(resource.description, "").replace("\n", " ")
            description = description.split(".")[0]
            description = mistune.html(description)

            append(f"<tr><th><a href=\"{resource.id}.html\">{resource.rename}</a></th><td>{description}</td></tr>")

        append("</table>")
        append()

    write("input/resources/index.md", "\n".join(lines))

    for group in model.groups:
        for resource in group.resources:
            generate_resource(resource)

def generate_resource(resource):
    debug(f"Generating {resource}")

    if resource.hidden:
        debug(f"{resource} is hidden")
        return

    lines = list()

    def append(line=""):
        if line is None:
            return

        lines.append(line)

    append("---")
    append("body_class: object resource")
    append(generate_object_links(resource))
    append("---")
    append()
    append(f"# {capitalize(resource.rename)} resource")
    append()
    append("<section>")
    append()

    if resource.description:
        append(resource.description.strip())
        append()

    append("~~~ yaml")
    append("apiVersion: skupper.io/v1alpha1")
    append(f"kind: {resource.rename}")
    append("metadata:  # Metadata properties")
    append("spec:      # Spec properties")
    append("status:    # Status properties")
    append("~~~")

    append()
    append("</section>")
    append()

    if resource.examples:
        append("<section>")
        append()
        append("## Examples")
        append()

        for example in resource.examples:
            append(example["description"].strip() + ":")
            append()
            append("~~~ yaml")
            append(example["yaml"].strip())
            append("~~~")
            append()

        append("</section>")
        append()

    append("<section>")
    append()
    append("## Metadata properties")
    append()

    for prop in resource.metadata_properties:
        generate_property(prop, append)

    append("</section>")
    append()
    append("<section>")
    append()
    append("## Spec properties")
    append()

    for prop in resource.spec_properties:
        generate_property(prop, append)

    append("</section>")
    append()
    append("<section>")
    append()
    append("## Status properties")
    append()

    for prop in resource.status_properties:
        generate_property(prop, append)

    append("</section>")
    append()

    if resource.notes:
        append("<section class=\"notes\">")
        append()
        append("## Notes")
        append()
        append(resource.notes.strip())
        append()
        append("</section>")
        append()

    write(f"input/resources/{resource.id}.md", "\n".join(lines))

def generate_property(prop, append):
    debug(f"Generating {prop}")

    if prop.hidden:
        debug(f"{prop} is hidden")
        return

    name = nvl(prop.rename, prop.name)
    id_ = get_fragment_id(name)
    prop_info = prop.type

    if prop.format:
        prop_info += f" ({prop.format})"

    if prop.required and prop.default is None:
        prop_info += ", required"

    append(f"- <h3 id=\"{id_}\">{name} <span class=\"attribute-info\">{prop_info}</span></h3>")
    append()

    if prop.description:
        append(indent(prop.description.strip(), 2))
        append()

    append(indent(generate_attribute_fields(prop), 2))
    append()

    if prop.notes:
        append("  <section class=\"notes\">")
        append()
        append(indent(prop.notes.strip(), 2))
        append()
        append("  </section>")
        append()

class ResourceModel:
    def __init__(self):
        debug(f"Loading {self}")

        self.data = read_yaml("config/resources.yaml")

        self.resources = list()
        self.resources_by_name = dict()
        self.groups = list()
        self.crds_by_name = dict()

        for resource_data in self.data["resources"]:
            resource = Resource(self, resource_data)

            self.resources.append(resource)
            self.resources_by_name[resource.name] = resource

        for group_data in self.data["groups"]:
            self.groups.append(ResourceGroup(self, group_data))

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
        return self.__class__.__name__

    def check_properties(self):
        for crd_name, crd_data in self.crds_by_name.items():
            try:
                resource = self.resources_by_name[crd_name]
            except KeyError:
                warning(f"Resource '{crd_name}' is missing")
                continue

            for name, data in crd_data["spec"]["versions"][0]["schema"]["openAPIV3Schema"]["properties"]["spec"]["properties"].items():
                if name not in resource.spec_properties_by_name:
                    warning(f"{resource}: Spec property '{name}' is missing")

            for name, data in crd_data["spec"]["versions"][0]["schema"]["openAPIV3Schema"]["properties"]["status"]["properties"].items():
                if name not in resource.status_properties_by_name:
                    warning(f"{resource}: Status property '{name}' is missing")

        for resource in self.resources:
            try:
                crd_data = self.crds_by_name[resource.name]
            except KeyError:
                warning(f"Resource '{resource.name}' is extra")
                continue

            for prop in resource.spec_properties:
                if prop.name not in crd_data["spec"]["versions"][0]["schema"]["openAPIV3Schema"]["properties"]["spec"]["properties"]:
                    warning(f"{resource}: Spec property '{prop.name}' is extra")

            for prop in resource.status_properties:
                if prop.name not in crd_data["spec"]["versions"][0]["schema"]["openAPIV3Schema"]["properties"]["status"]["properties"]:
                    warning(f"{resource}: Status property '{prop.name}' is extra")

    def get_schema(self, resource):
        try:
            return self.crds_by_name[resource.name]["spec"]["versions"][0]["schema"]["openAPIV3Schema"]
        except KeyError:
            return {}

    def get_schema_property(self, prop):
        if prop.object is None:
            return {}

        schema = self.get_schema(prop.object)

        try:
            return schema["properties"][prop.section]["properties"][prop.name]
        except KeyError:
            return {}

class Resource(ModelObject):
    examples = object_property("examples", default=[])
    description = object_property("description")

    def __init__(self, model, data):
        super().__init__(model, None, data)

        self.metadata_properties = list()
        self.metadata_properties_by_name = dict()

        for data in self.merge_property_data("metadata"):
            prop = Property(self.model, self, data, "metadata")

            self.metadata_properties.append(prop)
            self.metadata_properties_by_name[prop.name] = prop

        self.spec_properties = list()
        self.spec_properties_by_name = dict()

        for data in self.merge_property_data("spec"):
            prop = Property(self.model, self, data, "spec")

            self.spec_properties.append(prop)
            self.spec_properties_by_name[prop.name] = prop

        self.status_properties = list()
        self.status_properties_by_name = dict()

        for data in self.merge_property_data("status"):
            prop = Property(self.model, self, data, "status")

            self.status_properties.append(prop)
            self.status_properties_by_name[prop.name] = prop

    def merge_property_data(self, section):
        inherited_prop_data = dict()

        # XXX Check that the props are well formed here

        for pattern in self.data[section].get("inherit_properties", []):
            for key, data in self.model.data["properties"].items():
                if fnmatch.fnmatchcase(key, pattern):
                    inherited_prop_data[data["name"]] = data
            # for else? XXX

        specific_prop_data = {x["name"]: x for x in self.data[section].get("properties", [])}

        # for name in inherited_props:
        #     if name not in standard_prop_data:
        #         fail(f"Property '{name}' not in standard properties")

        inherited_prop_names = [x for x in inherited_prop_data if x not in specific_prop_data]
        prop_names = list(specific_prop_data.keys()) + inherited_prop_names
        prop_data = dict()

        for name in prop_names:
            prop_data[name] = dict(inherited_prop_data.get(name, {}))
            prop_data[name].update(specific_prop_data.get(name, {}))

        return prop_data.values()

class ResourceGroup(ModelObjectGroup):
    def __init__(self, model, data):
        super().__init__(model, data)

        self.resources = list()

        for resource_name in self.data.get("resources", []):
            self.resources.append(self.model.resources_by_name[resource_name])

def property_property(name):
    def get(obj):
        # XXX if prop.section in ("spec", "status"):
        default = obj.model.get_schema_property(obj).get(name)
        return obj.data.get(name, default)

    return property(get)

class Property(ModelObjectAttribute):
    type = property_property("type")
    format = property_property("format")
    description = property_property("description")

    def __init__(self, model, resource, data, section):
        super().__init__(model, resource, data)

        self.resource = resource
        self.section = section

    @property
    def required(self):
        default = None

        if self.section in ("spec", "status"):
            schema = self.model.get_schema(self.object)
            required_names = schema["properties"][self.section].get("required", [])
            default = self.name in required_names

        return self.data.get("required", default)

    @property
    def default(self):
        default = False if self.type == "boolean" else None
        return self.data.get("default", default)

    @property
    def choices(self):
        default = self.model.get_schema_property(self).get("enum")
        return self.data.get("choices", [])
