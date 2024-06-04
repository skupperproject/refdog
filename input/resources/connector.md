---
body_class: resource
---

# Connector

<section>

A connector binds local servers to listeners in remote
sites.


Each site can have multiple connector definitions.

_See also:_ [Skupper connector command]({{site_prefix}}/commands/skupper-connector.html)

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
  connectors.  To connect to a service at a remote site, the
  listener and connector must have matching routing keys.

- <h3 id="port">port <span class="property-info">integer, required</span></h3>

  The port number of the server listener.

- <h3 id="selector">selector <span class="property-info">string</span></h3>

  A Kubernetes label selector for targeting server pods.

  _See also:_ [Kubernetes label selectors]({{site_prefix}}https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors)

- <h3 id="host">host <span class="property-info">string</span></h3>

  The hostname or IP address of the server.  This is an
  alternative to `selector` for specifying the target
  server.

- <h3 id="tlssecret">tlsSecret <span class="property-info">string</span></h3>

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.

- <h3 id="type">type <span class="property-info">string</span></h3>

  What is this again?  I think we need a qualifier on "type".

- <h3 id="includenotready">includeNotReady <span class="property-info">boolean</span></h3>

</section>

<section>

## Status properties

- <h3 id="active">active <span class="property-info">boolean</span></h3>

- <h3 id="status">status <span class="property-info">string</span></h3>

</section>
