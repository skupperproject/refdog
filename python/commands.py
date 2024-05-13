from plano import *

def generate():
    model = Model("config/commands.yaml")
    lines = list()

    def append(line=""):
        if line is None:
            return

        lines.append(line)

    append("#### Contents")
    append()
    append(f"- [Global options](#global-options)")

    for group in model.groups:
        append(f"- [{group.title}](#{group.id})")

        for command in group.commands:
            append(f"  - [{command.title}](#{command.id})")

    append()

    append(f"## Global options")
    append()

    for argument in model.global_arguments:
        generate_argument(argument, append)

    for group in model.groups:
        append(f"## {group.title}")
        append()

        for command in group.commands:
            append(f"### {command.title}")
            append()
            append(command.description)
            append()

            if command.usage:
                append("#### Usage")
                append()
                append("~~~ shell")
                append(f"$ {command.usage.strip()}")

                if command.output:
                    append(command.output.strip())

                append("~~~")
                append()

            if command.examples:
                append("#### Examples")
                append()
                append("~~~")
                append(command.examples.strip())
                append("~~~")
                append()

            if command.arguments:
                append("#### Arguments")
                append()

                for argument in command.arguments:
                    generate_argument(argument, append)

            if command.errors:
                append("#### Errors")
                append()

                for error in command.errors:
                    append(f"- **{error.message}**")
                    append()

                    if error.description:
                        description = "\n".join(f"  {line}" for line in error.description.split("\n"))

                        append(description)
                        append()

            if command.notes:
                notes = "\n".join(f"_{line}_ " for line in command.notes.strip().split("\n"))

                append("#### _Notes_")
                append()
                append(notes)
                append()

    markdown = read("config/commands.md.in")
    markdown = markdown.replace("@content@", "\n".join(lines))

    write("input/commands.md", markdown)

def generate_argument(argument, append):
    title = f"**{argument.name}**"
    default = argument.default

    if argument.variable:
        title = f"**{argument.name}** _{argument.variable}_"

    if argument.default in (True, False):
        default = str(argument.default).lower()

    if argument.default is None:
        append(f"- {title}")
    else:
        append(f"- {title} (default: {default})")

    append()

    if argument.description:
        description = "\n".join(f"  {line}" for line in argument.description.split("\n"))

        append(description)
        append()

    if argument.notes:
        notes = "\n".join(f"  _{line}_" for line in argument.notes.strip().split("\n"))

        append("  ##### _Notes_")
        append()
        append(notes)
        append()

def fragment_id(title):
    return title.lower().replace(" ", "-")

class Model:
    def __init__(self, yaml_file):
        self.data = read_yaml(yaml_file)
        self.global_arguments = list()
        self.groups = list()

        for argument_data in self.data["global_arguments"]:
            self.global_arguments.append(Argument(self, argument_data))

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
            self.commands.append(Command(self.model, command_data))

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

class Command:
    def __init__(self, model, data):
        self.model = model
        self.data = data
        self.arguments = list()
        self.errors = list()

        for argument_data in self.data.get("arguments", []):
            if "include" in argument_data:
                argument_group = argument_data["include"]

                for x in self.model.data["arguments"][argument_group]:
                    self.arguments.append(Argument(self.model, x))
            else:
                self.arguments.append(Argument(self.model, argument_data))

        for error_data in self.data.get("errors", []):
            self.errors.append(Error(self, error_data))

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

    @property
    def examples(self):
        return self.data.get("examples")

    @property
    def usage(self):
        return self.data.get("usage")

    @property
    def output(self):
        return self.data.get("output")

    @property
    def notes(self):
        return self.data.get("notes")

class Argument:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def __repr__(self):
        return f"argument '{self.name}'"

    @property
    def name(self):
        return self.data["name"]

    @property
    def variable(self):
        return self.data.get("variable")

    @property
    def default(self):
        return self.data.get("default")

    @property
    def required(self):
        return self.data.get("required")

    @property
    def positional(self):
        return self.data.get("positional")

    @property
    def description(self):
        return self.data.get("description")

    @property
    def notes(self):
        return self.data.get("notes")

class Error:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def __repr__(self):
        return f"error '{self.message}'"

    @property
    def message(self):
        return self.data["message"]

    @property
    def description(self):
        return self.data.get("description")

    @property
    def notes(self):
        return self.data.get("notes")
