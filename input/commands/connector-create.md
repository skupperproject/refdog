---
body_class: command
links:
  - name: Connector concept
    url: /concepts/connector.html
  - name: Connector resource
    url: /resources/connector.html
  - name: Listener create command
    url: /commands/listener-create.html
---

# Connector create command

<section>

Create a connector.

A connector binds local servers to listeners in remote
sites.

Theses:

  - A connector targets a workload in the local site (or
    reachable on the local network).
  - A connector forwards connections from matching listeners
    at remote sites to the workload in the local site.

Each site can have multiple connector resources.

When creating a connector, you must supply a target workload
using the `--workload`, `--selector`, or `--host` options.

</section>

<section>

## Usage

~~~ shell
$ skupper connector create <name> <port> [options]
Waiting for status...
Connector "<name>" is ready
~~~

</section>

<section>

## Examples

~~~
# Create a connector for a database
skupper connector create database 5432 --workload deployment/postgresql

# Set the routing key explicitly
skupper connector create backend 8080 --workload deployment/backend --routing-key be1

# Produce YAML output
skupper connector create frontend 8080 --workload deployment/frontend --output yaml
~~~

</section>

<section>

## Arguments

- <h3 id="name">name <span class="argument-info">string, required</span></h3>

  The name of the connector resource.
  
  The name also serves as the default routing key if the
  `--routing-key` option is not set.

- <h3 id="port">port <span class="argument-info">integer, required</span></h3>

  The port number the target workload is listening on.

- <h3 id="--routing-key">--routing-key <span class="argument-info">string</span></h3>

  The identifier used to route traffic from listeners to
  connectors.  To expose a local workload to a remote
  site, the remote listener and the local connector must
  have matching routing keys.

  _Default:_ _Value of name_

  _See also:_ [Routing key concept]({{site_prefix}}/concepts/routing-key.html)

- <h3 id="--selector">--selector <span class="argument-info">string</span></h3>

  A Kubernetes label selector for targeting server pods.
  
  This is an alternative to setting the `--workload` or
  `--host` options.

  _See also:_ [Kubernetes label selectors]({{site_prefix}}https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors), [Kubernetes pods]({{site_prefix}}https://kubernetes.io/docs/concepts/workloads/pods/)

- <h3 id="--workload">--workload <span class="argument-info">string (<code>&lt;resource-kind&gt;/&lt;resource-name&gt;</code>)</span></h3>

  A Kubernetes resource name that identifies a workload.
  It resolves to an equivalent pod selector.
  
  This is an alternative to setting the `--selector` or
  `--host` options.

  _See also:_ [Kubernetes workloads]({{site_prefix}}https://kubernetes.io/docs/concepts/workloads/)

- <h3 id="--host">--host <span class="argument-info">string</span></h3>

  The hostname or IP address of the server.
  
  This is an alternative to setting the `--selector` or
  `--workload` options.

- <h3 id="--tls-secret">--tls-secret <span class="argument-info">string</span></h3>

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  
  This option is used when setting up client-to-router TLS
  encryption.

  _See also:_ [TLS re-encrypt]({{site_prefix}})

- <h3 id="--type">--type <span class="argument-info">string</span></h3>

  The connector type.

  _Default:_ `tcp`

- <h3 id="--include-not-ready">--include-not-ready <span class="argument-info">boolean</span></h3>

  If set, include server pods that are not in the ready
  state.

- <h3 id="--output">--output <span class="argument-info">string</span></h3>

  Print resources to the console instead of submitting
  them to the Skupper controller.

  _Choices:_
  
   - `json` - Produce JSON output
   - `yaml` - Produce YAML output

</section>
