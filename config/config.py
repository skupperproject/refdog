import os

site_prefix = os.environ.get("SITE_PREFIX", "")

def path_nav(page):
    files = reversed(list(page.ancestors))
    links = [f"<a href=\"{site_prefix}{x.url}\">{x.title}</a>" for x in files]

    return f"<nav class=\"path-nav\">{''.join(links)}</nav>"

def refdog_object_links(page):
    if "links" not in page.metadata:
        return ""

    lines = list()

    lines.append("<section>")
    lines.append("<h4>See also</h4>")
    lines.append("<nav>")

    for link in page.metadata["links"]:
        lines.append(f"<a href=\"{site_prefix}{link['url']}\">{link['name']}</a>")

    lines.append("</nav>")
    lines.append("</section>")

    return "\n".join(lines)
