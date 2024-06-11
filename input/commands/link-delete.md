---
body_class: command
links:
  - name: Link concept
    url: /concepts/link.html
  - name: Link resource
    url: /resources/link.html
  - name: link command
    url: /commands/link.html
---

# link delete command

<section>

Delete a link.

</section>

<section>

## Usage

~~~ shell
$ skupper link delete <name>
Waiting for deletion to complete...
Link "<name>" is deleted.
~~~

</section>

<section>

## Options

- <h4 id="name">name <span class="option-info">string, required</span></h4>

  The name of the link.

  
### Context options

- <h4 id="namespace">--namespace <span class="option-info">string</span></h4>

  Select the current namespace.

  
- <h4 id="context">--context <span class="option-info">string</span></h4>

  Select the current kubeconfig context.

  
- <h4 id="platform">--platform <span class="option-info">string</span></h4>

  Set the Skupper platform.

  | | |
  |-|-|
  | Choices | `kubernetes`, `docker`, `systemd` |
  
### Global options

- <h4 id="help">--help <span class="option-info"></span></h4>

  Display help and exit.

  
</section>
