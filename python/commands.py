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

    if command.options:
        append("<section>")
        append()
        append("## Options")
        append()

        for option in command.options:
            generate_option(option, append)

        if command.standard_options:
            for name, options in command.standard_options:
                append(f"### {name}")
                append()

                for option in options:
                    generate_option(option, append)

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

def generate_option(option, append):
    assert option.property_ or option.name, option

    debug(f"Generating {option}")

    prefix = "" if option.positional else "--"
    name = nvl(option.rename, option.name)
    id_ = get_fragment_id(name)
    option_info = option.type

    if option.format:
        option_info += f" ({option.format})"

    if option.required and option.default is None:
        option_info += ", required"

    if not option.required and option.positional:
        option_info += ", optional"

    append(f"- <h4 id=\"{id_}\">{prefix}{name} <span class=\"option-info\">{option_info}</span></h4>")
    append()

    if option.description:
        append(indent(option.description.strip(), 2))
        append()

    if option.default not in (None, False):
        append(indent(generate_attribute_default(option), 2))
        append()

    if option.choices:
        append(indent(generate_attribute_choices(option), 2))
        append()

    if option.links:
        append(indent(generate_attribute_links(option), 2))
        append()

    if option.notes:
        # XXX styling
        append(indent(option.notes.strip(), 2))
        append()

class CommandModel:
    def __init__(self):
        debug(f"Loading {self}")

        self.data = read_yaml("config/commands.yaml")

        self.global_options = list()
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
    usage = object_property("usage")
    output = object_property("output")
    examples = object_property("examples")

    @property
    def description(self):
        description = self.data.get("description")

        if description and self.concept and self.concept.description:
            description = description.replace("@concept_description@", self.concept.description.strip())

        if description and self.resource and self.resource.description:
            description = description.replace("@resource_description@", self.resource.description.strip())

        return description

    @property
    def options(self):
        options_by_name = dict()

        if "inherit_command_options" in self.data:
            command = self.data["inherit_command_options"]
            options = self.model.commands_by_name[command].options

            options_by_name.update(((x.name, x) for x in options))

        for option_data in self.data.get("options", []):
            name = option_data["name"]
            options_by_name[name] = Option(self.model, self, option_data)

        yield from options_by_name.values()

    @property
    def standard_options(self):
        if "inherit_standard_options" not in self.data:
            return

        for key in self.data["inherit_standard_options"]:
            group = self.model.data["standard_options"][key]
            options = [Option(self.model, self, x) for x in group["options"]]

            yield group["name"], options

    @property
    def errors(self):
        for error_data in self.data.get("errors", []):
            yield Error(self, error_data)

def option_property(name, default=None):
    def get(obj):
        default_ = getattr(obj.property_, name) if obj.property_ else default
        return obj.data.get(name, default_)

    return property(get)

def option_name(property_name):
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

class Option(ModelObjectAttribute):
    type = option_property("type")
    format = option_property("format")
    required = option_property("required", False)
    default = option_property("default")
    choices = option_property("choices")
    links = option_property("links", [])

    @property
    def property_(self):
        if "property" in self.data:
            assert self.object.resource is not None
            assert self.data["property"] in self.object.resource.spec_properties_by_name, \
                "Property '{}' not found in {}".format(self.data["property"], self.object.resource)

            return self.object.resource.spec_properties_by_name[self.data["property"]]

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

class Error:
    message = object_property("message", required=True)
    description = object_property("description")
    notes = object_property("notes")

    def __init__(self, model, data):
        self.model = model
        self.data = data

    def __repr__(self):
        return f"{self.__class__.__name__} '{self.message}'"
