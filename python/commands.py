from resources import *

def generate(model):
    debug("Generating commands")

    make_dir("input/commands")

    lines = list()

    def append(line=""):
        if line is None:
            return

        lines.append(line)

    append("---")
    append("links:")
    append("  - name: Skupper concepts")
    append("    url: /concepts/index.html")
    append("  - name: Skupper resources")
    append("    url: /resources/index.html")
    append("---")
    append()
    append("# Skupper commands")
    append()

    for group in model.groups:
        append(f"#### {group.name}")
        append()

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
    append(f"# {capitalize(command.rename)} command")
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
        append("## Options")
        append()

        for argument in command.arguments:
            generate_argument(argument, append)

        if command.standard_arguments:
            for name, arguments in command.standard_arguments:
                append(f"### {name}")
                append()

                for argument in arguments:
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

    prefix = "" if argument.positional else "--"
    name = nvl(argument.rename, argument.name)
    id_ = get_fragment_id(name)
    argument_info = argument.type

    if argument.format:
        argument_info += f" ({argument.format})"

    if argument.required and argument.default is None:
        argument_info += ", required"

    if not argument.required and argument.positional:
        argument_info += ", optional"

    append(f"- <h4 id=\"{id_}\">{prefix}{name} <span class=\"argument-info\">{argument_info}</span></h3>")
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
    def __init__(self):
        debug(f"Loading {self}")

        self.data = read_yaml("config/commands.yaml")

        self.global_arguments = list()
        self.groups = list()
        self.commands_by_name = dict()

        for group_data in self.data["groups"]:
            self.groups.append(CommandGroup(self, group_data))

        for group in self.groups:
            for command in group.commands:
                self.commands_by_name[command.name] = command

    def __repr__(self):
        return self.__class__.__name__

class CommandGroup(ModelObjectGroup):
    def __init__(self, model, data):
        super().__init__(model, data)

        self.commands = list()

        for command_data in self.data.get("commands", []):
            self.commands.append(Command(self.model, self, command_data))

class Command(ModelObject):
    @property
    def description(self):
        description = self.data.get("description")

        if description and self.concept and self.concept.description:
            description = description.replace("@concept_description@", self.concept.description.strip())

        if description and self.resource and self.resource.description:
            description = description.replace("@resource_description@", self.resource.description.strip())

        return description

    @property
    def usage(self):
        return self.data.get("usage")

    @property
    def output(self):
        return self.data.get("output")

    @property
    def examples(self):
        return self.data.get("examples")

    @property
    def arguments(self):
        arguments_by_name = dict()

        if "inherit_command_arguments" in self.data:
            command = self.data["inherit_command_arguments"]
            arguments = self.model.commands_by_name[command].arguments

            arguments_by_name.update(((x.name, x) for x in arguments))

        for argument_data in self.data.get("arguments", []):
            name = argument_data["name"]
            arguments_by_name[name] = Argument(self.model, self, argument_data)

        yield from arguments_by_name.values()

    @property
    def standard_arguments(self):
        if "inherit_standard_arguments" not in self.data:
            return

        for key in self.data["inherit_standard_arguments"]:
            group = self.model.data["standard_arguments"][key]
            arguments = [Argument(self.model, self, x) for x in group["arguments"]]

            yield group["name"], arguments

    @property
    def errors(self):
        for error_data in self.data.get("errors", []):
            yield Error(self, error_data)

class Argument(ModelObjectAttribute):
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
        default = self.property_.choices if self.property_ else []
        return self.data.get("choices", default)

    @property
    def positional(self):
        default = self.required and self.default is None
        return self.data.get("positional", default)

    @property
    def description(self):
        default = self.property_.description if self.property_ else None
        value = self.data.get("description", default)

        if self.property_ and self.property_.description:
            value = value.replace("@property_description@", self.property_.description)

        return value

    @property
    def links(self):
        default = self.property_.links if self.property_ else []
        return self.data.get("links", default)

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

def argument_name(property_name):
    chars = list()
    prev = None

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
