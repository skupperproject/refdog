# Listener

A [listener][listener] is a local connection endpoint bound to
servers in remote sites.

Each site can have multiple listener definitions.

[listener]: concepts.html#listener

## Examples

A listener in site West for the Hello World backend service
in site East


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
## Spec properties

- **routingKey** _string_

  The identifier used to route traffic from listeners to
  connectors.  To connect to a service at a remote site, the
  listener and connector must have matching routing keys.
  

- **host** _string_

  The hostname or IP address of the local listener.  Clients
  at this site use the listener host and port to
  establish connections to the remote service.
  

- **port** _integer_

  The port of the local listener.  Clients at this site use
  the listener host and port to establish connections to
  the remote service.
  

- **tlsCredentials** _string_

  The name of a Kubernetes secret containing TLS
  credentials.  The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  

- **type** _string_

  _What is this again?  I think we need a qualifier on "type"._
