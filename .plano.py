from plano import *

import collections

@command
def generate():
    lines = list()

    def append(line=""):
        lines.append(line)

    data = read_yaml("resources.yaml")
    data = transform_data(data)

    append("- [Notes](#{})".format(get_fragment_id("notes")))
    append("- [Overview](#{})".format(get_fragment_id("overview")))

    for resource in data:
        if resource.get("hidden"):
            continue

        resource_name = resource["name"]
        resource_title = capitalize(resource_name.replace("-", " "))
        resource_diagram = f"images/{resource_name}.svg"

        append(f"- [{resource_title}](#{resource_name})")
        append("    - [Examples](#{})".format(get_fragment_id("examples")))
        append("    - [Options](#{})".format(get_fragment_id("options")))

        for group in resource.get("groups", []):
            if group.get("hidden"):
                continue

            group_title = group["title"]
            group_id = group_title.lower().replace(" ", "-")
            group_id = get_fragment_id(group_id)

            append(f"    - [{group_title}](#{group_id})")

    toc = "\n".join(lines)
    lines.clear()

    for resource in data:
        if resource.get("hidden"):
            continue

        resource_name = resource["name"]
        resource_title = capitalize(resource_name.replace("-", " "))
        resource_diagram = f"images/{resource_name}.svg"

        append("## {}".format(resource_name))
        append()

        if exists(resource_diagram):
            append(f"#### Diagram")
            append()

            append(f"<img src=\"{resource_diagram}\" height=\"120\"/>")
            append()

        if "examples" in resource:
            append("### Examples")

        append("<dl>")
        append()

        append("### Options")
        append()

        for option in resource.get("options", []):
            if option.get("hidden"):
                continue

            generate_option(lines, option)

        append()

        for group in resource.get("groups", []):
            if group.get("hidden"):
                continue

            group_title = group["title"]
            group_id = group_title.replace(" ", "-")

            append(f"### {group_title}")
            append()

            append("<dl>")

            for option in group.get("options", []):
                if option.get("hidden"):
                    continue

                generate_option(lines, option)

            append("</dl>")
            append()

    resources = "\n".join(lines)

    readme = read("README.md.in")
    readme = readme.replace("@toc@", toc)
    readme = readme.replace("@resources@", resources)

    write("README.md", readme)

def transform_data(data):
    for resource in data:
        if "extends" in resource:
            base_name = resource["extends"]

            for candidate in data:
                if candidate["name"] == base_name:
                    base = candidate
                    break
            else:
                raise Exception()

            if "options" not in resource:
                resource["options"] = list()

            if "groups" not in resource:
                resource["groups"] = list()

            # Could use a nicer merge here

            if "options" in base:
                resource["options"][0:0] = base["options"]

            if "groups" in base:
                resource["groups"][0:0] = base["groups"]

    return data

fragment_ids = collections.defaultdict(int)

def get_fragment_id(fragment_id):
    count = fragment_ids[fragment_id]
    fragment_ids[fragment_id] += 1

    if count == 0:
        return fragment_id
    else:
        return f"{fragment_id}-{count}"

def generate_option(lines, option):
    lines.append("<dt><p>{}</p></dt>".format(option["name"]))
    lines.append("<dd>")

    if "description" in option:
        lines.append("<p>{}</p>".format(option["description"]).strip())

    if "type" in option:
        lines.append("<div><b>Type:</b> {}</div>".format(capitalize(option["type"])))

    if "default" in option and option["default"] is not None:
        lines.append("<div><b>Default:</b> {}</div>".format(option["default"]))

    if "choices" in option:
        lines.append("<div><b>Choices:</b> {}</div>".format(", ".join(option["choices"])))

    lines.append("</dd>")

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

    markdown = read("README.md")
    data = {"text": markdown}
    json = emit_json(data)
    content = http_post("https://api.github.com/markdown", json, content_type="application/json")
    html = render_template.replace("@content@", content)

    write("README.html", html)

    print(f"file:{get_real_path('README.html')}")

@command
def clean():
    remove("README.html")
    remove(find(".", "__pycache__"))
