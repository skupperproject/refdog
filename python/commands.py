from resources import *

import fnmatch

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
            title = command.title.removesuffix(" command")
            description = f"Overview of {command.name} commands"

            append("<table class=\"objects\">")
            append(f"<tr><th><a href=\"{command.href}\">{title}</a></th><td>{description}</td></tr>")

            for subcommand in command.subcommands:
                title = subcommand.title.removesuffix(" commands")
                title = title.removesuffix(" command")
                description = nvl(subcommand.description, "").replace("\n", " ")
                description = description.split(".")[0]
                description = mistune.html(description)

                append(f"<tr><th><a href=\"{subcommand.href}\">{title}</a></th><td>{description}</td></tr>")

            append("</table>")
            append()

        append()

    write("input/commands/index.md", "\n".join(lines))

    for command in model.commands:
        generate_command(command)

        for subcommand in command.subcommands:
            generate_command(subcommand)

def generate_command(command):
    debug(f"Generating {command}")

    lines = list()

    def append(line=""):
        if line is None:
            return

        lines.append(line)

    append("---")
    append("body_class: object command")
    append(generate_object_links(command))
    append("---")
    append()
    append(f"# {command.title}")
    append()
    append("<section>")
    append()

    if command.description:
        append(command.description.strip())
        append()

    append("</section>")
    append()
    append("<section>")
    append()
    append("## Usage")
    append()
    append("~~~ shell")
    append(f"{generate_usage(command)}")
    append("~~~")
    append()
    append("</section>")
    append()

    if command.output:
        append("<section>")
        append()
        append("## Output")
        append()
        append("~~~ console")
        append(command.output.strip())
        append("~~~")
        append()
        append("</section>")
        append()

    if command.subcommands:
        append("<section>")
        append()
        append("## Subcommands")
        append()
        append("<table class=\"objects\">")

        for subcommand in command.subcommands:
            description = nvl(subcommand.description, "").replace("\n", " ")
            description = description.split(".")[0]
            description = mistune.html(description)

            append(f"<tr><th><a href=\"{subcommand.name}.html\">{subcommand.name}</a></th><td>{description}</td></tr>")

        append("</table>")
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

        append("</section>")
        append()

    if command.errors:
        append("<section>")
        append()
        append("## Errors")
        append()

        for error in command.errors:
            generate_error(error, append)

        append("</section>")
        append()

    if command.notes:
        append("<section class=\"notes\">")
        append()
        append("## Notes")
        append()
        append(command.notes.strip())
        append()
        append("</section>")
        append()

    if command.subcommands:
        write(f"input/commands/{command.id}/index.md", "\n".join(lines))
    else:
        write(f"input/commands/{command.id}.md", "\n".join(lines))

def generate_usage(command):
    parts = ["skupper"]
    parts.extend([x.name for x in reversed(list(command.ancestors))])
    parts.append(command.name)

    if command.subcommands:
        parts.append("[subcommand]")

    for option in command.options:
        if option.positional:
            if option.required:
                parts.append(f"<{option.name}>")
            else:
                parts.append(f"[{option.name}]")

    parts.append("[options]")

    return " ".join(parts)

def generate_option(option, append):
    debug(f"Generating {option}")

    prefix = "" if option.positional else "--"
    id_ = get_fragment_id(option.name)
    option_info = option.type

    if option.format:
        option_info += f" ({option.format})"

    if option.required and option.default is None:
        option_info += ", required"

    if not option.required and option.positional:
        option_info += ", optional"

    append(f"- <h3 id=\"{id_}\">{prefix}{option.name} <span class=\"attribute-info\">{option_info}</span></h3>")
    append()

    if option.description:
        append(indent(option.description.strip(), 2))
        append()

    append(indent(generate_attribute_fields(option), 2))
    append()

    if option.notes:
        append("  <section class=\"notes\">")
        append()
        append(indent(option.notes.strip(), 2))
        append()
        append("  </section>")
        append()

def generate_error(error, append):
    append(f"- **{error.message}**")
    append()

    if error.description:
        append(indent(error.description.strip(), 2))
        append()

class CommandModel:
    def __init__(self):
        debug(f"Loading {self}")

        self.data = read_yaml("config/commands.yaml")

        self.commands = list()
        self.commands_by_id = dict()
        self.groups = list()

        for command_data in self.data["commands"]:
            command = Command(self, command_data)
            self.commands.append(command)

        for group_data in self.data["groups"]:
            self.groups.append(CommandGroup(self, group_data))

    def __repr__(self):
        return self.__class__.__name__

class Command(ModelObject):
    usage = object_property("usage")
    output = object_property("output")
    examples = object_property("examples")

    def __init__(self, model, data, parent=None):
        super().__init__(model, data)

        self.parent = parent
        self.subcommands = list()

        self.options = list()
        self.options_by_name = dict()

        for data in self.merge_option_data():
            option = Option(self.model, self, data)

            self.options.append(option)
            self.options_by_name[option.name] = option

        self.errors = list()

        for error_data in self.data.get("errors", []):
            self.errors.append(Error(self, error_data))

        self.model.commands_by_id[self.id] = self

        for command_data in self.data.get("subcommands", []):
            command = Command(model, command_data, self)
            self.subcommands.append(command)

    def merge_option_data(self):
        inherited_option_data = dict()

        for pattern in self.data.get("inherit_options", []):
            for key, data in self.model.data["options"].items():
                if fnmatch.fnmatchcase(key, pattern):
                    inherited_option_data[data["name"]] = data
            # for else? XXX

        specific_option_data = {x["name"]: x for x in self.data.get("options", [])}

        # for name in inherited_options:
        #     if name not in standard_option_data:
        #         fail(f"Option '{name}' not in standard options")

        inherited_option_names = [x for x in inherited_option_data if x not in specific_option_data]
        option_names = list(specific_option_data.keys()) + inherited_option_names
        option_data = dict()

        for name in option_names:
            option_data[name] = dict(inherited_option_data.get(name, {}))
            option_data[name].update(specific_option_data.get(name, {}))

        return option_data.values()

    @property
    def ancestors(self):
        command = self.parent

        while command is not None:
            yield command
            command = command.parent

    @property
    def id(self):
        if self.parent:
            return self.parent.id + "/" + super().id
        else:
            return super().id

    @property
    def title(self):
        if self.subcommands:
            type = "commands"
        else:
            type = "command"

        if self.parent:
            return f"{capitalize(self.parent.name)} {self.name} {type}"
        else:
            return f"{capitalize(self.name)} {type}"

    @property
    def href(self):
        if self.subcommands:
            return f"{{{{site_prefix}}}}/commands/{self.id}/index.html"
        else:
            return f"{{{{site_prefix}}}}/commands/{self.id}.html"

    @property
    def resource(self):
        name = self.data.get("resource", capitalize(self.name.split(" ")[0]))
        resource = self.model.resource_model.resources_by_name.get(name)

        if resource is None and self.parent is not None:
            return self.parent.resource

        return resource

    @property
    def description(self):
        description = self.data.get("description")

        if description and self.resource and self.resource.description:
            description = description.replace("@resource_description@", self.resource.description.strip())

        return description

class CommandGroup(ModelObjectGroup):
    def __init__(self, model, data):
        super().__init__(model, data)

        self.commands = list()

        for command_id in self.data.get("commands", []):
            self.commands.append(self.model.commands_by_id[command_id])

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
    required = option_property("required", default=False)
    default = option_property("default")
    choices = option_property("choices")
    platforms = option_property("platforms", default=["Kubernetes", "Docker"])
    links = option_property("links", default=[])

    @property
    def property_(self):
        if "property" in self.data:
            assert self.object.resource is not None

            if self.data["property"] not in self.object.resource.spec_properties_by_name:
                fail("{}: Property '{}' not found in {}".format \
                     (self, self.data["property"], self.object.resource))

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
