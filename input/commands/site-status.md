---
body_class: command
links:
  - name: Site resource
    url: /resources/site.html
  - name: Site command
    url: /commands/site.html
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

### Context options

- <h4 id="namespace">--namespace <span class="option-info">string</span></h4>

  Select the current namespace.

- <h4 id="context">--context <span class="option-info">string</span></h4>

  Select the current kubeconfig context.

- <h4 id="platform">--platform <span class="option-info">string</span></h4>

  Select the current Skupper platform.

### Global options

- <h4 id="help">--help <span class="option-info">None</span></h4>

  Display help and exit.

</section>

<section>

## Errors

</section>

<section class="notes">

## Notes

What is services-in-network?  Is that the total number of
unique routing keys defined by connectors?  Or listeners?
Or listeners plus connectors (not the orphans), grouped by
routing key?

</section>
