---
body_class: object command
refdog_object_has_attributes: true
refdog_object_links:
- title: Connector concept
  url: /concepts/connector.html
- title: Connector resource
  url: /resources/connector.html
- title: Listener update command
  url: /commands/listener/update.html
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

# Connector update command

<section>

Update a connector.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>Waits for</th><td>Configured</td></table>

</section>

<section>

## Usage

~~~ shell
skupper connector update <name> <port> [options]
~~~

</section>

<section>

## Examples

~~~ console
# Change the workload and port
$ skupper connector update database --workload deployment/mysql --port 3306
Waiting for status...
Connector "database" is configured.

# Change the routing key
$ skupper connector update backend --routing-key be2
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

The name of the resource to be updated.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="option-port">&lt;port&gt;</h3>
<div class="attribute-type-info">integer</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

The port on the target workload to forward traffic to.

<!-- The port to connect to. -->

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="option-routing-key">--routing-key</h3>
<div class="attribute-type-info">&lt;string&gt;</div>
<div class="attribute-flags">frequently used</div>
</div>
<div class="attribute-body">

The identifier used to route traffic from listeners to
connectors.  To expose a local workload to a remote site, the
remote listener and the local connector must have matching
routing keys.

<table class="fields"><tr><th>Default</th><td><p><em>Value of name</em></p>
</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/routing-key.html">Routing key concept</a></td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="option-selector">--selector</h3>
<div class="attribute-type-info">&lt;string&gt;</div>
<div class="attribute-flags">frequently used</div>
</div>
<div class="attribute-body">

A Kubernetes label selector for specifying target server pods.

<!-- The selector that identifies the pods to connect to. -->

On Kubernetes, you usually want to use this.  As an alternative,
you can use `host`.

<table class="fields"><tr><th>Default</th><td><p><code>app=[value-of-name]</code></p>
</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="option-workload">--workload</h3>
<div class="attribute-type-info">&lt;resource&gt;</div>
<div class="attribute-flags">frequently used</div>
</div>
<div class="attribute-body">

A Kubernetes resource name that identifies a workload.
It resolves to an equivalent pod selector.

This is an alternative to setting the `--selector` or
`--host` options.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/workloads/">Kubernetes workloads</a></td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="option-host">--host</h3>
<div class="attribute-type-info">&lt;string&gt;</div>
</div>
<div class="attribute-body">

The hostname or IP address of the server.  This is an
alternative to `selector` for specifying the target server.

<table class="fields"><tr><th>Default</th><td><p><em>Value of name</em></p>
</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

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
<h3 id="option-timeout">--timeout</h3>
<div class="attribute-type-info">&lt;duration&gt;</div>
</div>
<div class="attribute-body">

Raise an error if the operation does not complete in the given
period of time.

<table class="fields"><tr><th>Default</th><td><p><code>60s</code></p>
</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="option-include-not-ready">--include-not-ready</h3>
<div class="attribute-type-info">boolean</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

If set, include server pods that are not in the ready
state.

<table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="option-tls-credentials">--tls-credentials</h3>
<div class="attribute-type-info">&lt;string&gt;</div>
<div class="attribute-flags">advanced</div>
</div>
<div class="attribute-body">

A named bundle of TLS certificates and keys used for secure
application-to-router communication.  The bundle contains the
trusted server certificate.  It optionally includes a client
certificate and key for mutual TLS.

On Kubernetes, the value is the name of a Secret in the current
namespace.


This option is used when setting up router-to-server TLS
authentication and encryption.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="">Site-scoped TLS</a>, <a href="https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets">Kubernetes TLS secrets</a></td></table>

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
