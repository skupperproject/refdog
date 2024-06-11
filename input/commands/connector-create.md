---
body_class: command
links:
  - name: Connector concept
    url: /concepts/connector.html
  - name: Connector resource
    url: /resources/connector.html
  - name: connector command
    url: /commands/connector.html
  - name: Listener create command
    url: /commands/listener-create.html
---

# connector create command

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

- <h4 id="name">name <span class="option-info">string, required</span></h4>

  The name of the connector resource.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h4 id="port">port <span class="option-info">integer, required</span></h4>

  The port on the target workload to forward traffic to.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h4 id="routing-key">--routing-key <span class="option-info">string</span></h4>

  The identifier used to route traffic from listeners to
  connectors.  To expose a local workload to a remote
  site, the remote listener and the local connector must
  have matching routing keys.

  | | |
  |-|-|
  | Default | _Value of name_ |
  | Platforms | Kubernetes, Docker |
  | See also | [Routing key concept]({{site_prefix}}/concepts/routing-key.html) |
  
- <h4 id="selector">--selector <span class="option-info">string</span></h4>

  A Kubernetes label selector for specifying target server
  pods.
  
  On Kubernetes, you usually want to use this.  As an
  alternative, you can use `host`.

  | | |
  |-|-|
  | Default | `app=<value-of-name>` |
  | Platforms | Kubernetes, Docker |
  | See also | [Kubernetes label selectors]({{site_prefix}}https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors), [Kubernetes pods]({{site_prefix}}https://kubernetes.io/docs/concepts/workloads/pods/) |
  
- <h4 id="workload">--workload <span class="option-info">string (resource name)</span></h4>

  A Kubernetes resource name that identifies a workload.
  It resolves to an equivalent pod selector.
  
  This is an alternative to setting the `--selector` or
  `--host` options.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Kubernetes workloads]({{site_prefix}}https://kubernetes.io/docs/concepts/workloads/) |
  
- <h4 id="host">--host <span class="option-info">string</span></h4>

  The hostname or IP address of the server.
  
  This is an alternative to setting the `--selector` or
  `--workload` options.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h4 id="tls-secret">--tls-secret <span class="option-info">string</span></h4>

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  
  This option is used when setting up client-to-router TLS
  encryption.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [TLS re-encrypt]({{site_prefix}}) |
  
- <h4 id="type">--type <span class="option-info">string</span></h4>

  The connector type.

  | | |
  |-|-|
  | Default | `tcp` |
  | Platforms | Kubernetes, Docker |
  
- <h4 id="include-not-ready">--include-not-ready <span class="option-info">boolean</span></h4>

  If set, include server pods that are not in the ready
  state.

  | | |
  |-|-|
  | Default | False |
  | Platforms | Kubernetes, Docker |
  
### Output options

- <h4 id="output">--output <span class="option-info">string</span></h4>

  Print resources to the console instead of submitting
  them to the Skupper controller.

  | | |
  |-|-|
  | Choices | <table><tr><td><code>json</code></td><td>Produce JSON output</td></tr><tr><td><code>yaml</code></td><td>Produce YAML output</td></tr></table> |
  | Platforms | Kubernetes, Docker |
  
### Context options

- <h4 id="namespace">--namespace <span class="option-info">string</span></h4>

  Select the current namespace.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h4 id="context">--context <span class="option-info">string</span></h4>

  Select the current kubeconfig context.

  | | |
  |-|-|
  | Platforms | Kubernetes |
  
- <h4 id="platform">--platform <span class="option-info">string</span></h4>

  Set the Skupper platform.

  | | |
  |-|-|
  | Choices | <table><tr><td><code>kubernetes</code></td><td>Kubernetes</td></tr><tr><td><code>docker</code></td><td>Docker or Podman</td></tr></table> |
  | Platforms | Kubernetes, Docker |
  
### Global options

- <h4 id="help">--help <span class="option-info"></span></h4>

  Display help and exit.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
</section>
