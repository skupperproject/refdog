from plano import *
from plano.github import *
from transom.planocommands import *

import collections
import commands
import resources

@command
def generate():
    resources.generate()
    commands.generate()

@command
def update_crds():
    url = "https://github.com/skupperproject/skupper/archive/refs/heads/v2.tar.gz"
    crd_dir = get_absolute_path("crds")

    with temp_file() as temp:
        http_get(url, output_file=temp)

        with working_dir(quiet=True):
            extract_archive(temp)

            extracted_dir = list_dir()[0]
            assert is_dir(extracted_dir)

            with working_dir(extracted_dir):
                copy("api/types/crds", crd_dir, inside=False)
