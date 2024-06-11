---
body_class: command
links:
  - name: Site concept
    url: /concepts/site.html
  - name: Site resource
    url: /resources/site.html
  - name: site command
    url: /commands/site.html
---

# site status command

<section>

Show the current status of a site.

</section>

<section>

## Usage

~~~ shell
$ skupper site status
NAME   STATUS   SITES-IN-NETWORK   SERVICES-IN-NETWORK
west   Ready    1                  0
~~~

</section>

<section class="notes">

## Notes

What is services-in-network?  Is that the total number of
unique routing keys defined by connectors?  Or listeners?
Or listeners plus connectors (not the orphans), grouped by
routing key?

</section>
