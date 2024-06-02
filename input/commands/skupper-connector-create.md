# skupper connector create

Create a connector.

A [connector][connector] binds local servers to listeners in
remote sites.

Each site can have multiple connector definitions.

[connector]: concepts.html#connector



## Usage

~~~ shell
$ skupper connector create <name> [options]
Waiting for status...
Connector "<name>" is ready
~~~

## Examples

~~~
# Create a connector for a database
skupper connector create database --workload deployment/postgresql --port 5432
~~~

## Arguments

- **name** _string_

  The name of the connector resource.
  

- **--routing-key** _string_

  _Default:_ _value of name_

  The identifier used to route traffic from listeners to
  connectors.  To connect to a service at a remote site, the
  listener and connector must have matching routing keys.
  

- **--workload** _string_

- **--port** _integer_

  The port number of the server listener.
  

- **--selector** _string_

  A Kubernetes [label selector][selector] for targeting server
  pods.
  
  [selector]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
  

- **--host** _string_

  The hostname or IP address of the server.  This is an
  alternative to `selector` for specifying the target
  server.
  

- **--tls-credentials** _string_

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  

- **--type** _string_

  _What is this again?  I think we need a qualifier on "type"._

- **--include-not-ready** _boolean_

  _Default:_ false
