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

    for option in model.global_options:
        generate_option(option, append)

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

            if command.options:
                append("#### Options")
                append()

                for option in command.options:
                    generate_option(option, append)

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

def generate_option(option, append):
    title = f"**{option.name}**"
    default = option.default

    if option.variable:
        title = f"**{option.name}** _{option.variable}_"

    if option.default in (True, False):
        default = str(option.default).lower()

    if option.default is None:
        append(f"- {title}")
    else:
        append(f"- {title} (default: {default})")

    append()

    if option.description:
        description = "\n".join(f"  {line}" for line in option.description.split("\n"))

        append(description)
        append()

    if option.notes:
        notes = "\n".join(f"  _{line}_" for line in option.notes.strip().split("\n"))

        append("  ##### _Notes_")
        append()
        append(notes)
        append()

def fragment_id(title):
    return title.lower().replace(" ", "-")

class Model:
    def __init__(self, yaml_file):
        self.data = read_yaml(yaml_file)
        self.global_options = list()
        self.groups = list()

        for option_data in self.data["global_options"]:
            self.global_options.append(Option(self, option_data))

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
        self.options = list()
        self.errors = list()

        for option_data in self.data.get("options", []):
            if "include" in option_data:
                option_group = option_data["include"]

                for x in self.model.data["options"][option_group]:
                    self.options.append(Option(self.model, x))
            else:
                self.options.append(Option(self.model, option_data))

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

class Option:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def __repr__(self):
        return f"option '{self.name}'"

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
