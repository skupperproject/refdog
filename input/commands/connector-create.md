---
body_class: command
links:
  - name: Connector concept
    url: /concepts/connector.html
  - name: Connector resource
    url: /resources/connector.html
  - name: Listener create command
    url: /commands/listener-create.html
---

# Connector create command

<section>

Create a connector.

</section>

<section>

## Usage

~~~ shell
$ skupper connector create <name> <port> [options]
Waiting for status...
Connector "<name>" is ready.
~~~

</section>

<section>

## Examples

~~~
# Create a connector for a database
skupper connector create database 5432

# Set the routing key and workload explicitly
skupper connector create backend 8080 --routing-key be1 --workload deployment/backend

# Produce YAML output
skupper connector create backend 8080 --output yaml
~~~

</section>

<section>

## Options

</section>

<section>

## Errors

</section>
