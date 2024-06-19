---
body_class: object command
links:
  - name: Token command
    url: /commands/token.html
  - name: Token redeem command
    url: /commands/token-redeem.html
---

# Token issue command

<section>

Issue a token file redeemable for a link to the current site.

This command first creates a grant in order to issue the
token.

</section>

<section>

## Usage

~~~ shell
$ skupper token issue <file> [options]
Waiting for status...
Grant "<name>" is ready.
Token file <file> created.

Transfer this file to a remote site. At the remote site,
create a link to this site using the 'skupper token
redeem' command:

   $ skupper token redeem <file>

The token expires after 1 use or after 15 minutes.
~~~

</section>

<section>

## Examples

~~~
# Issue an access token
skupper token issue ~/token.yaml

# Issue an access token with non-default limits
skupper token issue ~/token.yaml --expiration-window 24h --redemptions-allowed 3
~~~

</section>

<section>

## Options

- <h3 id="file">file <span class="attribute-info">string, required</span></h3>

  The name of the token file to create.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="expiration-window">--expiration-window <span class="attribute-info">string (duration)</span></h3>

  The period of time in which an access token for this
  grant can be redeemed.

  <table class="fields"><tr><th>Default</th><td><code>15m</code></td><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="redemptions-allowed">--redemptions-allowed <span class="attribute-info">integer</span></h3>

  The number of times an access token for this grant can
  be redeemed.

  <table class="fields"><tr><th>Default</th><td>1</td><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="namespace">--namespace <span class="attribute-info">string</span></h3>

  Set the namespace.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="/concepts/namespace.html">Namespace concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a></td></table>

- <h3 id="context">--context <span class="attribute-info">string</span></h3>

  Set the kubeconfig context.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/">Kubernetes kubeconfigs</a></td></table>

- <h3 id="platform">--platform <span class="attribute-info">string</span></h3>

  Set the Skupper platform.

  <table class="fields"><tr><th>Choices</th><td><table class="choices"><tr><th><code>kubernetes</code></th><td><p>Kubernetes</p>
  </td></tr><tr><th><code>docker</code></th><td><p>Docker or Podman</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="/concepts/platform.html">Platform concept</a></td></table>

- <h3 id="help">--help <span class="attribute-info"></span></h3>

  Display help and exit.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

</section>

<section>

## Errors

- **Link access is not enabled**

  Link access at this site is not currently enabled.  You
  can use "skupper site update --enable-link-access" to
  enable it.

</section>
