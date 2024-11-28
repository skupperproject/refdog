---
body_class: object command
refdog_object_has_attributes: true
refdog_object_links:
- title: Listener concept
  url: /concepts/listener.html
- title: Listener resource
  url: /resources/listener.html
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

# Listener generate command

<section>

Generate a Listener resource.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</section>

<section>

## Usage

~~~ shell
skupper listener generate <name> <port> [options]
~~~

</section>

<section>

## Examples

~~~ console
# Generate a Listener resource and print it to the console
$ skupper listener generate backend 8080
apiVersion: skupper.io/v2alpha1
kind: Listener
metadata:
  name: backend
spec:
  routingKey: backend
  port: 8080
  host: backend

# Generate a Listener resource and direct the output to a file
$ skupper listener generate backend 8080 > backend.yaml
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

The name of the resource to be generated.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="option-port">&lt;port&gt;</h3>
<div class="attribute-type-info">integer</div>
<div class="attribute-flags">required</div>
</div>
<div class="attribute-body">

The port of the local listener.  Clients at this site use
the listener host and port to establish connections to
the remote service.

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
connectors.  To enable connecting to a service at a
remote site, the local listener and the remote connector
must have matching routing keys.

<table class="fields"><tr><th>Default</th><td><p><em>Value of name</em></p>
</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/routing-key.html">Routing key concept</a></td></table>

</div>
</div>

<div class="attribute">
<div class="attribute-heading">
<h3 id="option-host">--host</h3>
<div class="attribute-type-info">&lt;string&gt;</div>
<div class="attribute-flags">frequently used</div>
</div>
<div class="attribute-body">

The hostname or IP address of the local listener.  Clients
at this site use the listener host and port to
establish connections to the remote service.

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

<table class="fields"><tr><th>Default</th><td><p><code>configured</code></p>
</td><tr><th>Choices</th><td><table class="choices"><tr><th><code>pending</code></th><td><p>Pending</p>
</td></tr><tr><th><code>configured</code></th><td><p>Configured</p>
</td></tr><tr><th><code>ready</code></th><td><p>Ready</p>
</td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

<div class="attribute collapsed">
<div class="attribute-heading">
<h3 id="option-output">--output</h3>
<div class="attribute-type-info">(-o) &lt;format&gt;</div>
</div>
<div class="attribute-body">

Select the output format.

<table class="fields"><tr><th>Default</th><td><p><code>yaml</code></p>
</td><tr><th>Choices</th><td><table class="choices"><tr><th><code>json</code></th><td><p>Produce JSON output</p>
</td></tr><tr><th><code>yaml</code></th><td><p>Produce YAML output</p>
</td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>
</div>

</section>

<section class="attributes">

## Global options

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
