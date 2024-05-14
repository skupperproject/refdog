from plano import *

def generate():
    model = ResourceModel()
    lines = list()

    def append(line=""):
        if line is None:
            return

        lines.append(line)

    append("#### Contents")

    for group_name, group in model.groups.items():
        append(f"- [{group.title}](#{group_name})")

        for resource_name, resource in model.resources.items():
            if resource.group != group_name or (resource.group is None and group_name != "everything-else"):
                continue

            append(f"  - [{resource_name}](#{resource_name.lower()})")

    for group_name, group in model.groups.items():
        append(f"## {group.title}")
        append()
        append(group.description)
        append()

        for resource in model.resources.values():
            if resource.group != group_name or (resource.group is None and group_name != "everything-else"):
                continue

            generate_resource(resource, append)

    markdown = read("config/resources.md.in")
    markdown = markdown.replace("@content@", "\n".join(lines))

    write("input/resources.md", markdown)

def generate_resource(resource, append):
    debug(f"Generating {resource}")

    append(f"### {resource.name}")
    append()
    append(resource.description)

    append("#### Examples")
    append()

    for example in resource.examples:
        append(example["description"])
        append()
        append("~~~ yaml")
        append(example["yaml"])
        append("~~~")

    append("#### Spec properties")
    append()

    for prop in resource.properties.values():
        generate_property(prop, append)

    # append("#### Status properties")
    # append()

def generate_property(prop, append):
    debug(f"Generating {prop}")

    append(f"##### `{prop.name}`")
    append()

    append(prop.description or "")
    append()

    append(f"_Type:_ {capitalize(prop.type)}\\")
    append(f"_Required:_ {'Yes' if prop.required else 'No'}\\")
    append(f"_Default:_ {'False' if prop.default is None and prop.type == 'boolean' else prop.default}")


class ResourceModel:
    def __init__(self):
        self.data = read_yaml("config/resources.yaml")
        self.groups = dict()
        self.resources = dict()

        for name, data in self.data["groups"].items():
            self.groups[name] = Group(self, name, data)

        with working_dir("crds"):
            for crd_name in list_dir():
                if crd_name == "skupper_cluster_policy_crd.yaml":
                    continue

                crd_data = read_yaml(crd_name)

                if crd_data["kind"] != "CustomResourceDefinition":
                    continue

                name = crd_data["spec"]["names"]["kind"]
                data = self.data["resources"].get(name, {"properties": {}})

                self.resources[name] = Resource(self, name, data, crd_data)

    def __repr__(self):
        return "resource model"

class Group:
    def __init__(self, model, name, data):
        self.model = model
        self.name = name
        self.data = data

    def __repr__(self):
        return f"group '{self.name}'"

    @property
    def title(self):
        return self.data["title"]

    @property
    def description(self):
        return self.data.get("description")

class Resource:
    def __init__(self, model, name, data, crd_data):
        self.model = model
        self.name = name
        self.data = data
        self.crd_data = crd_data

        self.properties = dict()

        schema = self.crd_data["spec"]["versions"][0]["schema"]["openAPIV3Schema"]

        for name, crd_data in schema["properties"]["spec"]["properties"].items():
            data = self.data.get("properties", {}).get(name, {})
            self.properties[name] = Property(self.model, self, name, data, crd_data)

        for name, data in self.data.get("properties", {}).items():
            if name in self.properties:
                continue

            self.properties[name] = Property(self.model, self, name, data, None)

    def __repr__(self):
        return f"resource '{self.name}' (group={nvl(self.group, '-')}, description={mlen(self.examples)}, examples={mlen(self.examples)})"

    @property
    def group(self):
        return self.data.get("group")

    @property
    def description(self):
        return self.data.get("description")

    @property
    def examples(self):
        return self.data.get("examples", [])

class Property:
    def __init__(self, model, resource, name, data, crd_data):
        self.model = model
        self.resource = resource
        self.name = name
        self.data = data
        self.crd_data = crd_data

    def __repr__(self):
        return f"property '{self.name}' (type={self.type}, required={self.required}, default={mlen(self.default)})"

    @property
    def type(self):
        default = self.crd_data.get("type") if self.crd_data else None
        return self.data.get("type", default)

    @property
    def required(self):
        required_names = self.resource.crd_data["spec"]["versions"][0]["schema"]["openAPIV3Schema"]["properties"]["spec"].get("required", [])
        default = self.name in required_names
        return self.data.get("required", default)

    @property
    def default(self):
        return self.data.get("default")

    @property
    def description(self):
        default = self.crd_data.get("description") if self.crd_data else None
        return self.data.get("description", default)

    @property
    def notes(self):
        return self.data.get("notes")

def mlen(value):
    if value is not None:
        return len(value)

    return "-"
