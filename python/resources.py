from plano import *

def generate():
    model = Model("config/resources.yaml")
    lines = list()
    sections = dict()

    def append(line=""):
        if line is None:
            return

        lines.append(line)

    append("#### Contents")

    for group_name, group in model.groups.items():
        append(f"- [{group.title}](#{group_name})")

        for resource_name, resource in model.resources.items():
            if resource.group == group_name or (resource.group is None and group_name == "everything-else"):
                append(f"  - [{resource_name}](#{resource_name.lower()})")

    for group_name, group in model.groups.items():
        append(f"## {group.title}")
        append()
        append(group.description)
        append()

        for resource_name, resource in model.resources.items():
            if resource.group == group_name or (resource.group is None and group_name == "everything-else"):
                append(f"### {resource_name}")
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

                for prop_name, prop in resource.properties.items():
                    append(f"##### `{prop_name}`")
                    append()

                    append(prop.description or "")
                    append()

                    append(f"_Type_: {capitalize(prop.type)}\\")
                    append(f"_Required_: {'Yes' if prop.required else 'No'}\\")
                    append(f"_Default_: {'False' if prop.default is None and prop.type == 'boolean' else prop.default}")

                # append("#### Status properties")
                # append()

    markdown = read("config/resources.md.in")
    markdown = markdown.replace("@content@", "\n".join(lines))

    write("input/resources.md", markdown)

class Model:
    def __init__(self, yaml_file):
        self.data = read_yaml(yaml_file)
        self.groups = dict()
        self.resources = dict()

        for name, data in self.data["groups"].items():
            self.groups[name] = Group(self, name, data)

        with working_dir("crds"):
            for crd_name in list_dir():
                if crd_name == "skupper_cluster_policy_crd.yaml":
                    continue

                crd = read_yaml(crd_name)

                if crd["kind"] != "CustomResourceDefinition":
                    continue

                name = crd["spec"]["names"]["kind"]
                data = self.data["resources"].get(name, {"properties": {}})

                self.resources[name] = Resource(self, name, data, crd)

    def __repr__(self):
        return "model"

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
    def __init__(self, model, name, data, crd):
        self.model = model
        self.name = name
        self.data = data
        self.crd = crd

        self.properties = dict()

        schema = self.crd["spec"]["versions"][0]["schema"]["openAPIV3Schema"]

        for name, crd in schema["properties"]["spec"]["properties"].items():
            data = self.data.get("properties", {}).get(name, {})
            self.properties[name] = Property(self.model, self, name, data, crd)

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
    def __init__(self, model, resource, name, data, crd):
        self.model = model
        self.resource = resource
        self.name = name
        self.data = data
        self.crd = crd

    def __repr__(self):
        return f"  property '{self.name}' (type={self.type}, required={self.required}, default={mlen(self.default)}, description={mlen(self.description)})"

    @property
    def type(self):
        return self.crd["type"]

    @property
    def required(self):
        names = self.resource.crd["spec"]["versions"][0]["schema"]["openAPIV3Schema"]["properties"]["spec"].get("required", [])
        return self.name in names

    @property
    def default(self):
        return self.data.get("default")

    @property
    def description(self):
        return self.data.get("description")

def mlen(value):
    if value is not None:
        return len(value)

    return "-"
