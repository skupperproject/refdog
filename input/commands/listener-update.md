---
body_class: command
links:
  - name: Listener concept
    url: /concepts/listener.html
  - name: Listener resource
    url: /resources/listener.html
  - name: Connector update command
    url: /commands/connector-update.html
---

# Listener update command

<section>

Update a listener.

</section>

<section>

## Usage

~~~ shell
$ skupper listener update <name> [options]
Waiting for update to complete...
Listener "<name>" is updated.
~~~

</section>

<section>

## Examples

~~~
# Change the host and port
skupper listener update database --host mysql --port 3306

# Change the routing key
skupper listener update backend --routing-key be2

# Produce YAML output
skupper listener update frontend --port 9090 --output yaml
~~~

</section>

<section>

## Options

</section>

<section>

## Errors

</section>
