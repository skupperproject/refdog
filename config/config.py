import os

site_prefix = os.environ.get("SITE_PREFIX", "")

def refdog_object_links(page):
    if "links" not in page.metadata:
        return ""

    lines = list()

    lines.append("<section>")
    lines.append("<h4>See also</h4>")
    lines.append("<nav>")

    for link in page.metadata["links"]:
        lines.append(f"<a href=\"{link['url']}\">{link['name']}</a>")

    lines.append("</nav>")
    lines.append("</section>")

    return "\n".join(lines)
