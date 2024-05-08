from plano import *
from plano.github import *

import collections
import commands
import resources

@command
def generate():
    commands.generate()
    resources.generate()

@command
def render():
    generate()

    # write("concepts.html", convert_github_markdown(read("concepts.md")))
    write("commands.html", convert_github_markdown(read("commands.md")))
    # write("resources.html", convert_github_markdown(read("resources.md")))

    # print(f"file:{get_real_path('concepts.html')}")
    print(f"file:{get_real_path('commands.html')}")
    # print(f"file:{get_real_path('resources.html')}")

@command
def clean():
    remove(find(".", "__pycache__"))
