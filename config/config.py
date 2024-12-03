import os

site_prefix = os.environ.get("SITE_PREFIX", "")

def path_nav(page):
    files = reversed(list(page.ancestors))
    links = [f"<a href=\"{site_prefix}{x.url}\">{x.title}</a>" for x in files]

    return f"<nav class=\"path-nav\">{''.join(links)}</nav>"

def directory_nav(page):
    def sort_fn(x):
        return x.title

    children = sorted(page.children, key=sort_fn)
    links = [f"<li><a href=\"{site_prefix}{x.url}\">{x.title}</a></li>" for x in children]

    return f"<nav class=\"directory-nav\"><ul>{''.join(links)}</ul></nav>"

def refdog_object_links(page):
    if not page.metadata.get("refdog_object_links"):
        return ""

    lines = list()

    lines.append("<section>")
    lines.append("<h4>See also</h4>")
    lines.append("<nav>")

    for link in page.metadata["refdog_object_links"]:
        title = link["title"]
        url = link["url"]

        if url.startswith("/"):
            url = site_prefix + url

        lines.append(f"<a href=\"{url}\">{title}</a>")

    lines.append("</nav>")
    lines.append("</section>")

    return "\n".join(lines)

def refdog_object_toc(page):
    if not page.metadata.get("refdog_object_toc"):
        return ""

    lines = list()

    lines.append("<section id=\"-toc\">")
    lines.append("  <h4>Contents</h4>")
    lines.append("  <nav>")

    for section in page.metadata["refdog_object_toc"]:
        lines.append(f"<a href=\"#{section['id']}\">{section['title']}</a>")

        children = section.get("children", [])

        if children:
            lines.append("<nav>")

            for child in children:
                lines.append(f"<a href=\"#{child['id']}\">{child['title']}</a>")

            lines.append("</nav>")

    lines.append("</nav>")
    lines.append("</section>")

    return "\n".join(lines)

def refdog_object_operations(page):
    if not page.metadata.get("refdog_object_has_attributes"):
        return ""

    lines = list()

    lines.append("<section>")
    lines.append("<h4>Page</h4>")
    lines.append("<nav>")
    lines.append("<a id=\"expand-all\">Expand all</a>")
    lines.append("<a id=\"collapse-all\">Collapse all</a>")
    lines.append("</nav>")
    lines.append("</section>")

    return "\n".join(lines)
