---
body_class: object command
links:
  - name: Listener concept
    url: /concepts/listener.html
  - name: Listener resource
    url: /resources/listener.html
  - name: Connector command
    url: /commands/connector.html
---

# Listener command

<section>

Display help for listener commands and exit.

</section>

<section>

## Usage

~~~ shell
skupper listener [subcommand] [options]
~~~

</section>

<section>

## Subcommands

<table class="objects">
<tr><th><a href="listener-create.html">listener create</a></th><td><p>Create a listener</p>
</td></tr>
<tr><th><a href="listener-status.html">listener status</a></th><td><p>Display the status of listeners in the current site</p>
</td></tr>
<tr><th><a href="listener-update.html">listener update</a></th><td><p>Update a listener</p>
</td></tr>
<tr><th><a href="listener-delete.html">listener delete</a></th><td><p>Delete a listener</p>
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
