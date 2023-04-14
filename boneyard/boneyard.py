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
