---
body_class: command
links:
  - name: Listener concept
    url: /concepts/listener.html
  - name: Listener resource
    url: /resources/listener.html
  - name: Connector delete command
    url: /commands/connector-delete.html
---

# Listener delete command

<section>

Delete a listener.

</section>

<section>

## Usage

~~~ shell
$ skupper listener delete <name>
Waiting for deletion to complete...
Listener "<name>" is deleted.
~~~

</section>

<section>

## Options

- <h4 id="name">name <span class="argument-info">string, required</span></h4>

  The name of the listener resource.

### Context options

- <h4 id="namespace">--namespace <span class="argument-info">string</span></h4>

  Select the current namespace.

- <h4 id="context">--context <span class="argument-info">string</span></h4>

  Select the current kubeconfig context.

- <h4 id="platform">--platform <span class="argument-info">string</span></h4>

  Select the current Skupper platform.

### Global options

- <h4 id="help">--help <span class="argument-info">None</span></h4>

  Display help and exit.

</section>

<section>

## Errors

</section>
