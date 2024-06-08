---
body_class: resource
links:
  - name: Connector concept
    url: /concepts/connector.html
  - name: Listener resource
    url: /resources/listener.html
  - name: Connector create command
    url: /commands/connector-create.html
---

# Connector resource

<section>

A connector binds target workloads in the local site to
listeners in remote sites.

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

- <h4 id="routingkey">routingKey <span class="property-info">string, required</span></h3>

  The identifier used to route traffic from listeners to
  connectors.  To expose a local workload to a remote
  site, the remote listener and the local connector must
  have matching routing keys.

  _See also:_ [Routing key concept]({{site_prefix}}/concepts/routing-key.html)

- <h4 id="port">port <span class="property-info">integer, required</span></h3>

  The port on the target workload to forward traffic to.

- <h4 id="selector">selector <span class="property-info">string</span></h3>

  A Kubernetes label selector for specifying target pods.

  _See also:_ [Kubernetes label selectors]({{site_prefix}}https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors), [Kubernetes pods]({{site_prefix}}https://kubernetes.io/docs/concepts/workloads/pods/)

- <h4 id="host">host <span class="property-info">string</span></h3>

  The hostname or IP address of the server.  This is an
  alternative to `selector` for specifying the target
  server.

- <h4 id="tlssecret">tlsSecret <span class="property-info">string</span></h3>

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  
  This option is used when setting up client-to-router TLS
  encryption.

  _See also:_ [TLS re-encrypt]({{site_prefix}})

- <h4 id="includenotready">includeNotReady <span class="property-info">boolean</span></h3>

  If set, include server pods that are not in the ready
  state.

- <h4 id="type">type <span class="property-info">string</span></h3>

  The connector type.

  _Default:_ `tcp`

</section>

<section>

## Status properties

- <h4 id="status">status <span class="property-info">string</span></h3>

  The current state of the resource.

- <h4 id="active">active <span class="property-info">boolean</span></h3>

</section>
