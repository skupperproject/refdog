---
body_class: object command
refdog_object_has_attributes: true
refdog_object_links:
- title: Connector concept
  url: /concepts/connector.html
- title: Connector resource
  url: /resources/connector.html
- title: Listener command
  url: /commands/listener/index.html
refdog_object_toc:
- id: ''
  title: Overview
- id: usage
  title: Usage
- id: subcommands
  title: Subcommands
- children:
  - id: option-platform
    title: --platform
  - id: option-help
    title: --help
  id: options
  title: Options
---

# Connector command

<section>

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</section>

<section>

## Usage

~~~ shell
skupper connector [command] [options]
~~~

</section>

<section>

## Subcommands

<table class="objects">
<tr><th><a href="create.html">Connector create</a></th><td><p>Create a connector</p>
</td></tr>
<tr><th><a href="update.html">Connector update</a></th><td><p>Update a connector</p>
</td></tr>
<tr><th><a href="delete.html">Connector delete</a></th><td><p>Delete a connector</p>
</td></tr>
<tr><th><a href="status.html">Connector status</a></th><td><p>Display the status of connectors in the current site</p>
</td></tr>
<tr><th><a href="generate.html">Connector generate</a></th><td><p>Generate a Connector resource</p>
</td></tr>
</table>

</section>
