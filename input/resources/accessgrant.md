---
body_class: object resource
links:
  - name: AccessToken resource
    url: /resources/accesstoken.html
  - name: Token issue command
    url: /commands/token/issue.html
attributes: true
---

# AccessGrant resource

<section>

Permission to redeem access tokens for links to the local
site.  A remote site can use a token containing the grant
URL and secret code to obtain a certificate signed by the
grant's certificate authority (CA), within a certain
expiration window and for a limited number of redemptions.

The `code`, `url`, and `ca` properties of the resource
status are used to generate access tokens from the grant.

~~~ yaml
apiVersion: skupper.io/v2alpha1
kind: AccessGrant
~~~

</section>

<section class="attributes">

## Metadata properties

<div class="attribute">
<div class="attribute-heading">
<h3 id="metadata-name">name</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

The name of the resource.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="metadata-namespace">namespace</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

The namespace of the resource.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/namespace.html">Namespace concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a></td></table>

</div>
</div>

</section>

<section class="attributes">

## Spec properties

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-redemptionsallowed">redemptionsAllowed</h3>
<div class="attribute-type-info">integer</div>
</div>
<div class="attribute-body">

The number of times an access token for this grant can
be redeemed.

<table class="fields"><tr><th>Default</th><td>1</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-expirationwindow">expirationWindow</h3>
<div class="attribute-type-info">string (duration)</div>
</div>
<div class="attribute-body">

The period of time in which an access token for this
grant can be redeemed.

<table class="fields"><tr><th>Default</th><td><p><code>15m</code></p>
</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-code">code</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

The secret code used to authenticate access tokens
submitted for redemption.

If not set, a value for the code field in the status is
generated.

<table class="fields"><tr><th>Default</th><td><p><em>Generated</em></p>
</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-issuer">issuer</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

The name of a Kubernetes secret used to generate a
certificate when redeeming a token for this grant.

If not set, the defaultIssuer on Site is used.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-settings">settings</h3>
<div class="attribute-type-info">object</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

A map containing additional settings.  Each map entry is a
string name and a string value.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

</section>

<section class="attributes">

## Status properties

<div class="attribute">
<div class="attribute-heading">
<h3 id="status-status">status</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">frequently used</div>
</div>
<div class="attribute-body">

The current state of the resource.

- Pending
- Ready

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="status-message">message</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">frequently used</div>
</div>
<div class="attribute-body">

A human-readable status message.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-redemptions">redemptions</h3>
<div class="attribute-type-info">integer</div>
</div>
<div class="attribute-body">

The number of times a token for this grant has been
redeemed.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-expirationtime">expirationTime</h3>
<div class="attribute-type-info">string (date-time)</div>
</div>
<div class="attribute-body">

The point in time when the grant expires.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-url">url</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

The URL of the token-redemption service for this grant.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-ca">ca</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

The trusted server certificate of the token-redemption
service for this grant.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-code">code</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

The secret code used to authenticate access tokens
submitted for redemption.

<table class="fields"><tr><th>Default</th><td><p><em>Generated</em></p>
</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-conditions">conditions</h3>
<div class="attribute-type-info">array</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

A set of named conditions describing the current state of the
resource.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://maelvls.dev/kubernetes-conditions/">Kubernetes conditions</a></td></table>

</div>
</div>

</section>
