---
body_class: command
links:
  - name: Listener concept
    url: /concepts/listener.html
  - name: Listener resource
    url: /resources/listener.html
  - name: Listener command
    url: /commands/listener.html
---

# Listener status command

<section>

Show the status of listeners in the current site.

</section>

<section>

## Usage

~~~ shell
$ skupper listener status
NAME       ROUTING-KEY   HOST       PORT   MATCHING-CONNECTORS
backend    backend       backend    8080   1
database   database      database   5432   1
~~~

</section>
