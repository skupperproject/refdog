---
body_class: object resource
refdog_object_has_attributes: true
refdog_object_links:
- title: AttachedConnector resource
  url: /resources/attachedconnector.html
refdog_object_toc:
- id: ''
  title: Overview
- children:
  - id: metadata-name
    title: name
  - id: metadata-namespace
    title: namespace
  id: metadata
  title: Metadata
- children:
  - id: spec-connectornamespace
    title: connectorNamespace
  - id: spec-routingkey
    title: routingKey
  - id: spec-settings
    title: settings
  id: spec
  title: Spec
- children:
  - id: status-status
    title: status
  - id: status-message
    title: message
  - id: status-conditions
    title: conditions
  - id: status-hasmatchinglisteners
    title: hasMatchingListeners
  - id: status-selectedpods
    title: selectedPods
  id: status
  title: Status
---

# AttachedConnectorBinding resource

<section>

A binding to an attached connector in a peer namespace.

~~~ yaml
apiVersion: skupper.io/v2alpha1
kind: AttachedConnectorBinding
~~~

</section>

<section class="attributes">

## Metadata

<div class="attribute">
<div class="attribute-heading">
<h3 id="metadata-name">name</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

The name of the resource.


The name must be the same as that of the associated
AttachedConnector resource in the connector namespace.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

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

## Spec

<div class="attribute">
<div class="attribute-heading">
<h3 id="spec-connectornamespace">connectorNamespace</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

The name of the namespace where the associated
AttachedConnector is located.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="spec-routingkey">routingKey</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

The identifier used to route traffic from listeners to
connectors.  To expose a local workload to a remote site, the
remote listener and the local connector must have matching
routing keys.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/routing-key.html">Routing key concept</a></td></table>

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

## Status

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-status">status</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

The current state of the resource.

- Pending
- Ready

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-message">message</h3>
<div class="attribute-type-info">None</div>
</div>
<div class="attribute-body">

A human-readable status message.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-hasmatchinglisteners">hasMatchingListeners</h3>
<div class="attribute-type-info">boolean</div>
</div>
<div class="attribute-body">

<table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

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

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-selectedpods">selectedPods</h3>
<div class="attribute-type-info">array</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

</section>
