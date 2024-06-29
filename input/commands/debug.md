---
body_class: object command
---

# Debug command

<section>

Display help for debug commands and exit.

</section>

<section>

## Usage

~~~ shell
skupper debug [subcommand] [options]
~~~

</section>

<section>

## Subcommands

<table class="objects">
<tr><th><a href="debug-dump.html">debug dump</a></th><td><p>Generate a debug dump file</p>
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
