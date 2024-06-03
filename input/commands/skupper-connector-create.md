---
body_class: command
---

# skupper connector create

Create a connector.

A connector binds local servers to listeners in remote
sites.

Each site can have multiple connector definitions.

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

- <h3 id="name">name <span class="argument-info">string, required</span></h3>

  The name of the connector resource.

- <h3 id="--routing-key">--routing-key <span class="argument-info">string</span></h3>

  The identifier used to route traffic from listeners to
  connectors.  To connect to a service at a remote site, the
  listener and connector must have matching routing keys.

  _Default:_ _value of name_

- <h3 id="--workload">--workload <span class="argument-info">string</span></h3>

- <h3 id="--port">--port <span class="argument-info">integer, required</span></h3>

  The port number of the server listener.

- <h3 id="--selector">--selector <span class="argument-info">string</span></h3>

  A Kubernetes label selector for targeting server pods.

- <h3 id="--host">--host <span class="argument-info">string</span></h3>

  The hostname or IP address of the server.  This is an
  alternative to `selector` for specifying the target
  server.

- <h3 id="--tls-credentials">--tls-credentials <span class="argument-info">string</span></h3>

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.

- <h3 id="--type">--type <span class="argument-info">string</span></h3>

  _What is this again?  I think we need a qualifier on "type"._

- <h3 id="--include-not-ready">--include-not-ready <span class="argument-info">boolean</span></h3>

  _Default:_ false
