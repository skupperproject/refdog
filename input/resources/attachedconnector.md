---
body_class: object resource
links:
  - name: AttachedConnectorAnchor resource
    url: /resources/attachedconnectoranchor.html
  - name: Connector resource
    url: /resources/connector.html
---

# AttachedConnector resource

<section>

~~~ yaml
apiVersion: skupper.io/v2alpha1
kind: AttachedConnector
~~~

</section>

<section class="attributes">

## Metadata properties

</section>

<section class="attributes">

## Spec properties

<div class="attribute">
<div class="attribute-heading">
<h3 id="spec-sitenamespace">siteNamespace</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="spec-port">port</h3>
<div class="attribute-type-info">integer</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="spec-selector">selector</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute folded">
<div class="attribute-heading">
<h3 id="spec-tlscredentials">tlsCredentials</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute folded">
<div class="attribute-heading">
<h3 id="spec-type">type</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute folded">
<div class="attribute-heading">
<h3 id="spec-includenotready">includeNotReady</h3>
<div class="attribute-type-info">boolean</div>
</div>
<div class="attribute-body">

<table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute folded">
<div class="attribute-heading">
<h3 id="spec-settings">settings</h3>
<div class="attribute-type-info">object</div>
</div>
<div class="attribute-body">

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

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="status-message">message</h3>
<div class="attribute-type-info">None</div>
<div class="attribute-flags">frequently used</div>
</div>
<div class="attribute-body">

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute folded">
<div class="attribute-heading">
<h3 id="status-selectedpods">selectedPods</h3>
<div class="attribute-type-info">array</div>
</div>
<div class="attribute-body">

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute folded">
<div class="attribute-heading">
<h3 id="status-matchinglistenercount">matchingListenerCount</h3>
<div class="attribute-type-info">integer</div>
</div>
<div class="attribute-body">

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute folded">
<div class="attribute-heading">
<h3 id="status-conditions">conditions</h3>
<div class="attribute-type-info">array</div>
</div>
<div class="attribute-body">

A set of named conditions describing the current state of the
resource.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://maelvls.dev/kubernetes-conditions/">Kubernetes conditions</a></td></table>

</div>
</div>

</section>
