import os

site_prefix = os.environ.get("SITE_PREFIX", "")

def path_nav(page):
    files = reversed(list(page.ancestors))
    links = [f"<a href=\"{site_prefix}{x.url}\">{x.title}</a>" for x in files]

    return f"<nav class=\"path-nav\">{''.join(links)}</nav>"
