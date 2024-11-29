---
body_class: object resource
refdog_object_has_attributes: true
refdog_object_links:
- title: Site concept
  url: /concepts/site.html
- title: Site command
  url: /commands/site/index.html
- title: Network concept
  url: /concepts/network.html
- title: Platform concept
  url: /concepts/platform.html
- title: Link resource
  url: /resources/link.html
refdog_object_toc:
- id: ''
  title: Overview
- id: examples
  title: Examples
- id: metadata-properties
  title: Metadata properties
- id: spec-properties
  title: Spec properties
- id: status-properties
  title: Status properties
---

# Site resource

<section>

A place where components of your application are running.
Sites are linked to form application networks.

There can be only one Site resource per namespace.

~~~ yaml
apiVersion: skupper.io/v2alpha1
kind: Site
~~~

</section>

<section>

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

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/platform.html">Platform concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a>, <a href="https://example.net/">System namespaces</a></td></table>

</div>
</div>

</section>

<section class="attributes">

## Spec properties

<div class="attribute">
<div class="attribute-heading">
<h3 id="spec-linkaccess">linkAccess</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">frequently used</div>
</div>
<div class="attribute-body">

Configure external access for links from remote sites.

Sites and links are the basis for creating application
networks.  In a simple two-site network, at least one of
the sites must have link access enabled.

<table class="fields"><tr><th>Default</th><td><p><code>none</code></p>
</td><tr><th>Choices</th><td><table class="choices"><tr><th><code>none</code></th><td><p>No linking to this site is permitted.</p>
</td></tr><tr><th><code>default</code></th><td><p>Use the default link access for the current platform. On OpenShift, the default is <code>route</code>.  For other Kubernetes flavors, the default is <code>loadbalancer</code>.</p>
</td></tr><tr><th><code>route</code></th><td><p>Use an OpenShift route.  <em>OpenShift only.</em></p>
</td></tr><tr><th><code>loadbalancer</code></th><td><p>Use a Kubernetes load balancer.  <em>Kubernetes only.</em></p>
</td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/link.html">Link concept</a>, <a href="https://example.net/">Site linking</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-ha">ha</h3>
<div class="attribute-type-info">boolean</div>
</div>
<div class="attribute-body">

Configure the site for high availability (HA).  HA sites
have two active routers.

Note that Skupper routers are stateless, and they restart
after failure.  This already provides a high level of
availability.  Enabling HA goes further and reduces the
window of downtime caused by restarts.

<table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes</td><tr><th>Updatable</th><td>True</td><tr><th>See also</th><td><a href="https://example.net/">High availability</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-defaultissuer">defaultIssuer</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

The name of a Kubernetes secret containing the signing CA
used to generate a certificate from a token.  A secret is
generated if none is supplied.

This issuer is used by AccessGrant and RouterAccess if a
specific issuer is not set.

<table class="fields"><tr><th>Default</th><td><p><code>skupper-site-ca</code></p>
</td><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://example.net/">Router TLS</a>, <a href="https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets">Kubernetes TLS secrets</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-edge">edge</h3>
<div class="attribute-type-info">boolean</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

Configure the site to operate in edge mode.  Edge sites
cannot accept links from remote sites.

Edge mode can help you scale your network to large numbers
of sites.  However, for networks with 16 or fewer sites,
there is little benefit.

Currently, edge sites cannot also have HA enabled.

<table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="https://example.net/">Large networks</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="spec-serviceaccount">serviceAccount</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

The name of the Kubernetes service account under which to
run the Skupper controller.

<table class="fields"><tr><th>Default</th><td><p><code>skupper-router</code></p>
</td><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/security/service-accounts/">Kubernetes service accounts</a></td></table>

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


- `routerDataConnections` - Set the number of data
  connections the router uses when linking to other
  routers.<br/>
  Default: *Computed based on the number of router worker
  threads.  Minimum 2.*
- `routerLogging` - Set the router logging level.<br/>
  Default: `info`.  Choices: `debug`, `info`, `warning`, `error`.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="https://example.net/">Resource settings</a></td></table>

</div>
</div>

</section>

<section class="attributes">

## Status properties

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


- Configured
- Running
- Resolved
- Ready

<table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://example.net/">Resource status</a>, <a href="https://maelvls.dev/kubernetes-conditions/">Kubernetes conditions</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-defaultissuer">defaultIssuer</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

The name of the Kubernetes secret containing the active
default signing CA.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://example.net/">Router TLS</a>, <a href="https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets">Kubernetes TLS secrets</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-endpoints">endpoints</h3>
<div class="attribute-type-info">array</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

An array of connection endpoints.  Each item has a name, host,
port, and group.

<!-- To what purpose? -->

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/link.html">Link concept</a>, <a href="https://example.net/">Site linking</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-network">network</h3>
<div class="attribute-type-info">array</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/network.html">Network concept</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="status-sitesinnetwork">sitesInNetwork</h3>
<div class="attribute-type-info">integer</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/network.html">Network concept</a></td></table>

</div>
</div>

</section>
