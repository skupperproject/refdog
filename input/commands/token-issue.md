---
body_class: command
links:
  - name: token redeem command
    url: /commands/token-redeem.html
---

# Token issue command

<section>

Issue a token redeemable for a link to the current site.

Issue a token that can be redeemed at a remote site for a
link to the current site.

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

- <h3 id="file">file <span class="option-info">string, required</span></h3>

  The name of the token file.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h3 id="expiration-window">--expiration-window <span class="option-info">string (duration)</span></h3>

  The period of time in which an access token for this
  grant can be redeemed.

  | | |
  |-|-|
  | Default | `15m` |
  | Platforms | Kubernetes, Docker |
  
- <h3 id="redemptions-allowed">--redemptions-allowed <span class="option-info">integer</span></h3>

  The number of times an access token for this grant can
  be redeemed.

  | | |
  |-|-|
  | Default | 1 |
  | Platforms | Kubernetes, Docker |
  
### Context options

- <h3 id="namespace">--namespace <span class="option-info">string</span></h3>

  Set the namespace.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Namespace concept]({{site_prefix}}/concepts/namespace.html), [Kubernetes namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) |
  
- <h3 id="context">--context <span class="option-info">string</span></h3>

  Set the kubeconfig context.

  | | |
  |-|-|
  | Platforms | Kubernetes |
  | See also | [Kubernetes kubeconfigs](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) |
  
- <h3 id="platform">--platform <span class="option-info">string</span></h3>

  Set the Skupper platform.

  | | |
  |-|-|
  | Choices | <table><tr><td><code>kubernetes</code></td><td>Kubernetes</td></tr><tr><td><code>docker</code></td><td>Docker or Podman</td></tr></table> |
  | Platforms | Kubernetes, Docker |
  | See also | [Platform concept]({{site_prefix}}/concepts/platform.html) |
  
### Global options

- <h3 id="help">--help <span class="option-info"></span></h3>

  Display help and exit.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
</section>

<section>

## Errors

- **Link access is not enabled**

  Link access at this site is not currently enabled.  You
  can use "skupper site update --enable-link-access" to
  enable it.

</section>
