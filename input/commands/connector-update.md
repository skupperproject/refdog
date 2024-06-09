---
body_class: command
links:
  - name: Connector concept
    url: /concepts/connector.html
  - name: Connector resource
    url: /resources/connector.html
  - name: Listener update command
    url: /commands/listener-update.html
---

# Connector update command

<section>

Update a connector.

</section>

<section>

## Usage

~~~ shell
$ skupper connector update <name> [options]
Waiting for update to complete...
Connector "<name>" is updated.
~~~

</section>

<section>

## Examples

~~~
# Change the workload and port
skupper connector update database --workload deployment/mysql --port 3306

# Change the routing key
skupper connector update backend --routing-key be2

# Produce YAML output
skupper connector update frontend --port 9090 --output yaml
~~~

</section>

<section>

## Options

</section>

<section>

## Errors

</section>
