---
body_class: command
links:
  - name: Connector concept
    url: /concepts/connector.html
  - name: Connector resource
    url: /resources/connector.html
  - name: connector command
    url: /commands/connector.html
---

# connector status command

<section>

Display the status of connectors in the current site.

</section>

<section>

## Usage

~~~ shell
$ skupper connector status
NAME       ROUTING-KEY   SELECTOR         HOST   PORT   MATCHING-LISTENERS
backend    backend       app=backend      -      8080   1
database   database      app=postgresql   -      5432   1
~~~

</section>
