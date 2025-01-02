from resources import *

def generate(model):
    notice("Generating commands")

    make_dir("input/commands")

    append = StringBuilder()

    append("---")
    append("refdog_links:")
    append("  - title: Skupper concepts")
    append("    url: /concepts/index.html")
    append("  - title: Skupper resources")
    append("    url: /resources/index.html")
    append("---")
    append()
    append("# Skupper commands")
    append()
    append("[Overview](overview.html)")
    append()

    for group in model.groups:
        append(f"#### {group.title}")
        append()

        for command in group.commands:
            append("<table class=\"objects\">")

            if command.subcommands:
                summary = f"Overview of {command.name} commands"

                append(f"<tr><th><a href=\"{command.href}\">{command.title}</a></th><td>{summary}</td></tr>")

                for sc in command.subcommands:
                    append(f"<tr><th><a href=\"{sc.href}\">{sc.title}</a></th><td>{sc.summary}</td></tr>")
            else:
                append(f"<tr><th><a href=\"{command.href}\">{command.title}</a></th><td>{command.summary}</td></tr>")

            append("</table>")
            append()

        append()

    append.write("input/commands/index.md")

    for command in model.commands:
        generate_command(command)

        for subcommand in command.subcommands:
            generate_command(subcommand)

def generate_command(command):
    notice(f"Generating {command}")

    append = StringBuilder()

    append("---")
    append(generate_object_metadata(command))
    append("---")
    append()
    append(f"# {command.title_with_type}")
    append()
    append("~~~ shell")
    append(f"{generate_usage(command)}")
    append("~~~")
    append()

    if command.description and not command.subcommands:
        append(command.description.strip())
        append()

    append(generate_command_fields(command))
    append()

    if command.output:
        append("## Output")
        append()
        append("~~~ console")
        append(command.output.strip())
        append("~~~")
        append()

    if command.subcommands:
        append("## Subcommands")
        append()
        append("<table class=\"objects\">")

        for sc in command.subcommands:
            append(f"<tr><th><a href=\"{sc.href}\">{sc.title}</a></th><td>{sc.summary}</td></tr>")

        append("</table>")
        append()
    else:
        if command.examples:
            append("## Examples")
            append()
            append("~~~ console")
            append(command.examples.strip())
            append("~~~")
            append()

        if command.options:
            append("## Primary options")
            append()

            for group in ("positional", "required", "frequently-used", None, "advanced"):
                for option in command.options:
                    if option.group == group:
                        generate_option(option, append)

            append("## Global options")
            append()

            for option in command.options:
                if option.group == "global":
                    generate_option(option, append)

        if command.errors:
            append("## Errors")
            append()

            for error in command.errors:
                generate_error(error, append)

    append(command.input_file)

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
    option_key = option.syntax_name
    type_info = option.type

    if not option.positional and option.type != "boolean":
        if option.placeholder:
            type_info = f"&lt;{option.placeholder}&gt;"
        else:
            type_info = f"&lt;{option.type}&gt;"

    if option.short_option:
        type_info = f"(-{option.short_option}) {type_info}"

    if option.group:
        if option.group == "positional":
            if option.required:
                flags.append("required")
            else:
                flags.append("optional")
        else:
            flags.append(option.group.replace("-", " "))

    if option.group not in ("positional", "required", "frequently-used"):
        classes.append("collapsed")

    append(f"<div class=\"{' '.join(classes)}\">")
    append(f"<div class=\"attribute-heading\">")
    append(f"<h3 id=\"{option.id}\">{option_key}</h3>")
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
    append("</div>")
    append("</div>")
    append()

def generate_error(error, append):
    append(f"- **{error.message}**")
    append()

    if error.description:
        append(f"  <p>{error.description.strip()}</p>")
        append()

class CommandModel:
    def __init__(self):
        debug(f"Loading {self}")

        self.option_data = read_yaml("config/commands/options.yaml")

        self.commands = list()
        self.commands_by_id = dict()
        self.groups = list()

        for yaml_file in list_dir("config/commands"):
            if yaml_file in ("index.yaml", "options.yaml"):
                continue

            command_data = read_yaml(join("config/commands", yaml_file))
            command = Command(self, command_data)

            self.commands.append(command)

        index_data = read_yaml("config/commands/index.yaml")

        for group_data in index_data["groups"]:
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
            command = Command(model, command_data, self)
            self.subcommands.append(command)

    def __repr__(self):
        if self.parent:
            return f"{self.__class__.__name__} '{self.parent.name} {self.name}'"
        else:
            return super().__repr__()

    def merge_option_data(self):
        model_options = self.model.option_data
        included_keys = list()

        for pattern in self.data.get("include_options", []):
            for key in model_options:
                if string_matches_glob(key, pattern):
                    included_keys.append(key)

        for pattern in self.data.get("exclude_options", []):
            for key in included_keys:
                if string_matches_glob(key, pattern):
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

        return super().id

    @property
    def title(self):
        if self.parent:
            return f"{capitalize(self.parent.name)} {self.name}"

        return f"{capitalize(self.name)}"

    @property
    def input_file(self):
        if self.subcommands:
            return f"input/commands/{self.id}/index.md"

        return super().input_file

    @property
    def href(self):
        if self.subcommands:
            return f"{{{{site_prefix}}}}/commands/{self.id}/index.html"

        return super().href

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
            try:
                self.commands.append(self.model.commands_by_id[command_id])
            except KeyError:
                fail(f"{self}: Command '{command_id}' not found")

def option_property(name, default=None):
    def get(obj):
        default_ = getattr(obj.property_, name, None) if obj.property_ else default
        return obj.data.get(name, default_)

    return property(get)

class Option(ModelObjectAttribute):
    type = option_property("type")
    required = option_property("required", default=False)
    placeholder = option_property("placeholder")
    short_option = option_property("short_option")
    default = option_property("default")
    choices = option_property("choices")

    @property
    def id(self):
        return f"option-{super().id}"

    @property
    def syntax_name(self):
        if self.positional:
            if self.required:
                return f"&lt;{self.name}&gt;"
            else:
                return f"[{self.name}]"
        else:
            return f"--{self.name}"

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

    @property
    def links(self):
        default = self.property_.links if self.property_ else []
        return self.data.get("links", default)

    def gather_links(self):
        links = list()

        if self.property_:
            for concept in self.property_.related_concepts:
                links.append((concept.title, concept.href))

        links.extend(super().gather_links())

        return links

class Error:
    message = object_property("message", required=True)
    description = object_property("description")
    notes = object_property("notes")

    def __init__(self, model, data):
        self.model = model
        self.data = data

    def __repr__(self):
        return f"{self.__class__.__name__} '{self.message}'"
