---
body_class: resource
links:
  - name: Connector concept
    url: /concepts/connector.html
  - name: Listener resource
    url: /resources/listener.html
  - name: Connector command
    url: /commands/connector.html
---

# Connector resource

<section>

A connector binds local servers to listeners in remote
sites.

Theses:

  - A connector targets a workload in the local site (or
    reachable on the local network).
  - A connector forwards connections from matching listeners
    at remote sites to the workload in the local site.

Each site can have multiple connector resources.

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

## Spec properties

- <h3 id="routingkey">routingKey <span class="property-info">string, required</span></h3>

  The identifier used to route traffic from listeners to
  connectors.  To expose a local workload to a remote
  site, the remote listener and the local connector must
  have matching routing keys.

  _See also:_ [Routing key concept]({{site_prefix}}/concepts/routing-key.html)

- <h3 id="port">port <span class="property-info">integer, required</span></h3>

  The port number the target workload is listening on.

- <h3 id="selector">selector <span class="property-info">string</span></h3>

  A Kubernetes label selector for targeting server pods.

  _See also:_ [Kubernetes label selectors]({{site_prefix}}https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors), [Kubernetes pods]({{site_prefix}}XXX)

- <h3 id="host">host <span class="property-info">string</span></h3>

  The hostname or IP address of the server.  This is an
  alternative to `selector` for specifying the target
  server.

- <h3 id="tlssecret">tlsSecret <span class="property-info">string</span></h3>

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  
  This option is used when setting up client-to-router TLS
  encryption.

  _See also:_ [TLS re-encrypt]({{site_prefix}}XXX)

- <h3 id="includenotready">includeNotReady <span class="property-info">boolean</span></h3>

  If set, include server pods that are not in the ready
  state.

- <h3 id="type">type <span class="property-info">string</span></h3>

  The connector type.

  _Default:_ `tcp`

</section>

<section>

## Status properties

- <h3 id="status">status <span class="property-info">string</span></h3>

  The current state of the resource.

- <h3 id="active">active <span class="property-info">boolean</span></h3>

</section>
