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

A listener binds a connection endpoint in the local site to
target workloads in remote sites.

Each site can have multiple listener definitions.

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

## Arguments

- <h3 id="name">name <span class="argument-info">string, required</span></h3>

  The name of the listener resource.

</section>

<section>

## Errors

</section>
