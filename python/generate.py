from transom.planocommands import *

from common import Appender

import commands
import concepts
import resources

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

def generate_objects():
    resource_model.check()
    command_model.check()

    concepts.generate(concept_model)
    resources.generate(resource_model)
    commands.generate(command_model)

def generate_index():
    append = Appender()

    append("---")
    append("body_class: object index")
    append("---")
    append()
    append("# Refdog")
    append()
    append("## Concepts")
    append()

    for concept in concept_model.concepts:
        append(f"- [{concept.title}]({concept.href})")

    append()
    append("## Resources")
    append()

    for resource in resource_model.resources:
        append(f"- [{resource.title}]({resource.href})")

    append()
    append("## Commands")
    append()

    for command in command_model.commands:
        append(f"- [{command.title}]({command.href})")

    append()

    write("input/index.md", append.output())
