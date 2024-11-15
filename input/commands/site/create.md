---
body_class: object command
refdog_object_has_attributes: true
refdog_object_links:
- title: Site concept
  url: /concepts/site.html
- title: Site resource
  url: /resources/site.html
refdog_object_toc:
- id: ''
  title: Overview
- id: usage
  title: Usage
- id: examples
  title: Examples
- id: primary-options
  title: Primary options
- id: global-options
  title: Global options
---

# Site create command

<section>

Create a site.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>Waits for</th><td>Ready</td></table>

</section>

<section>

## Usage

~~~ shell
skupper site create <name> [options]
~~~

</section>

<section>

## Examples

~~~ console
# Create a site
$ skupper site create west
Waiting for status...
Site "west" is ready.

# Create a site that can accept links from remote sites
$ skupper site create west --enable-link-access
~~~

</section>

<section class="attributes">

## Primary options

<div class="attribute">
<div class="attribute-heading">
<h3 id="option-name">&lt;name&gt;</h3>
<div class="attribute-type-info">string</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

A name of your choice for the Skupper site.  This name is
displayed in the console and CLI output.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="option-enable-link-access">--enable-link-access</h3>
<div class="attribute-type-info">boolean</div>
<div class="attribute-flags">frequently used</div>
</div>
<div class="attribute-body">

Allow access for incoming links from remote sites.

<!-- XXX reference link access type -->

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/link-access.html">Link access concept</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="option-link-access-type">--link-access-type</h3>
<div class="attribute-type-info">&lt;type&gt;</div>
</div>
<div class="attribute-body">

Configure external access for links from remote sites.

Sites and links are the basis for creating application
networks.  In a simple two-site network, at least one of
the sites must have link access enabled.

<table class="fields"><tr><th>Default</th><td><p><code>default</code></p>
</td><tr><th>Choices</th><td><table class="choices"><tr><th><code>default</code></th><td><p>Use the default link access.  On OpenShift, the default is <code>route</code>.  For other Kubernetes flavors, the default is <code>loadbalancer</code>.</p>
</td></tr><tr><th><code>route</code></th><td><p>Use an OpenShift route.  <em>OpenShift only.</em></p>
</td></tr><tr><th><code>loadbalancer</code></th><td><p>Use a Kubernetes load balancer.  <em>Kubernetes only.</em></p>
</td></tr></table></td><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="">Site linking</a>, <a href="/concepts/link-access.html">Link access concept</a>, <a href="https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer">Kubernetes load balancer services</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="option-enable-ha">--enable-ha</h3>
<div class="attribute-type-info">boolean</div>
</div>
<div class="attribute-body">

Configure the site for high availability (HA).  HA sites
have two active routers.

Note that Skupper routers are stateless, and they restart
after failure.  This already provides a high level of
availability.  Enabling HA goes further and reduces the
window of downtime caused by restarts.

<table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="">Advanced deployment options</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="option-timeout">--timeout</h3>
<div class="attribute-type-info">&lt;duration&gt;</div>
</div>
<div class="attribute-body">

Raise an error if the operation does not complete in the given
period of time.

<table class="fields"><tr><th>Default</th><td><p><code>60s</code></p>
</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="https://pkg.go.dev/time#ParseDuration">Duration format</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="option-wait">--wait</h3>
<div class="attribute-type-info">&lt;status&gt;</div>
</div>
<div class="attribute-body">

Wait for the given status before exiting.

<table class="fields"><tr><th>Default</th><td><p><code>ready</code></p>
</td><tr><th>Choices</th><td><table class="choices"><tr><th><code>pending</code></th><td><p>Pending</p>
</td></tr><tr><th><code>configured</code></th><td><p>Configured</p>
</td></tr><tr><th><code>ready</code></th><td><p>Ready</p>
</td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="option-default-issuer">--default-issuer</h3>
<div class="attribute-type-info">&lt;name&gt;</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

The name of a Kubernetes secret containing the signing CA
used to generate a certificate from a token.  A secret is
generated if none is supplied.

This issuer is used by AccessGrant and RouterAccess if a
specific issuer is set.

<table class="fields"><tr><th>Default</th><td><p><code>skupper-site-ca</code></p>
</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="option-enable-edge">--enable-edge</h3>
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

<table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="">Advanced deployment options</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="option-service-account">--service-account</h3>
<div class="attribute-type-info">&lt;name&gt;</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

The name of the Kubernetes service account under which to
run the Skupper controller.

<table class="fields"><tr><th>Default</th><td><p><code>skupper-router</code></p>
</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="">Advanced deployment options</a>, <a href="https://kubernetes.io/docs/concepts/security/service-accounts/">Kubernetes service accounts</a></td></table>

</div>
</div>

</section>

<section class="attributes">

## Global options

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="option-context">--context</h3>
<div class="attribute-type-info">&lt;name&gt;</div>
<div class="attribute-flags">global</div>
</div>
<div class="attribute-body">

Set the kubeconfig context.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/">Kubernetes kubeconfigs</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="option-kubeconfig">--kubeconfig</h3>
<div class="attribute-type-info">&lt;file&gt;</div>
<div class="attribute-flags">global</div>
</div>
<div class="attribute-body">

Set the path to the kubeconfig file.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/">Kubernetes kubeconfigs</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="option-namespace">--namespace</h3>
<div class="attribute-type-info">(-n) &lt;name&gt;</div>
<div class="attribute-flags">global</div>
</div>
<div class="attribute-body">

Set the namespace.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/namespace.html">Namespace concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="option-platform">--platform</h3>
<div class="attribute-type-info">&lt;platform&gt;</div>
<div class="attribute-flags">global</div>
</div>
<div class="attribute-body">

Set the Skupper platform.

<table class="fields"><tr><th>Default</th><td><p><code>kubernetes</code></p>
</td><tr><th>Choices</th><td><table class="choices"><tr><th><code>kubernetes</code></th><td><p>Kubernetes</p>
</td></tr><tr><th><code>docker</code></th><td><p>Docker</p>
</td></tr><tr><th><code>podman</code></th><td><p>Podman</p>
</td></tr><tr><th><code>linux</code></th><td><p>Linux</p>
</td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/platform.html">Platform concept</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="option-help">--help</h3>
<div class="attribute-type-info">(-h) boolean</div>
<div class="attribute-flags">global</div>
</div>
<div class="attribute-body">

Display help and exit.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

</section>

<section>

## Errors

- **A site resource already exists**

  There is already a site resource defined for the namespace.

</section>
