---
body_class: object command
links:
  - name: Link concept
    url: /concepts/link.html
  - name: Link resource
    url: /resources/link.html
  - name: Token commands
    url: /commands/token/index.html
---

# Link commands

<section>

Display help for link commands and exit.

</section>

<section>

## Usage

~~~ shell
skupper link [subcommand] [options]
~~~

</section>

<section>

## Subcommands

<table class="objects">
<tr><th><a href="create.html">create</a></th><td><p>Create a link</p>
</td></tr>
<tr><th><a href="status.html">status</a></th><td><p>Display the status of links in the current site</p>
</td></tr>
<tr><th><a href="update.html">update</a></th><td><p>Change link settings</p>
</td></tr>
<tr><th><a href="delete.html">delete</a></th><td><p>Delete a link</p>
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
