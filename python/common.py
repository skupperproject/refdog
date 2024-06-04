from plano import *

def get_fragment_id(name):
    return name.lower().replace(" ", "-")

def generate_links(obj):
    links = ["[{}]({{{{site_prefix}}}}{})".format(x["name"], x["url"]) for x in obj.links]
    return "_See also:_ " + ", ".join(links)
