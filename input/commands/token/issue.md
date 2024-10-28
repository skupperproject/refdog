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
  - name: Token redeem command
    url: /commands/token/redeem.html
---

# Token issue command

<section>

Issue a token file redeemable for a link to the current site.

This command first creates an access grant in order to issue
the token.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>Waits for</th><td>Ready</td></table>

</section>

<section>

## Usage

~~~ shell
skupper token issue <file> [options]
~~~

</section>

<section>

## Examples

~~~ console
# Issue an access token
$ skupper token issue ~/token.yaml
Waiting for status...
Access grant "west-6bfn6" is ready.
Token file /home/fritz/token.yaml created.

Transfer this file to a remote site. At the remote site,
create a link to this site using the 'skupper token
redeem' command:

    $ skupper token redeem <file>

The token expires after 1 use or after 15 minutes.

# Issue an access token with non-default limits
$ skupper token issue ~/token.yaml --expiration-window 24h --redemptions-allowed 3

# Issue a token using an existing access grant
$ skupper token issue ~/token.yaml --grant west-1
~~~

</section>

<section>

## Options

- <div class="attribute"><h3 id="option-file">file</h3><div>string, required</div></div>

  The name of the token file to create.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <div class="attribute"><h3 id="option-timeout">--timeout</h3><div>&lt;string&gt; (duration)</div></div>

  Raise an error if the operation does not complete in the given
  period of time.

  <table class="fields"><tr><th>Default</th><td><p><code>60s</code></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <div class="attribute"><h3 id="option-expiration-window">--expiration-window</h3><div>&lt;string&gt; (duration)</div></div>

  The period of time in which an access token for this
  grant can be redeemed.

  <table class="fields"><tr><th>Default</th><td><p><code>15m</code></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <div class="attribute"><h3 id="option-redemptions-allowed">--redemptions-allowed</h3><div>&lt;integer&gt;</div></div>

  The number of times an access token for this grant can
  be redeemed.

  <table class="fields"><tr><th>Default</th><td>1</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <div class="attribute"><h3 id="option-grant">--grant</h3><div>&lt;string&gt;</div></div>

  Use the named access grant instead of creating a new
  one.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <div class="attribute"><h3 id="option-namespace">--namespace</h3><div>&lt;string&gt;</div></div>

  Set the namespace.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="/concepts/namespace.html">Namespace concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a></td></table>

- <div class="attribute"><h3 id="option-context">--context</h3><div>&lt;string&gt;</div></div>

  Set the kubeconfig context.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/">Kubernetes kubeconfigs</a></td></table>

- <div class="attribute"><h3 id="option-kubeconfig">--kubeconfig</h3><div>&lt;string&gt;</div></div>

  Set the path to the kubeconfig file.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/">Kubernetes kubeconfigs</a></td></table>

- <div class="attribute"><h3 id="option-platform">--platform</h3><div>&lt;string&gt;</div></div>

  Set the Skupper platform.

  <table class="fields"><tr><th>Default</th><td><p><code>kubernetes</code></p>
  </td><tr><th>Choices</th><td><table class="choices"><tr><th><code>kubernetes</code></th><td><p>Kubernetes</p>
  </td></tr><tr><th><code>docker</code></th><td><p>Docker</p>
  </td></tr><tr><th><code>podman</code></th><td><p>Podman</p>
  </td></tr><tr><th><code>systemd</code></th><td><p>Systemd</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="/concepts/platform.html">Platform concept</a></td></table>

- <div class="attribute"><h3 id="option-help">--help</h3><div>boolean</div></div>

  Display help and exit.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

</section>

<section>

## Errors

- **Link access is not enabled**

  Link access at this site is not currently enabled.  You
  can use "skupper site update --enable-link-access" to
  enable it.

</section>
