---
body_class: resource
---

# Listener

<section>

@concept_description@

Each site can have multiple listener definitions.

</section>

<section>

## Examples

A listener in site West for the Hello World backend service
in site East:

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Listener
metadata:
  name: backend
  namespace: hello-world-west
spec:
  routingKey: backend
  port: 8080
  host: backend
~~~

</section>

<section>

## Spec properties

- <h3 id="routingkey">routingKey <span class="property-info">string, required</span></h3>

  The identifier used to route traffic from listeners to
  connectors.  To connect to a service at a remote site, the
  listener and connector must have matching routing keys.

- <h3 id="host">host <span class="property-info">string, required</span></h3>

  The hostname or IP address of the local listener.  Clients
  at this site use the listener host and port to
  establish connections to the remote service.

- <h3 id="port">port <span class="property-info">integer, required</span></h3>

  The port of the local listener.  Clients at this site use
  the listener host and port to establish connections to
  the remote service.

- <h3 id="tlssecret">tlsSecret <span class="property-info">string</span></h3>

  The name of a Kubernetes secret containing TLS
  credentials.  The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.

- <h3 id="type">type <span class="property-info">string</span></h3>

  _What is this again?  I think we need a qualifier on "type"._

</section>

<section>

## Status properties

- <h3 id="active">active <span class="property-info">boolean</span></h3>

- <h3 id="status">status <span class="property-info">string</span></h3>

</section>
