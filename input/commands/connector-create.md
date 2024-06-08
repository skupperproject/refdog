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

</section>

<section>

## Usage

~~~ shell
$ skupper connector create <name> <port> [options]
Waiting for status...
Connector "<name>" is ready.
~~~

</section>

<section>

## Examples

~~~
# Create a connector for a database
skupper connector create database 5432

# Set the routing key and workload explicitly
skupper connector create backend 8080 --routing-key be1 --workload deployment/backend

# Produce YAML output
skupper connector create backend 8080 --output yaml
~~~

</section>

<section>

## Options

- <h4 id="name">name <span class="argument-info">string, required</span></h3>

  The name of the connector resource.

- <h4 id="port">port <span class="argument-info">integer, required</span></h3>

  The port on the target workload to forward traffic to.

- <h4 id="routing-key">--routing-key <span class="argument-info">string</span></h3>

  The identifier used to route traffic from listeners to
  connectors.  To expose a local workload to a remote
  site, the remote listener and the local connector must
  have matching routing keys.

  _Default:_ _Value of name_

  _See also:_ [Routing key concept]({{site_prefix}}/concepts/routing-key.html)

- <h4 id="selector">--selector <span class="argument-info">string</span></h3>

  A Kubernetes label selector for specifying target pods.

  _Default:_ `app=<value-of-name>`

  _See also:_ [Kubernetes label selectors]({{site_prefix}}https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors), [Kubernetes pods]({{site_prefix}}https://kubernetes.io/docs/concepts/workloads/pods/)

- <h4 id="workload">--workload <span class="argument-info">string (resource name)</span></h3>

  A Kubernetes resource name that identifies a workload.
  It resolves to an equivalent pod selector.
  
  This is an alternative to setting the `--selector` or
  `--host` options.

  _See also:_ [Kubernetes workloads]({{site_prefix}}https://kubernetes.io/docs/concepts/workloads/)

- <h4 id="host">--host <span class="argument-info">string</span></h3>

  The hostname or IP address of the server.
  
  This is an alternative to setting the `--selector` or
  `--workload` options.

- <h4 id="tls-secret">--tls-secret <span class="argument-info">string</span></h3>

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  
  This option is used when setting up client-to-router TLS
  encryption.

  _See also:_ [TLS re-encrypt]({{site_prefix}})

- <h4 id="type">--type <span class="argument-info">string</span></h3>

  The connector type.

  _Default:_ `tcp`

- <h4 id="include-not-ready">--include-not-ready <span class="argument-info">boolean</span></h3>

  If set, include server pods that are not in the ready
  state.

### Output options

- <h4 id="output">--output <span class="argument-info">string</span></h3>

  Print resources to the console instead of submitting
  them to the Skupper controller.

  _Choices:_
  
   - `json` - Produce JSON output
   - `yaml` - Produce YAML output

### Context options

- <h4 id="namespace">--namespace <span class="argument-info">string</span></h3>

  Select the current namespace.

- <h4 id="context">--context <span class="argument-info">string</span></h3>

  Select the current kubeconfig context.

- <h4 id="platform">--platform <span class="argument-info">string</span></h3>

  Select the current Skupper platform.

### Global options

- <h4 id="help">--help <span class="argument-info">None</span></h3>

  Display help and exit.

</section>

<section>

## Errors

</section>
