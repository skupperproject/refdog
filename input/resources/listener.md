---
body_class: object resource
refdog_links:
- title: Service exposure
  url: /topics/service-exposure.html
- title: Listener concept
  url: /concepts/listener.html
- title: Listener command
  url: /commands/listener/index.html
- title: Connector resource
  url: /resources/connector.html
refdog_object_has_attributes: true
---

# Listener resource

A listener binds a local connection endpoint to connectors in remote sites.
Listeners and connector are matched by routing key.

A Listener resource specifies a host and port for accepting connections
from local client. To expose a multi-port service, create multiple listeners
with the same host value.

## Examples

A listener in site West for the Hello World backend service
in site East:

~~~ yaml
apiVersion: skupper.io/v2alpha1
kind: Listener
metadata:
  name: backend
  namespace: hello-world-west
spec:
  routingKey: backend
  host: backend
  port: 8080
~~~

## Metadata properties

<div class="attribute">
<div class="attribute-heading">
<h3 id="metadata-name">name</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

The name of the resource.

<table class="fields"><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="metadata-namespace">namespace</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

The namespace of the resource.

<table class="fields"><tr><th>See also</th><td><a href="{{site.prefix}}/concepts/platform.html">Platform concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a>, <a href="{{site.prefix}}/topics/system-namespaces.html">System namespaces</a></td></table>

</div>
</div>

## Spec properties

<div class="attribute">
<div class="attribute-heading">
<h3 id="spec-routing-key">routingKey</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

The identifier to route traffic from listeners to connectors. To
enable connecting to a service at a remote site, the local listener
and the remote connector must have matching routingKeys.

<table class="fields"><tr><th>Updatable</th><td>True</td><tr><th>See also</th><td><a href="{{site.prefix}}/concepts/routing-key.html">Routing key concept</a></td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="spec-host">host</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

The hostname or IP address of the local listener. Clients at this
site use the listener host and port to establish connections to the
remote service.

<table class="fields"><tr><th>Updatable</th><td>True</td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="spec-port">port</h3>
<div class="attribute-type-info">integer</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

The port of the local listener. Clients at this site use the listener
host and port to establish connections to the remote service.

<table class="fields"><tr><th>Updatable</th><td>True</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-expose-pods-by-name">exposePodsByName</h3>
<div class="attribute-type-info">boolean</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

If true, expose each pod as an individual service. This allows individual
pods to be directly connected across a network. The pod names will be used
to create each service.

<table class="fields"><tr><th>Default</th><td>False</td><tr><th>See also</th><td><a href="{{site.prefix}}/topics/individual-pod-services.html">Individual pod services</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-tls-credentials">tlsCredentials</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

The name of a bundle of TLS certificates used for secure client-to-router
communication. The bundle contains the server certificate and key. It
optionally includes the trusted client certificate (usually a CA) for
mutual TLS.

On Kubernetes, the value is the name of a Secret in the current namespace.
On Docker, Podman, and Linux, the value is the name of a directory under
input/certs/ in the current namespace.

<table class="fields"><tr><th>See also</th><td><a href="{{site.prefix}}/topics/application-tls.html">Application TLS</a>, <a href="https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets">Kubernetes TLS secrets</a>, <a href="{{site.prefix}}/topics/system-tls-credentials.html">System TLS credentials</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-settings">settings</h3>
<div class="attribute-type-info">object</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

A map containing additional settings. Each map entry has a string name and a string value.

**Note:** In general, we recommend not changing settings from
their default values.

<table class="fields"><tr><th>See also</th><td><a href="{{site.prefix}}/topics/resource-settings.html">Resource settings</a></td></table>

</div>
</div>

## Status properties

<div class="attribute">
<div class="attribute-heading">
<h3 id="status-status">status</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

The current state of the resource.
- `Pending`: The resource is being processed.
- `Error`: There was an error processing the resource. See `message` for more information.
- `Ready`: The resource is ready to use.

<table class="fields"><tr><th>See also</th><td><a href="{{site.prefix}}/topics/resource-status.html">Resource status</a></td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="status-message">message</h3>
<div class="attribute-type-info">string</div>
</div>
<div class="attribute-body">

A human-readable status message. Error messages are reported here.

<table class="fields"><tr><th>See also</th><td><a href="{{site.prefix}}/topics/resource-status.html">Resource status</a></td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="status-has-matching-connector">hasMatchingConnector</h3>
<div class="attribute-type-info">boolean</div>
</div>
<div class="attribute-body">

True if there is at least one connector with a matching routing key (usually in a remote site).

<table class="fields"><tr><th>Default</th><td>False</td><tr><th>See also</th><td><a href="{{site.prefix}}/concepts/routing-key.html">Routing key concept</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-conditions">conditions</h3>
<div class="attribute-type-info">array</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

A set of named conditions describing the current state of the resource.

- `Configured`: The listener configuration has been applied to the router.
- `Operational`: There is at least one connector corresponding to this listener.
- `Ready`: The listener is ready for use. All other conditions are true.

<table class="fields"><tr><th>See also</th><td><a href="{{site.prefix}}/topics/resource-status.html">Resource status</a>, <a href="https://maelvls.dev/kubernetes-conditions/">Kubernetes conditions</a></td></table>

</div>
</div>
