from transom.planocommands import *

import commands
import concepts
import resources

@command
def generate():
    concept_model = concepts.ConceptModel()
    resource_model = resources.ResourceModel(concept_model)
    command_model = commands.CommandModel(resource_model)

    concept_model.resource_model = resource_model
    resource_model.command_model = command_model
    command_model.concept_model = concept_model

    concepts.generate(concept_model)
    resources.generate(resource_model)
    commands.generate(command_model)

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
