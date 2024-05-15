from common import *

def generate():
    model = ResourceModel()
    lines = list()

    def append(line=""):
        if line is None:
            return

        lines.append(line)

    append("#### Contents")

    for group in model.groups:
        append(f"- [{group.title}](#{group.id})")

        for resource in group.resources:
            append(f"  - [{resource.name}](#{resource.name.lower()})") # XXX resource.id

    for group in model.groups:
        append(f"## {group.title}")
        append()
        append(group.description)
        append()

        for resource in group.resources:
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
        # XXX An example object
        append(example["description"])
        append()
        append("~~~ yaml")
        append(example["yaml"])
        append("~~~")

    append("#### Spec properties")
    append()

    for prop in resource.properties:
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
        debug(f"Loading {self}")

        self.data = read_yaml("config/resources.yaml")

        self.groups = list()
        self.crds = dict()
        self.resources = dict()

        with working_dir("crds"):
            for crd_file in list_dir():
                if crd_file == "skupper_cluster_policy_crd.yaml":
                    continue

                crd_data = read_yaml(crd_file)

                if crd_data["kind"] != "CustomResourceDefinition":
                    continue

                kind = crd_data["spec"]["names"]["kind"]

                self.crds[kind] = crd_data

        for group_data in self.data["groups"]:
            self.groups.append(Group(self, group_data))

        for group in self.groups:
            for resource in group.resources:
                self.resources[resource.name] = resource

    def __repr__(self):
        return "resource model"

class Group:
    def __init__(self, model, data):
        self.model = model
        self.data = data

        debug(f"Loading {self}")

        self.resources = list()

        for resource_data in self.data.get("resources", []):
            crd_data = self.model.crds[resource_data["name"]]
            self.resources.append(Resource(self.model, self, resource_data, crd_data))

    def __repr__(self):
        return f"group '{self.title}'"

    @property
    def id(self):
        return fragment_id(self.title)

    @property
    def title(self):
        return self.data["title"]

    @property
    def description(self):
        return self.data.get("description")

class Resource:
    def __init__(self, model, group, data, crd_data):
        self.model = model
        self.group = group
        self.data = data
        self.crd_data = crd_data

        debug(f"Loading {self}")

        self.properties = list()
        self.properties_by_name = dict()

        schema = self.crd_data["spec"]["versions"][0]["schema"]["openAPIV3Schema"]

        for name, crd_data in schema["properties"]["spec"]["properties"].items():
            for property_data in self.data.get("properties", []):
                if property_data["name"] == name:
                    break
            else:
                property_data = {"name": name}

            prop = Property(self.model, self, property_data, crd_data)

            self.properties.append(prop)
            self.properties_by_name[prop.name] = prop

        for property_data in self.data.get("properties", []):
            if property_data["name"] not in self.properties_by_name:
                prop = Property(self.model, self, property_data, None)

                self.properties.append(prop)
                self.properties_by_name[prop.name] = prop

    def __repr__(self):
        return f"resource '{self.name}'"

    @property
    def name(self):
        return self.data["name"]

    @property
    def description(self):
        return self.data.get("description")

    @property
    def examples(self):
        return self.data.get("examples", [])

class Property:
    def __init__(self, model, resource, data, crd_data):
        self.model = model
        self.resource = resource
        self.data = data
        self.crd_data = crd_data

        debug(f"Loading {self}")

    def __repr__(self):
        return f"property '{self.name}'"

    @property
    def name(self):
        return self.data["name"]

    @property
    def type(self):
        default = self.crd_data.get("type") if self.crd_data else None
        return self.data.get("type", default)

    @property
    def format(self):
        default = self.crd_data.get("format") if self.crd_data else None
        return self.data.get("format", default)

    @property
    def required(self):
        required_names = self.resource.crd_data["spec"]["versions"][0]["schema"]["openAPIV3Schema"]["properties"]["spec"].get("required", [])
        default = self.name in required_names
        return self.data.get("required", default)

    @property
    def default(self):
        default = False if self.type == "boolean" else None
        return self.data.get("default", default)

    @property
    def description(self):
        default = self.crd_data.get("description") if self.crd_data else None
        return self.data.get("description", default)

    @property
    def notes(self):
        return self.data.get("notes")
