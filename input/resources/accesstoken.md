---
body_class: object resource
links:
  - name: AccessGrant resource
    url: /resources/accessgrant.html
  - name: Token redeem command
    url: /commands/token/redeem.html
---

# AccessToken resource

<section>

A transferrable token redeemable for a link to a remote
site.  An access token contains the URL and secret code of a
corresponding access grant.

~~~ yaml
apiVersion: skupper.io/v2alpha1
kind: AccessToken
~~~

</section>

<section class="attributes">

## Metadata properties

<div class="attribute">

<div class="attribute-heading"><h3 id="metadata-name">name</h3><div>string, required</div></div>

The name of the resource.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

</div>

<div class="attribute">

<div class="attribute-heading"><h3 id="metadata-namespace">namespace</h3><div>string</div></div>

The namespace of the resource.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/namespace.html">Namespace concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a></td></table>

</div>

</section>

<section class="attributes">

## Spec properties

<div class="attribute">

<div class="attribute-heading"><h3 id="spec-url">url</h3><div>string, required</div></div>

The URL of the token redemption service at the remote
site.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>

<div class="attribute">

<div class="attribute-heading"><h3 id="spec-ca">ca</h3><div>string, required</div></div>

The trusted server certificate of the token redemption
service at the remote site.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>

<div class="attribute">

<div class="attribute-heading"><h3 id="spec-code">code</h3><div>string, required</div></div>

The secret code used to authenticate the token when
submitted for redemption.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>

<div class="attribute">

<div class="attribute-heading"><h3 id="spec-settings">settings</h3><div>object</div></div>

Additional settings.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>

</section>

<section class="attributes">

## Status properties

<div class="attribute">

<div class="attribute-heading"><h3 id="status-redeemed">redeemed</h3><div>boolean</div></div>

True if the token has been redeemed.

<table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>

<div class="attribute">

<div class="attribute-heading"><h3 id="status-status">status</h3><div>string</div></div>

The current state of the resource.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>

<div class="attribute">

<div class="attribute-heading"><h3 id="status-message">message</h3><div>string</div></div>

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>

<div class="attribute">

<div class="attribute-heading"><h3 id="status-conditions">conditions</h3><div>array</div></div>

YOYO

<table class="fields"><tr><th>Platforms</th><td>Kubernetes</td></table>

</div>

</section>
