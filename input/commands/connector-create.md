---
body_class: command
links:
  - name: Connector resource
    url: /resources/connector.html
---

# Connector create command

<section>

Create a connector.

A connector binds local servers to listeners in remote
sites.

Each site can have multiple connector definitions.

</section>

<section>

## Usage

~~~ shell
$ skupper connector create <name> [options]
Waiting for status...
Connector "<name>" is ready
~~~

</section>

<section>

## Examples

~~~
# Create a connector for a database
skupper connector create database --workload deployment/postgresql --port 5432
~~~

</section>

<section>

## Arguments

- <h3 id="name">name <span class="argument-info">string, required</span></h3>

  The name of the connector resource.

- <h3 id="--routing-key">--routing-key <span class="argument-info">string</span></h3>

  The identifier used to route traffic from listeners to
  connectors.  To connect to a service at a remote site, the
  listener and connector must have matching routing keys.

  _Default:_ _value of name_

- <h3 id="--workload">--workload <span class="argument-info">string</span></h3>

  A Kubernetes resource name that identifies a workload.
  This resolves to an equivalent label selector and
  servers as an alternative to setting the host or
  selector options.

- <h3 id="--port">--port <span class="argument-info">integer, required</span></h3>

  The port number of the server listener.

- <h3 id="--selector">--selector <span class="argument-info">string</span></h3>

  A Kubernetes label selector for targeting server pods.

- <h3 id="--host">--host <span class="argument-info">string</span></h3>

  The hostname or IP address of the server.  This is an
  alternative to `selector` for specifying the target
  server.

- <h3 id="--tls-secret">--tls-secret <span class="argument-info">string</span></h3>

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  
  This option is used when setting up client-to-router TLS
  encryption.

- <h3 id="--type">--type <span class="argument-info">string</span></h3>

  The connector type.

  _Default:_ `tcp`

- <h3 id="--include-not-ready">--include-not-ready <span class="argument-info">boolean</span></h3>

  If set, include server pods that are not in the ready
  state.

- <h3 id="--output">--output <span class="argument-info">string</span></h3>

  _Choices:_
  
   - `json` - JSON
   - `yaml` - YAML

</section>
