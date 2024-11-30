---
body_class: object resource
refdog_object_has_attributes: true
refdog_object_links:
- title: Site linking
  url: https://example.net/
- title: Access token concept
  url: /concepts/access-token.html
- title: AccessGrant resource
  url: /resources/accessgrant.html
- title: Token redeem command
  url: /commands/token/redeem.html
refdog_object_toc:
- id: ''
  title: Overview
- id: metadata-properties
  title: Metadata properties
- id: spec-properties
  title: Spec properties
- id: status-properties
  title: Status properties
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

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="{{site_prefix}}/concepts/platform.html">Platform concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a>, <a href="https://example.net/">System namespaces</a></td></table>

</div>
</div>

</section>

<section class="attributes">

## Spec properties

<div class="attribute">
<div class="attribute-heading">
<h3 id="spec-url">url</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

The URL of the token redemption service at the remote
site.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="spec-code">code</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

The secret code used to authenticate the token when
submitted for redemption.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-ca">ca</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

The trusted server certificate of the token redemption
service at the remote site.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-linkcost">linkCost</h3>
<div class="attribute-type-info">integer</div>
</div>
<div class="attribute-body">

The link cost to use when creating the link.

<table class="fields"><tr><th>Default</th><td>1</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="https://example.net/">Load balancing</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-settings">settings</h3>
<div class="attribute-type-info">object</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

A map containing additional settings.  Each map entry has a
string name and a string value.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="https://example.net/">Resource settings</a></td></table>

</div>
</div>

</section>

<section class="attributes">

## Status properties

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-redeemed">redeemed</h3>
<div class="attribute-type-info">boolean</div>
</div>
<div class="attribute-body">

True if the token has been redeemed.  Once a token is
redeemed, it cannot be used again.

<table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-status">status</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

The current state of the resource.

- Pending
- Ready

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="https://example.net/">Resource status</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-message">message</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

A human-readable status message.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="https://example.net/">Resource status</a></td></table>

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

<table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://example.net/">Resource status</a>, <a href="https://maelvls.dev/kubernetes-conditions/">Kubernetes conditions</a></td></table>

</div>
</div>

</section>
