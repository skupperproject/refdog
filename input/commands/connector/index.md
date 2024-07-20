---
body_class: object command
links:
  - name: Connector concept
    url: /concepts/connector.html
  - name: Connector resource
    url: /resources/connector.html
  - name: Listener command
    url: /commands/listener.html
---

# Connector commands

<section>

Display help for connector commands and exit.

</section>

<section>

## Usage

~~~ shell
skupper connector [subcommand] [options]
~~~

</section>

<section>

## Subcommands

<table class="objects">
<tr><th><a href="create.html">create</a></th><td><p>Create a connector</p>
</td></tr>
<tr><th><a href="status.html">status</a></th><td><p>Display the status of connectors in the current site</p>
</td></tr>
<tr><th><a href="update.html">update</a></th><td><p>Update a connector</p>
</td></tr>
<tr><th><a href="delete.html">delete</a></th><td><p>Delete a connector</p>
</td></tr>
</table>

</section>

<section>

## Options

- <h3 id="platform">--platform <span class="attribute-info">string</span></h3>

  Set the Skupper platform.

  <table class="fields"><tr><th>Choices</th><td><table class="choices"><tr><th><code>kubernetes</code></th><td><p>Kubernetes</p>
  </td></tr><tr><th><code>docker</code></th><td><p>Docker or Podman</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="/concepts/platform.html">Platform concept</a></td></table>

- <h3 id="help">--help <span class="attribute-info"></span></h3>

  Display help and exit.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

</section>
