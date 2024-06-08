---
body_class: command
links:
  - name: Connector concept
    url: /concepts/connector.html
  - name: Connector resource
    url: /resources/connector.html
  - name: Listener delete command
    url: /commands/listener-delete.html
---

# Connector delete command

<section>

Delete a connector.

</section>

<section>

## Usage

~~~ shell
$ skupper connector delete <name>
Waiting for deletion to complete...
Connector "<name>" is deleted.
~~~

</section>

<section>

## Options

- <h4 id="name">name <span class="argument-info">string, required</span></h3>

  The name of the connector resource.

### Context options

- <h4 id="namespace">--namespace <span class="argument-info">string</span></h3>

  Select the current namespace.

- <h4 id="context">--context <span class="argument-info">string</span></h3>

  Select the current kubeconfig context.

- <h4 id="platform">--platform <span class="argument-info">string</span></h3>

  Select the current Skupper platform.

### Global options

- <h4 id="help">--help <span class="argument-info">None</span></h3>

  Display help and exit.

</section>

<section>

## Errors

</section>
