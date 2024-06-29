---
body_class: object resource
links:
  - name: Connector concept
    url: /concepts/connector.html
  - name: Connector command
    url: /commands/connector.html
  - name: Listener resource
    url: /resources/listener.html
---

# Connector resource

<section>

Binds a connection endpoint in the local site to target
workloads in remote sites.

Each site can have multiple connector resources.

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Connector
metadata:  # Metadata properties
spec:      # Spec properties
status:    # Status properties
~~~

</section>

<section>

## Examples

A connector in site East for the Hello World backend service:

~~~ yaml
apiVersion: skupper.io/v1alpha1
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

<section>

## Metadata properties

- <h3 id="name">name <span class="attribute-info">string, required</span></h3>

  The name of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

- <h3 id="namespace">namespace <span class="attribute-info">string</span></h3>

  The namespace of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="/concepts/namespace.html">Namespace concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a></td></table>

</section>

<section>

## Spec properties

- <h3 id="routingkey">routingKey <span class="attribute-info">string, required</span></h3>

  The identifier used to route traffic from listeners to
  connectors.  To expose a local workload to a remote
  site, the remote listener and the local connector must
  have matching routing keys.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="/concepts/routing-key.html">Routing key concept</a></td></table>

- <h3 id="port">port <span class="attribute-info">integer, required</span></h3>

  The port on the target workload to forward traffic to.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="selector">selector <span class="attribute-info">string</span></h3>

  A Kubernetes label selector for specifying target server
  pods.
  
  On Kubernetes, you usually want to use this.  As an
  alternative, you can use `host`.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors">Kubernetes label selectors</a>, <a href="https://kubernetes.io/docs/concepts/workloads/pods/">Kubernetes pods</a></td></table>

- <h3 id="host">host <span class="attribute-info">string</span></h3>

  The hostname or IP address of the server.  This is an
  alternative to `selector` for specifying the target
  server.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="tlssecret">tlsSecret <span class="attribute-info">string</span></h3>

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  
  This option is used when setting up client-to-router TLS
  encryption.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="">Site-scoped TLS</a></td></table>

- <h3 id="includenotready">includeNotReady <span class="attribute-info">boolean</span></h3>

  If set, include server pods that are not in the ready
  state.

  <table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/">Kubernetes pod lifecycle</a></td></table>

- <h3 id="type">type <span class="attribute-info">string</span></h3>

  The connector type.

  <table class="fields"><tr><th>Default</th><td><code>tcp</code></td><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="options">options <span class="attribute-info">object</span></h3>

  Additional settings.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

</section>

<section>

## Status properties

- <h3 id="status">status <span class="attribute-info">string</span></h3>

  The current state of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="active">active <span class="attribute-info">boolean</span></h3>

  This thing is working.

  <table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

</section>
