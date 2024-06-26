---
body_class: object command
links:
  - name: Access grant concept
    url: /concepts/access-grant.html
  - name: Access token concept
    url: /concepts/access-token.html
  - name: AccessGrant resource
    url: /resources/accessgrant.html
  - name: AccessToken resource
    url: /resources/accesstoken.html
---

# Token command

<section>

Display help for token commands and exit.

</section>

<section>

## Usage

~~~ shell
skupper token [subcommand] [options]
~~~

</section>

<section>

## Subcommands

<table class="objects">
<tr><th><a href="token-issue.html">token issue</a></th><td><p>Issue a token file redeemable for a link to the current site</p>
</td></tr>
<tr><th><a href="token-redeem.html">token redeem</a></th><td><p>Redeem a token file in order to create a link to a remote site</p>
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
