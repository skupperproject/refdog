---
body_class: object resource
links:
  - name: Connector concept
    url: /concepts/connector.html
  - name: Connector command
    url: /commands/connector/index.html
  - name: Listener resource
    url: /resources/listener.html
---

# Connector resource

<section>

Binds local workloads to listeners in remote sites.

Each site can have multiple connector resources.

~~~ yaml
apiVersion: skupper.io/v2alpha1
kind: Connector
~~~

</section>

<section>

## Examples

A connector in site East for the Hello World backend service:

~~~ yaml
apiVersion: skupper.io/v2alpha1
kind: Connector
metadata:
  name: backend
  namespace: hello-world-east
spec:
  routingKey: backend
  port: 8080
  selector: app=backend
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

<div class="attribute folded">
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

<div class="attribute">
<div class="attribute-heading">
<h3 id="spec-routingkey">routingKey</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

The identifier used to route traffic from listeners to
connectors.  To expose a local workload to a remote
site, the remote listener and the local connector must
have matching routing keys.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/routing-key.html">Routing key concept</a></td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="spec-port">port</h3>
<div class="attribute-type-info">integer</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

The port on the target workload to forward traffic to.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="spec-selector">selector</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">frequently used</div>
</div>
<div class="attribute-body">

A Kubernetes label selector for specifying target server
pods.

On Kubernetes, you usually want to use this.  As an
alternative, you can use `host`.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors">Kubernetes label selectors</a>, <a href="https://kubernetes.io/docs/concepts/workloads/pods/">Kubernetes pods</a></td></table>

</div>
</div>

<div class="attribute folded">
<div class="attribute-heading">
<h3 id="spec-host">host</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

The hostname or IP address of the server.  This is an
alternative to `selector` for specifying the target
server.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute folded">
<div class="attribute-heading">
<h3 id="spec-tlscredentials">tlsCredentials</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

The name of a Kubernetes secret containing the trusted
server certificate (typically a CA).

It can optionally include a client certificate and key for
mutual TLS.

This option is used when setting up router-to-server TLS
encryption.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="">Site-scoped TLS</a></td></table>

</div>
</div>

<div class="attribute folded">
<div class="attribute-heading">
<h3 id="spec-includenotready">includeNotReady</h3>
<div class="attribute-type-info">boolean</div>
</div>
<div class="attribute-body">

If set, include server pods that are not in the ready
state.

<table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/">Kubernetes pod lifecycle</a></td></table>

</div>
</div>

<div class="attribute folded">
<div class="attribute-heading">
<h3 id="spec-type">type</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

The connector type.

<table class="fields"><tr><th>Default</th><td><p><code>tcp</code></p>
</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute folded">
<div class="attribute-heading">
<h3 id="spec-settings">settings</h3>
<div class="attribute-type-info">object</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

Additional settings.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

</section>

<section class="attributes">

## Status properties

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
<div class="attribute-type-info">string</div>
<div class="attribute-flags">frequently used</div>
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
