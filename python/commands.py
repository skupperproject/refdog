from plano import *

def generate():
    model = Model("commands.yaml")
    lines = list()
    # sections = dict()

    def append(line=""):
        if line is None:
            return

        lines.append(line)

    for group in model.groups:
        append(f"- [{group.title}](#)")

        for command in group.commands:
            append(f"  - [{command.title}](#)")

    markdown = read("commands.md.in")
    markdown = markdown.replace("@content@", "\n".join(lines))

    write("commands.md", markdown)

class Model:
    def __init__(self, yaml_file):
        self.data = read_yaml(yaml_file)
        self.groups = list()

        for group_data in self.data["groups"]:
            self.groups.append(Group(self, group_data))

    def __repr__(self):
        return "model"

class Group:
    def __init__(self, model, data):
        self.model = model
        self.data = data
        self.commands = list()

        for command_data in self.data["commands"]:
            self.commands.append(Command(self, command_data))

    def __repr__(self):
        return f"group '{self.title}'"

    @property
    def title(self):
        return self.data["title"]

    @property
    def description(self):
        return self.data.get("description")

class Command:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def __repr__(self):
        return f"group '{self.title}'"

    @property
    def title(self):
        return self.data["title"]

    @property
    def description(self):
        return self.data.get("description")
