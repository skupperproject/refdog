---
body_class: command
links:
  - name: Site concept
    url: /concepts/site.html
  - name: Site resource
    url: /resources/site.html
---

# Site status command

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

<section>

## Options

</section>

<section>

## Context options

- <h3 id="namespace">--namespace <span class="argument-info">string</span></h3>

  Select the current namespace.

- <h3 id="context">--context <span class="argument-info">string</span></h3>

  Select the current kubeconfig context.

- <h3 id="platform">--platform <span class="argument-info">string</span></h3>

  Select the current Skupper platform.

</section>

<section>

## Global options

- <h3 id="help">--help <span class="argument-info">None</span></h3>

  Display help and exit.

</section>

<section>

## Errors

</section>

<section>

## Notes

What is services-in-network?  Is that the total number of
unique routing keys defined by connectors?  Or listeners?
Or listeners plus connectors (not the orphans), grouped by
routing key?

</section>
