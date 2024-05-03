@command
def generate_():
    lines = list()

    def append(line=""):
        lines.append(line)

    data = read_yaml("entities.yaml")
    data = transform_data(data)

    # append("- [Notes](#{})".format(get_fragment_id("notes")))
    append("- [Overview](#{})".format(get_fragment_id("overview")))

    for entity_name, entity in data.items():
        if entity.get("hidden"):
            continue

        entity_title = entity["title"]

        append(f"- [{entity_title}](#{entity_name})")

    toc = "\n".join(lines)
    lines.clear()

    for entity_name, entity in data.items():
        if entity.get("hidden"):
            continue

        entity_title = entity["title"]
        entity_diagram = f"images/{entity_name}.svg"
        entity_description = entity.get("description", "").rstrip()

        append("## {}".format(entity_title))
        append()

        if entity_description:
            append(entity_description)
            append()

        resource_name = entity["resource-name"]

        if not resource_name.startswith("*"):
            resource_name = "`{}`".format(resource_name)

        append("_Resource kind_: `{}`\\".format(entity["resource-kind"]))
        append(f"_Resource name_: {resource_name}\\")
        append("_Type label_: `{}`\\".format(entity["type-label"]))

        # Chomp off the last backslash
        lines[-1] = lines[-1].removesuffix("\\")

        append()

        if exists(entity_diagram):
            append(f"<img src=\"{entity_diagram}\" height=\"180\"/>")
            append()

        if "examples" in entity:
            if "yaml" in entity["examples"]:
                append("#### YAML example")
                append()
                append("~~~ yaml")
                append(entity["examples"]["yaml"])
                append("~~~")
                append()

            if "cli" in entity["examples"]:
                append("#### CLI example")
                append()
                append("~~~ sh")
                append(entity["examples"]["cli"])
                append("~~~")
                append()

        for group_name, group in entity.get("groups", {}).items():
            if group.get("hidden"):
                continue

            group_title = group.get("title", "Settings")
            group_description = group.get("description", "").rstrip()
            group_id = make_entity_id(group_title)

            append(f"### {group_title}")
            append()

            if group_description:
                append(group_description)
                append()

            for setting_name, setting in group.get("settings", {}).items():
                if setting.get("hidden"):
                    continue

                generate_setting(lines, setting_name, setting)

    entities = "\n".join(lines)

    readme = read("README.md.in")
    readme = readme.replace("@toc@", toc)
    readme = readme.replace("@entities@", entities)

    write("README.md", readme)

def transform_data(data):
    for entity_name, entity in data.items():
        if "title" not in entity:
            entity["title"] = make_entity_title(entity_name)

        if "extends" in entity:
            base_name = entity["extends"]

            for candidate_name, candidate in data.items():
                if candidate_name == base_name:
                    base_entity = candidate
                    break
            else:
                raise Exception(f"I can't find base entity '{base_name}'")

            if "groups" not in base_entity:
                base_entity["groups"] = dict()

            if "groups" not in entity:
                entity["groups"] = dict()

            group_names = list(base_entity["groups"].keys())

            for group_name in entity["groups"]:
                if group_name not in group_names:
                    group_names.append(group_name)

            for group_name in group_names:
                try:
                    base_group = base_entity["groups"][group_name]
                except KeyError:
                    base_entity["groups"][group_name] = base_group = dict()

                try:
                    derived_group = entity["groups"][group_name]
                except KeyError:
                    entity["groups"][group_name] = derived_group = dict()

                settings = dict()

                if "settings" in base_group:
                    for setting_name, setting in base_group["settings"].items():
                        settings[setting_name] = setting

                if "settings" in derived_group:
                    for setting_name, setting in derived_group["settings"].items():
                        settings[setting_name] = setting

                derived_group["settings"] = settings

    return data

def make_entity_title(name):
    title = name.replace("-", " ")
    return title[0].upper() + title[1:]

def make_entity_id(title):
    return title.lower().replace(" ", "-")

fragment_ids = collections.defaultdict(int)

def get_fragment_id(fragment_id):
    count = fragment_ids[fragment_id]
    fragment_ids[fragment_id] += 1

    if count == 0:
        return fragment_id
    else:
        return f"{fragment_id}-{count}"

def generate_setting(lines, name, setting):
    def append(line=""):
        lines.append(line)

    description = setting.get("description", "").strip()
    type_ = capitalize(setting.get("type", ""))

    # XXX Minor hack
    if type_ == "Boolean" and "default" not in setting:
        setting["default"] = False

    default = str(setting.get("default", "")).strip()
    choices = setting.get("choices")

    append(f"#### `{name}`")
    append()

    if "description" in setting:
        # append(f"  {description}".replace("\n", "\n  "))
        append(description)

    append()

    required = "No"

    if "required" in setting:
        required = "Yes" if setting["required"] else required

    append(f"_Required_: {required}\\")

    if "type" in setting:
        append(f"_Type_: {type_}\\")

    if "default" in setting:
        if type_ in ("String", "Duration") and default != "*Generated*" and " " not in default:
            default = f"`{default}`"

        append(f"_Default_: {default}\\")
    elif "choices" in setting:
        append(f"_Default_: `{choices[0]}`\\")

    if "choices" in setting:
        choices = ", ".join([f"`{x}`" for x in choices])
        append(f"_Choices_: {choices}\\")

    # Chomp off the last backslash
    lines[-1] = lines[-1].removesuffix("\\")

    append()

render_template = """
<html>
  <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.1.0/github-markdown.min.css"
          integrity="sha512-KUoB3bZ1XRBYj1QcH4BHCQjurAZnCO3WdrswyLDtp7BMwCw7dPZngSLqILf68SGgvnWHTD5pPaYrXi6wiRJ65g=="
          crossorigin="anonymous" referrerpolicy="no-referrer"/>
    <style>
        .markdown-body {
            box-sizing: border-box;
            min-width: 200px;
            max-width: 980px;
            margin: 0 auto;
            padding: 45px;
        }
        @media (max-width: 767px) {
           .markdown-body {
               padding: 15px;
           }
        }
    </style>
  </head>
  <body>
    <article class="markdown-body">
@content@
    </article>
  </body>
</html>
""".strip()

@command
def render():
    """
    Render README.html from the data in skewer.yaml
    """
    generate()

    html = convert_github_markdown(read("README.md"))
    write("README.html", html)

    print(f"file:{get_real_path('reference.html')}")
