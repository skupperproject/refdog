---
body_class: command
links:
  - name: Listener concept
    url: /concepts/listener.html
  - name: Listener resource
    url: /resources/listener.html
  - name: Connector create command
    url: /commands/connector-create.html
---

# Listener create command

<section>

Create a listener.

</section>

<section>

## Usage

~~~ shell
$ skupper listener create <name> <port> [options]
Waiting for status...
Listener "<name>" is ready.
~~~

</section>

<section>

## Examples

~~~
# Create a listener for a database
skupper listener create database 5432

# Set the routing key and host explicitly
skupper listener create backend 8080 --routing-key be1 --host apiserver

# Produce YAML output
skupper listener create frontend 8080 --output yaml
~~~

</section>

<section>

## Options

</section>

<section>

## Errors

</section>
