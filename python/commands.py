from resources import *

def generate(model):
    debug("Generating commands")

    make_dir("input/commands")

    lines = list()

    def append(line=""):
        if line is None:
            return

        lines.append(line)

    append("# Skupper commands")
    append()

    for group in model.groups:
        # append(f"- [{group.title}]({group.id}.html)")
        append(f"- {group.name}")

        for command in group.commands:
            append(f"  - [{command.name}]({command.id}.html)")

    write("input/commands/index.md", "\n".join(lines))

    for group in model.groups:
        for command in group.commands:
            generate_command(command)

def generate_command(command):
    debug(f"Generating {command}")

    lines = list()

    def append(line=""):
        if line is None:
            return

        lines.append(line)

    append("---")
    append("body_class: command")
    append(generate_object_links(command))
    append("---")
    append()
    append(f"# {command.name}")
    append()
    append("<section>")
    append()

    if command.description:
        append(command.description.strip())
        append()

    append("</section>")
    append()

    if command.usage:
        append("<section>")
        append()
        append("## Usage")
        append()
        append("~~~ shell")
        append(f"$ {command.usage.strip()}")

        if command.output:
            append(command.output.strip())

        append("~~~")
        append()
        append("</section>")
        append()

    if command.examples:
        append("<section>")
        append()
        append("## Examples")
        append()
        append("~~~")
        append(command.examples.strip())
        append("~~~")
        append()
        append("</section>")
        append()

    if command.arguments:
        append("<section>")
        append()
        append("## Arguments")
        append()

        for argument in command.arguments:
            generate_argument(argument, append)

        append("</section>")
        append()

    if command.errors:
        append("<section>")
        append()
        append("## Errors")
        append()

        for error in command.errors:
            append(f"- **{error.message}**")
            append()

            if error.description:
                append(indent(error.description.strip(), 2))
                append()

        append("</section>")
        append()

    if command.notes:
        append("<section>")
        append()
        append("## Notes")
        append()
        append(command.notes.strip()) # XXX styling
        append()
        append("</section>")
        append()

    write(f"input/commands/{command.id}.md", "\n".join(lines))

def generate_argument(argument, append):
    assert argument.property_ or argument.name, argument

    debug(f"Generating {argument}")

    name = nvl(argument.rename, argument.name)
    id_ = get_fragment_id(name)
    argument_info = argument.type

    if argument.format:
        argument_info += f" ({argument.format})"

    if argument.required and argument.default is None:
        argument_info += ", required"

    append(f"- <h3 id=\"{id_}\">{name} <span class=\"argument-info\">{argument_info}</span></h3>")
    append()

    if argument.description:
        append(indent(argument.description.strip(), 2))
        append()

    if argument.default not in (None, False):
        append(indent(generate_attribute_default(argument), 2))
        append()

    if argument.choices:
        append(indent(generate_attribute_choices(argument), 2))
        append()

    if argument.links:
        append(indent(generate_attribute_links(argument), 2))
        append()

    if argument.notes:
        # XXX styling
        append(indent(argument.notes.strip(), 2))
        append()

class CommandModel:
    def __init__(self, resource_model):
        debug(f"Loading {self}")

        self.resource_model = resource_model

        self.data = read_yaml("config/commands.yaml")

        self.global_arguments = list()
        self.groups = list()
        self.commands_by_name = dict()

        # for argument_data in self.data["global_arguments"]:
        #     self.global_arguments.append(Argument(self, self, argument_data))

        for group_data in self.data["groups"]:
            self.groups.append(Group(self, group_data))

        for group in self.groups:
            for command in group.commands:
                self.commands_by_name[command.name] = command

    def __repr__(self):
        return "command model"

class Group:
    def __init__(self, model, data):
        self.model = model
        self.data = data

        debug(f"Loading {self}")

        self.commands = list()

        for command_data in self.data.get("commands", []):
            self.commands.append(Command(self.model, self, command_data))

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

class Command(ModelObject):
    def __init__(self, model, group, data):
        super().__init__("command", model, group, data)

        self.arguments = list()
        self.errors = list()

        for argument_data in self.data.get("arguments", []):
            self.arguments.append(Argument(self.model, self, argument_data))

        for error_data in self.data.get("errors", []):
            self.errors.append(Error(self, error_data))

    @property
    def description(self):
        description = self.data.get("description")

        if description and self.concept and self.concept.description:
            description = description.replace("@concept_description@", self.concept.description.strip())

        if description and self.resource and self.resource.description:
            description = description.replace("@resource_description@", self.resource.description.strip())

        return description

    @property
    def examples(self):
        return self.data.get("examples")

    @property
    def usage(self):
        return self.data.get("usage")

    @property
    def output(self):
        return self.data.get("output")

class Argument(ModelObjectAttribute):
    def __init__(self, model, command, data):
        super().__init__("argument", model, command, data)

    @property
    def command(self):
        return self.object

    @property
    def property_(self):
        if "property" in self.data:
            assert self.command.resource is not None
            assert self.data["property"] in self.command.resource.spec_properties_by_name, \
                "Property '{}' not found in {}".format(self.data["property"], self.command.resource)

            return self.command.resource.spec_properties_by_name[self.data["property"]]

    @property
    def name(self):
        default = argument_name(self.property_.name, self.positional) if self.property_ else None
        return self.data.get("name", default)

    @property
    def rename(self):
        if self.property_ and self.property_.rename:
            default = argument_name(self.property_.rename, self.positional)
        else:
            default = None

        return self.data.get("rename", default)

    @property
    def type(self):
        default = self.property_.type if self.property_ else None
        return self.data.get("type", default)

    @property
    def format(self):
        default = self.property_.format if self.property_ else None
        return self.data.get("format", default)

    @property
    def required(self):
        default = self.property_.required if self.property_ else None
        return self.data.get("required", default)

    @property
    def default(self):
        default = self.property_.default if self.property_ else None
        return self.data.get("default", default)

    @property
    def choices(self):
        default = self.property_.choices if self.property_ else None
        return self.data.get("choices", default)

    @property
    def positional(self):
        return self.data.get("positional")

    @property
    def description(self):
        default = self.property_.description if self.property_ else None
        value = self.data.get("description", default)

        if self.property_ and self.property_.description:
            value = value.replace("@property_description@", self.property_.description)

        return value

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

def argument_name(property_name, positional):
    chars = list()
    prev = None

    if not positional:
        chars.append("--")

    for char in property_name:
        if char.isupper():
            if prev and prev.islower():
                chars.append("-")

            chars.append(char.lower())
        else:
            if prev and prev.isupper() and chars[-2] != "-":
                chars.insert(-1, "-")

            chars.append(char)

        prev = char

    return "".join(chars)
