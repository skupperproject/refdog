---
body_class: object command
links:
  - name: Site concept
    url: /concepts/site.html
  - name: Site resource
    url: /resources/site.html
---

# Site command

<section>

Display help for site commands and exit.

</section>

<section>

## Usage

~~~ shell
skupper site [subcommand] [options]
~~~

</section>

<section>

## Subcommands

<table class="objects">
<tr><th><a href="site-create.html">site create</a></th><td><p>Create a site</p>
</td></tr>
<tr><th><a href="site-update.html">site update</a></th><td><p>Change site settings</p>
</td></tr>
<tr><th><a href="site-delete.html">site delete</a></th><td><p>Delete a site</p>
</td></tr>
<tr><th><a href="site-status.html">site status</a></th><td><p>Display the current status of a site</p>
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
