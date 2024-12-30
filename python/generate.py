from common import *

import commands as _commands
import concepts as _concepts
import resources as _resources

concept_model = _concepts.ConceptModel()
resource_model = _resources.ResourceModel()
command_model = _commands.CommandModel()

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

    _concepts.generate(concept_model)
    _resources.generate(resource_model)
    _commands.generate(command_model)

def generate_index():
    append = Appender()

    append("---")
    append("body_class: object index")
    append("---")
    append()
    append("# Refdog")
    append()
    append("#### Concepts")
    append()

    append("- [Overview](concepts/overview.html)")
    append("- [Index](concepts/index.html)")
    append()

    # for concept in concept_model.concepts:
    #     append(f"- [{concept.title}]({concept.href})")

    append()
    append("#### Resources")
    append()
    append("- [Overview](resources/overview.html)")
    append("- [Index](resources/index.html)")
    append()

    # for resource in resource_model.resources:
    #     append(f"- [{resource.title}]({resource.href})")

    append()
    append("#### Commands")
    append()
    append("- [Overview](commands/overview.html)")
    append("- [Index](commands/index.html)")
    append()

    # for command in command_model.commands:
    #     append(f"- [{command.title}]({command.href})")

    append()

    append.write("input/index.md")
