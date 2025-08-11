---
body_class: object resource
refdog_links:
- title: Site configuration
  url: /topics/site-configuration.html
- title: Site concept
  url: /concepts/site.html
- title: Site command
  url: /commands/site/index.html
- title: Link resource
  url: /resources/link.html
refdog_object_has_attributes: true
---

# Site resource

A site is a place on the network where application workloads are
running. Sites are joined by links.

The Site resource is the basis for site configuration. It is the
parent of all Skupper resources in its namespace. There can be only
one active Site resource per namespace.

## Examples

A minimal site:

~~~ yaml
apiVersion: skupper.io/v2alpha1
kind: Site
metadata:
  name: east
  namespace: hello-world-east
~~~

A site configured to accept links:

~~~ yaml
apiVersion: skupper.io/v2alpha1
kind: Site
metadata:
  name: west
  namespace: hello-world-west
spec:
  linkAccess: default
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
<h3 id="spec-link-access">linkAccess</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">frequently used</div>
</div>
<div class="attribute-body">

Configure external access for links from remote sites.

Sites and links are the basis for creating application
networks. In a simple two-site network, at least one of the
sites must have link access enabled. Choices include:

- `none`: No linking to this site is enabled.
- `default`: Use the default link access for the current platform. For OpenShift, the default is `route`. For other Kubernetes flavors, the default is `loadbalancer`.
- `route`: Use an OpenShift route.
- `loadbalancer`: Use a Kubernetes load balancer.

<table class="fields"><tr><th>Default</th><td><p><code>none</code></p>
</td><tr><th>Choices</th><td><table class="choices"><tr><th><code>none</code></th><td><p>No linking to this site is permitted.</p>
</td></tr><tr><th><code>default</code></th><td><p>Use the default link access for the current platform. On OpenShift, the default is <code>route</code>.  For other Kubernetes flavors, the default is <code>loadbalancer</code>.</p>
</td></tr><tr><th><code>route</code></th><td><p>Use an OpenShift route.  <em>OpenShift only.</em></p>
</td></tr><tr><th><code>loadbalancer</code></th><td><p>Use a Kubernetes load balancer.</p>
</td></tr></table></td><tr><th>Updatable</th><td>True</td><tr><th>See also</th><td><a href="{{site.prefix}}/concepts/link.html">Link concept</a>, <a href="{{site.prefix}}/topics/site-linking.html">Site linking</a></td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="spec-ha">ha</h3>
<div class="attribute-type-info">boolean</div>
</div>
<div class="attribute-body">

Configure the site for high availability (HA). HA sites
have two active routers.

Note that Skupper routers are stateless, and they restart
after failure. This already provides a high level of
availability. Enabling HA goes further and reduces the
window of downtime caused by restarts.

By default, Pod anti-affinity will be configured on the router
Deployments when HA is enabled. To overwrite this behavior
see the `disable-anti-affinity` Site setting.

<table class="fields"><tr><th>Default</th><td>False</td><tr><th>Updatable</th><td>True</td><tr><th>See also</th><td><a href="{{site.prefix}}/topics/high-availability.html">High availability</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-default-issuer">defaultIssuer</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

Advanced. The name of a Kubernetes secret containing the
signing CA used to generate a certificate from a token. A
secret is generated if none is specified.

This issuer is used by AccessGrant and RouterAccess if a
specific issuer is not set. Defaults to `skupper-site-ca`

<table class="fields"><tr><th>Default</th><td><p><code>skupper-site-ca</code></p>
</td><tr><th>Updatable</th><td>True</td><tr><th>See also</th><td><a href="{{site.prefix}}/topics/router-tls.html">Router TLS</a>, <a href="https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets">Kubernetes TLS secrets</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-edge">edge</h3>
<div class="attribute-type-info">boolean</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

Advanced. Configure the site to operate in edge mode. Edge
sites cannot accept links from remote sites.

Edge mode can help you scale your network to large numbers
of sites. However, for networks with 16 or fewer sites,
there is little benefit.

Currently, edge sites cannot also have HA enabled.

<table class="fields"><tr><th>Default</th><td>False</td><tr><th>See also</th><td><a href="{{site.prefix}}/topics/large-networks.html">Large networks</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-service-account">serviceAccount</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

Advanced. The name of the Kubernetes service account under
which to run the Skupper router. A service account is
generated if none is specified.

<table class="fields"><tr><th>Default</th><td><p><em>Generated</em></p>
</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/security/service-accounts/">Kubernetes service accounts</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-settings">settings</h3>
<div class="attribute-type-info">object</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

Advanced. A map containing additional settings. Each map
entry has a string name and a string value.

**Note:** In  general, we recommend not changing settings
from their default values.

- `routerDataConnections`: Set the number of router worker threads. Minimum 2.
- `routerLogging`: Set the number of router logging level. Options are "info", "warning", "error".
- `disable-anti-affinity`: Set to "true" in order to prevent skupper from specifying router pod affinity.
- `size`: The desired site sizing profile to use for constraining pod resources. Corresponds to a ConfigMap with matching `skupper.io/site-sizing` label.
- `tls-prior-valid-revisions`: Set the number of revisions to TLS Secrets backing Site Link connections that are permissible to hold open to preserve established service connections. An unsigned integer defaults to 1. Set to 0 to immediately disrupt connections secured with old TLS configurations.

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

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-conditions">conditions</h3>
<div class="attribute-type-info">array</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

A set of named conditions describing the current state of the resource.

- `Configured`: The output resources for this resource have been created.
- `Running`: There is at least one router pod running.
- `Resolved`: The hostname or IP address for link access is available.
- `Ready`: The site is ready for use. All other conditions are true.

<table class="fields"><tr><th>See also</th><td><a href="{{site.prefix}}/topics/resource-status.html">Resource status</a>, <a href="https://maelvls.dev/kubernetes-conditions/">Kubernetes conditions</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-default-issuer">defaultIssuer</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

The name of the Kubernetes secret containing the active default signing CA.

<table class="fields"><tr><th>See also</th><td><a href="{{site.prefix}}/topics/router-tls.html">Router TLS</a>, <a href="https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets">Kubernetes TLS secrets</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-endpoints">endpoints</h3>
<div class="attribute-type-info">array</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

An array of connection endpoints. Each item has a name, host, port, and group. These include connection endpoints for link access.

<table class="fields"><tr><th>See also</th><td><a href="{{site.prefix}}/concepts/link.html">Link concept</a>, <a href="{{site.prefix}}/topics/site-linking.html">Site linking</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-network">network</h3>
<div class="attribute-type-info">array</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">



</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-sites-in-network">sitesInNetwork</h3>
<div class="attribute-type-info">integer</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

<table class="fields"><tr><th>See also</th><td><a href="{{site.prefix}}/concepts/network.html">Network concept</a></td></table>

</div>
</div>
