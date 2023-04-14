from plano import *

import collections

@command
def generate():
    out = list()
    data = read_yaml("resources.yaml")

    out.append("- [Notes](#{})".format(get_fragment_id("notes")))
    out.append("- [Diagram](#{})".format(get_fragment_id("diagram")))

    for resource in data:
        resource_name = resource["name"]
        resource_title = capitalize(resource_name.replace("-", " "))
        resource_diagram = f"images/{resource_name}.svg"

        out.append(f"- [{resource_title}](#{resource_name})")

        if exists(resource_diagram):
            out.append("    - [Diagram](#{})".format(get_fragment_id("diagram")))

        out.append("    - [Examples](#{})".format(get_fragment_id("examples")))
        out.append("    - [Options](#{})".format(get_fragment_id("options")))

        for group in resource.get("groups", []):
            if group.get("hidden"):
                continue

            group_title = group["title"]
            group_id = group_title.lower().replace(" ", "-")
            group_id = get_fragment_id(group_id)

            out.append(f"    - [{group_title}](#{group_id})")

    toc = "\n".join(out)
    out.clear()

    for resource in data:
        resource_name = resource["name"]
        resource_title = capitalize(resource_name.replace("-", " "))
        resource_diagram = f"images/{resource_name}.svg"

        out.append("## {}".format(resource_name))
        out.append("")

        if exists(resource_diagram):
            out.append(f"### Diagram")
            out.append("")

            out.append(f"<img src=\"{resource_diagram}\" width=\"480\"/>")
            out.append("")

        if "yaml_example" in resource or "kubernetes_example" in resource or "cli_example" in resource:
            out.append(f"### Examples")
            out.append("")

            out.append("<table>")
            out.append("<tbody>")
            out.append("<tr><th>Skupper YAML</th></tr>")
            out.append("<tr><td><pre>{}</pre></td></tr>".format(nvl(resource.get("yaml_example"), "").strip(),
                                                                nvl(resource.get("kubernetes_example"), "").strip()))
            out.append("<tr><th>Skupper CLI</th></tr>")
            out.append("<tr><td><pre>{}</pre></td></tr>".format(nvl(resource.get("cli_example"), "").strip()))
            out.append("</tbody>")
            out.append("</table>")
            out.append("")

        out.append("<dl>")
        out.append("")

        out.append("### Options")
        out.append("")

        for option in resource.get("options", []):
            if option.get("hidden"):
                continue

            generate_option(out, option)

        out.append("")

        for group in resource.get("groups", []):
            if group.get("hidden"):
                continue

            group_title = group["title"]
            group_id = group_title.replace(" ", "-")

            out.append(f"### {group_title}")
            out.append("")

            out.append("<dl>")

            for option in group.get("options", []):
                if option.get("hidden"):
                    continue

                generate_option(out, option)

            out.append("</dl>")
            out.append("")

    resources = "\n".join(out)

    readme = read("README.md.in")
    readme = readme.replace("@toc@", toc)
    readme = readme.replace("@resources@", resources)

    write("README.md", readme)

fragment_ids = collections.defaultdict(int)

def get_fragment_id(fragment_id):
    count = fragment_ids[fragment_id]
    fragment_ids[fragment_id] += 1

    if count == 0:
        return fragment_id
    else:
        return f"{fragment_id}-{count}"

def generate_option(out, option):
    out.append("<dt><p>{}</p></dt>".format(option["name"]))
    out.append("<dd>")
    out.append("<p>{}</p>".format(option["description"]).strip())

    out.append("<div><b>Type:</b> {}</div>".format(capitalize(option["type"])))

    if "default" in option and option["default"] is not None:
        out.append("<div><b>Default:</b> {}</div>".format(option["default"]))

    if "choices" in option:
        out.append("<div><b>Choices:</b> {}</div>".format(", ".join(option["choices"])))

    out.append("</dd>")

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
