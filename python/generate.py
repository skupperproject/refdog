from plano import *

def gen():
    model = Model()

    # for name, resource in model.resources.items():
    #     print(resource)
    #     for name, prop in resource.properties.items():
    #         print(prop)

    lines = list()

    def append(line=""):
        lines.append(line)

    append(f"- [Site configuration](#site-configuration)")

    for resource_name, resource in model.resources.items():
        if resource.group != "site-configuration": continue
        append(f"  - [{resource_name}](#{resource_name})")

    append(f"- [Site linking](#site-linking)")

    for resource_name, resource in model.resources.items():
        if resource.group != "site-linking": continue
        append(f"  - [{resource_name}](#{resource_name})")

    append(f"- [Service exposure](#service-exposure)")

    for resource_name, resource in model.resources.items():
        if resource.group != "service-exposure": continue
        append(f"  - [{resource_name}](#{resource_name})")

    toc = "\n".join(lines)
    lines.clear()

    for resource_name, resource in model.resources.items():
        if resource.group != "site-configuration": continue
        append(f"### {resource_name}")

    site_configuration_resources = "\n".join(lines)
    lines.clear()

    for resource_name, resource in model.resources.items():
        if resource.group != "site-linking": continue
        append(f"### {resource_name}")

    site_linking_resources = "\n".join(lines)
    lines.clear()

    for resource_name, resource in model.resources.items():
        if resource.group != "service-exposure": continue
        append(f"### {resource_name}")

    service_exposure_resources = "\n".join(lines)
    lines.clear()

    reference = read("reference.md.in")
    reference = reference.replace("@toc@", toc)
    reference = reference.replace("@site_configuration_resources@", site_configuration_resources)
    reference = reference.replace("@site_linking_resources@", site_linking_resources)
    reference = reference.replace("@service_exposure_resources@", service_exposure_resources)

    write("reference.md", reference)

def object_property(name, default=None):
    def get(obj):
        value = obj.data.get(name, default)

        if is_string(value):
            value = value.replace("@default@", str(nvl(default, "")).strip())
            value = value.strip()

        return value

    return property(get)

class Model:
    title = object_property("title")

    def __init__(self):
        self.data = read_yaml("model.yaml")
        self.resources = dict()

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
        return f"model"

class Resource:
    def __init__(self, model, name, data, crd):
        assert name is not None

        self.model = model
        self.name = name
        self.data = data
        self.crd = crd

        self.properties = dict()

        schema = self.crd["spec"]["versions"][0]["schema"]["openAPIV3Schema"]

        for name, crd in schema["properties"]["spec"]["properties"].items():
            data = self.data["properties"].get(name, {})
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
        return self.data.get("examples")

class Property:
    def __init__(self, model, resource, name, data, crd):
        assert name is not None

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
