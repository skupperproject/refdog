# Connector

A [connector][connector] binds local servers to listeners in
remote sites.

Each site can have multiple connector definitions.

[connector]: concepts.html#connector

## Examples

A connector in site East for the Hello World backend service


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
## Spec properties

- **routingKey** _string_

  The identifier used to route traffic from listeners to
  connectors.  To connect to a service at a remote site, the
  listener and connector must have matching routing keys.
  

- **selector** _string_

  A Kubernetes [label selector][selector] for targeting server
  pods.
  
  [selector]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
  

- **host** _string_

  The hostname or IP address of the server.  This is an
  alternative to `selector` for specifying the target
  server.
  

- **port** _integer_

  The port number of the server listener.
  

- **tlsCredentials** _string_

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  

- **type** _string_

  _What is this again?  I think we need a qualifier on "type"._

- **includeNotReady** _boolean_

  _Default:_ false
