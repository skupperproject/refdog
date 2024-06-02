# skupper listener create

Create a listener.

A [listener][listener] is a local connection endpoint bound to
servers in remote sites.

Each site can have multiple listener definitions.

[listener]: concepts.html#listener



## Usage

~~~ shell
$ skupper listener create <name> [options]
Waiting for status...
Listener "<name>" is ready
~~~

## Examples

~~~
# Create a listener for a database
skupper listener create database --host database --port 5432
~~~

## Arguments

- **name** _string_

  The name of the listener resource.
  

- **--routing-key** _string_

  _Default:_ _value of name_

  The identifier used to route traffic from listeners to
  connectors.  To connect to a service at a remote site, the
  listener and connector must have matching routing keys.
  

- **--host** _string_

  The hostname or IP address of the local listener.  Clients
  at this site use the listener host and port to
  establish connections to the remote service.
  

- **--port** _integer_

  The port of the local listener.  Clients at this site use
  the listener host and port to establish connections to
  the remote service.
  

- **--tls-credentials** _string_

  The name of a Kubernetes secret containing TLS
  credentials.  The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  

- **--type** _string_

  _What is this again?  I think we need a qualifier on "type"._
