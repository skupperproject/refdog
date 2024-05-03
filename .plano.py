from plano import *
from plano.github import *

import collections
import commands
import resources

@command
def generate():
    resources.generate()
    commands.generate()

    write("resources.html", convert_github_markdown(read("resources.md")))
    write("commands.html", convert_github_markdown(read("commands.md")))

    print(f"file:{get_real_path('resources.html')}")
    print(f"file:{get_real_path('commands.html')}")

@command
def clean():
    remove(find(".", "__pycache__"))
