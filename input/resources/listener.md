---
body_class: resource
links:
  - name: Listener concept
    url: /concepts/listener.html
  - name: Listener create command
    url: /commands/listener-create.html
---

# Listener resource

<section>

A listener binds a connection endpoint in the local site to
target workloads in remote sites.

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

- <h4 id="routingkey">routingKey <span class="property-info">string, required</span></h4>

  The identifier used to route traffic from listeners to
  connectors.  To enable connecting to a service at a
  remote site, the local listener and the remote connector
  must have matching routing keys.

  _See also:_ [Routing key concept]({{site_prefix}}/concepts/routing-key.html)

- <h4 id="host">host <span class="property-info">string, required</span></h4>

  The hostname or IP address of the local listener.  Clients
  at this site use the listener host and port to
  establish connections to the remote service.

- <h4 id="port">port <span class="property-info">integer, required</span></h4>

  The port of the local listener.  Clients at this site use
  the listener host and port to establish connections to
  the remote service.

- <h4 id="tlssecret">tlsSecret <span class="property-info">string</span></h4>

  The name of a Kubernetes secret containing TLS
  credentials.  The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  
  This option is used when setting up router-to-server TLS
  encryption.

  _See also:_ [TLS re-encrypt]({{site_prefix}})

- <h4 id="type">type <span class="property-info">string</span></h4>

  The listener type.

  _Default:_ `tcp`

</section>

<section>

## Status properties

- <h4 id="status">status <span class="property-info">string</span></h4>

  The current state of the resource.

- <h4 id="active">active <span class="property-info">boolean</span></h4>

</section>
