option = """    - name: {name}
      default:
      required: n
      type: {type}
      description: |
        {description}"""

@command
def convert_help():
    for line in STDIN:
        line = line.strip()

        if not line:
            continue

        if not line.startswith("--"):
            continue

        elems = line.split()
        name = elems[0][2:]

        if elems[1] in ("int", "string", "strings", "duration"):
            type = elems[1]
            description = " ".join(elems[2:])
        else:
            type = bool
            description = " ".join(elems[1:])

        print(option.format(**locals()))

class Command:
    def arguments(self, include=None, exclude=None):
        arguments_by_name = dict()

        if "inherit_command_arguments" in self.data:
            from_command = self.data["inherit_arguments"]["from"]
            include = self.data["inherit_arguments"].get("include")
            exclude = self.data["inherit_arguments"].get("exclude")
            inherited = self.model.commands_by_name[from_command].arguments(include, exclude)

            arguments_by_name.update(((x.name, x) for x in inherited))

        for argument_data in self.data.get("arguments", []):
            name = argument_data["name"]

            if include is not None and name not in include:
                continue

            if exclude is not None and name in exclude:
                continue

            arguments_by_name[name] = Argument(self.model, self, argument_data)

        yield from arguments_by_name.values()
