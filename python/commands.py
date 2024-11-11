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
    append("<a href=\"overview.html\">Overview</a>")
    append()


    for group in model.groups:
        append(f"#### {group.name}")
        append()

        for command in group.commands:
            append("<table class=\"objects\">")

            if command.subcommands:
                title = command.title.removesuffix(" command")
                description = f"Overview of {command.name} commands"

                append(f"<tr><th><a href=\"{command.href}\">{title}</a></th><td>{description}</td></tr>")

                for subcommand in command.subcommands:
                    title = subcommand.title.removesuffix(" command")
                    description = nvl(subcommand.description, "").replace("\n", " ")
                    description = description.split(".")[0]
                    description = mistune.html(description)

                    append(f"<tr><th><a href=\"{subcommand.href}\">{title}</a></th><td>{description}</td></tr>")
            else:
                title = command.title.removesuffix(" command")
                description = nvl(command.description, "").replace("\n", " ")
                description = description.split(".")[0]
                description = mistune.html(description)

                append(f"<tr><th><a href=\"{command.href}\">{title}</a></th><td>{description}</td></tr>")

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

    if command.description and not command.subcommands:
        append(command.description.strip())
        append()

    append(generate_command_fields(command))
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
        append("## Commands")
        append()
        append("<table class=\"objects\">")

        for subcommand in command.subcommands:
            title = subcommand.title.removesuffix(" command")
            description = nvl(subcommand.description, "").replace("\n", " ")
            description = description.split(".")[0]
            description = mistune.html(description)

            append(f"<tr><th><a href=\"{subcommand.name}.html\">{title}</a></th><td>{description}</td></tr>")

        append("</table>")
        append()
        append("</section>")
        append()
    else:
        if command.examples:
            append("<section>")
            append()
            append("## Examples")
            append()
            append("~~~ console")
            append(command.examples.strip())
            append("~~~")
            append()
            append("</section>")
            append()

        if command.options:
            append("<section class=\"attributes\">")
            append()
            append("## Options")
            append()

            for group in ("positional", "required", "frequently-used", None, "advanced", "global"):
                for option in command.options:
                    if option.group == group:
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
        parts.append("[command]")

    for option in command.options:
        if option.positional:
            if option.required:
                parts.append(f"<{option.name}>")
            else:
                parts.append(f"[{option.name}]")

    parts.append("[options]")

    return " ".join(parts)

def generate_command_fields(command):
    rows = list()

    rows.append(f"<tr><th>Platforms</th><td>{', '.join(command.platforms)}</td>")

    if command.wait:
        rows.append(f"<tr><th>Waits for</th><td>{command.wait}</td>")

    return f"<table class=\"fields\">{''.join(rows)}</table>"

def generate_option(option, append):
    debug(f"Generating {option}")

    classes = ["attribute"]
    flags = list()
    prefix = ""
    id_ = f"option-{get_fragment_id(option.name)}"
    option_key = option.name
    type_info = option.type

    if option.positional:
        if option.required:
            option_key = f"&lt;{option_key}&gt;"
        else:
            option_key = f"[{option_key}]"
    else:
        option_key = f"--{option_key}"

        if option.type != "boolean":
            if option.placeholder:
                type_info = f"&lt;{option.placeholder}&gt;"
            else:
                type_info = f"&lt;{option.type}&gt;"

        if option.short_option:
            type_info = f"(-{option.short_option}) {type_info}"

    # if option.format:
    #     type_info += f" ({option.format})"

    if option.group:
        if option.group == "positional":
            if option.required:
                flags.append("required")
            else:
                flags.append("optional")
        else:
            flags.append(option.group.replace("-", " "))

    if option.group not in ("positional", "required", "frequently-used"):
        classes.append("folded")

    append(f"<div class=\"{' '.join(classes)}\">")
    append(f"<div class=\"attribute-heading\">")
    append(f"<h3 id=\"{id_}\">{option_key}</h3>")
    append(f"<div class=\"attribute-type-info\">{type_info}</div>")

    if flags:
        append(f"<div class=\"attribute-flags\">{', '.join(flags)}</div>")

    append("</div>")
    append("<div class=\"attribute-body\">")
    append()

    if option.description:
        append(option.description.strip())
        append()

    append(generate_attribute_fields(option))
    append()

    if option.notes:
        append("<section class=\"notes\">")
        append()
        append(option.notes.strip())
        append()
        append("</section>")
        append()

    append("</div>")
    append("</div>")
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

    def check(self):
        for command in self.commands:
            for option in command.options:
                if not option.name:
                    fail(f"{command}: {option} has no name")

                if not option.type:
                    fail(f"{command}: {option} has no type")

            for subcommand in command.subcommands:
                for option in subcommand.options:
                    if not option.name:
                        fail(f"{command}: {subcommand}: {option} has no name")

                    if not option.type:
                        fail(f"{command}: {subcommand}: {option} has no type")

class Command(ModelObject):
    usage = object_property("usage")
    platforms = object_property("platforms", default=["Kubernetes", "Docker", "Podman", "Linux"])
    output = object_property("output")
    examples = object_property("examples")
    wait = object_property("wait")

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
            command = Subcommand(model, command_data, self)
            self.subcommands.append(command)

    def merge_option_data(self):
        model_options = self.model.data.get("options", {})
        included_keys = list()

        for pattern in self.data.get("include_options", []):
            for key in model_options:
                if fnmatch.fnmatchcase(key, pattern):
                    included_keys.append(key)

        for pattern in self.data.get("exclude_options", []):
            for key in included_keys:
                if fnmatch.fnmatchcase(key, pattern):
                    included_keys.remove(key)

        included_options = {model_options[x]["name"]: model_options[x] for x in included_keys}
        specific_options = {x["name"]: x for x in self.data.get("options", [])}

        included_names = [x for x in included_options if x not in specific_options]
        merged_names = list(specific_options.keys()) + included_names
        merged_options = list()

        for name in merged_names:
            included_data = included_options.get(name, {})
            specific_data = specific_options.get(name, {})

            merged_data = dict(included_data)
            merged_data.update(specific_data)

            if "description" in included_data and "description" in specific_data:
                included_description = included_data["description"]
                specific_description = specific_data["description"]

                merged_data["description"] = specific_description.replace("@description@", included_description)

            merged_options.append(merged_data)

        return merged_options

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
        if self.parent:
            return f"{capitalize(self.parent.name)} {self.name} command"
        else:
            return f"{capitalize(self.name)} command"

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

class Subcommand(Command):
    pass

class CommandGroup(ModelObjectGroup):
    def __init__(self, model, data):
        super().__init__(model, data)

        self.commands = list()

        for command_id in self.data.get("commands", []):
            self.commands.append(self.model.commands_by_id[command_id])

def option_property(name, default=None):
    def get(obj):
        default_ = getattr(obj.property_, name, None) if obj.property_ else default
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
    required = option_property("required", default=False)
    placeholder = option_property("placeholder")
    short_option = option_property("short_option")
    default = option_property("default")
    choices = option_property("choices")

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
    def group(self):
        if self.positional:
            return "positional"

        if self.required:
            return "required"

        default = self.property_.group if self.property_ else None
        return self.data.get("group", default)

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
