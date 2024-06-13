---
body_class: command
links:
  - name: Connector resource
    url: /resources/connector.html
  - name: connector command
    url: /commands/connector.html
  - name: listener create command
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

- <h3 id="name">name <span class="option-info">string, required</span></h3>

  The name of the connector resource.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h3 id="port">port <span class="option-info">integer, required</span></h3>

  The port on the target workload to forward traffic to.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h3 id="routing-key">--routing-key <span class="option-info">string</span></h3>

  The identifier used to route traffic from listeners to
  connectors.  To expose a local workload to a remote
  site, the remote listener and the local connector must
  have matching routing keys.

  | | |
  |-|-|
  | Default | _Value of name_ |
  | Platforms | Kubernetes, Docker |
  | See also | [Routing key concept]({{site_prefix}}/concepts/routing-key.html) |
  
- <h3 id="selector">--selector <span class="option-info">string</span></h3>

  A Kubernetes label selector for specifying target server
  pods.
  
  On Kubernetes, you usually want to use this.  As an
  alternative, you can use `host`.

  | | |
  |-|-|
  | Default | `app=<value-of-name>` |
  | Platforms | Kubernetes |
  | See also | [Kubernetes label selectors]({{site_prefix}}https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors), [Kubernetes pods]({{site_prefix}}https://kubernetes.io/docs/concepts/workloads/pods/) |
  
- <h3 id="workload">--workload <span class="option-info">string (resource name)</span></h3>

  A Kubernetes resource name that identifies a workload.
  It resolves to an equivalent pod selector.
  
  This is an alternative to setting the `--selector` or
  `--host` options.

  | | |
  |-|-|
  | Platforms | Kubernetes |
  | See also | [Kubernetes workloads]({{site_prefix}}https://kubernetes.io/docs/concepts/workloads/) |
  
- <h3 id="host">--host <span class="option-info">string</span></h3>

  The hostname or IP address of the server.
  
  This is an alternative to setting the `--selector` or
  `--workload` options.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h3 id="tls-secret">--tls-secret <span class="option-info">string</span></h3>

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
  
- <h3 id="type">--type <span class="option-info">string</span></h3>

  The connector type.

  | | |
  |-|-|
  | Default | `tcp` |
  | Platforms | Kubernetes, Docker |
  
- <h3 id="include-not-ready">--include-not-ready <span class="option-info">boolean</span></h3>

  If set, include server pods that are not in the ready
  state.

  | | |
  |-|-|
  | Default | False |
  | Platforms | Kubernetes |
  | See also | [Kubernetes pod lifecycle]({{site_prefix}}https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/) |
  
### Output options

- <h3 id="output">--output <span class="option-info">string</span></h3>

  Print resources to the console instead of submitting
  them to the Skupper controller.

  | | |
  |-|-|
  | Choices | <table><tr><td><code>json</code></td><td>Produce JSON output</td></tr><tr><td><code>yaml</code></td><td>Produce YAML output</td></tr></table> |
  | Platforms | Kubernetes, Docker |
  
### Context options

- <h3 id="namespace">--namespace <span class="option-info">string</span></h3>

  Set the namespace.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Namespace concept]({{site_prefix}}/concepts/namespace.html), [Kubernetes namespaces]({{site_prefix}}https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) |
  
- <h3 id="context">--context <span class="option-info">string</span></h3>

  Set the kubeconfig context.

  | | |
  |-|-|
  | Platforms | Kubernetes |
  | See also | [Kubernetes kubeconfigs]({{site_prefix}}https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) |
  
- <h3 id="platform">--platform <span class="option-info">string</span></h3>

  Set the Skupper platform.

  | | |
  |-|-|
  | Choices | <table><tr><td><code>kubernetes</code></td><td>Kubernetes</td></tr><tr><td><code>docker</code></td><td>Docker or Podman</td></tr></table> |
  | Platforms | Kubernetes, Docker |
  | See also | [Platform concept]({{site_prefix}}/concepts/platform.html) |
  
### Global options

- <h3 id="help">--help <span class="option-info"></span></h3>

  Display help and exit.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
</section>
