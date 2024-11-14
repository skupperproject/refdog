from transom.planocommands import *

import commands
import concepts
import resources

@command
def generate():
    concept_model = concepts.ConceptModel()
    resource_model = resources.ResourceModel()
    command_model = commands.CommandModel()

    concept_model.resource_model = resource_model
    concept_model.command_model = command_model
    concept_model.concept_model = concept_model

    resource_model.concept_model = concept_model
    resource_model.command_model = command_model
    resource_model.resource_model = resource_model

    command_model.concept_model = concept_model
    command_model.resource_model = resource_model
    command_model.command_model = command_model

    resource_model.check()
    command_model.check()

    concepts.generate(concept_model)
    resources.generate(resource_model)
    commands.generate(command_model)

@command
def generate_diagrams():
    for input_file in find("input/concepts/images", "*.d2"):
        output_file = input_file.removesuffix(".d2") + ".svg"

        run(f"d2 --layout elk --theme 105 --pad 0 {input_file} {output_file}")

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
