from transom.planocommands import *

from generate import generate_objects, generate_index

@command
def generate():
    generate_objects()
    generate_index()

@command
def generate_diagrams():
    for input_file in find("input/concepts/images", "*.d2"):
        output_file = input_file.removesuffix(".d2") + ".svg"

        with temp_file() as tmp:
            run(f"d2 --layout elk --theme 105 --pad 0 {input_file} {tmp}")
            move(tmp, output_file)

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
