---
body_class: command
links:
  - name: Connector create command
    url: /commands/connector-create.html
---

# Listener create command

<section>

Create a listener.

</section>

<section>

## Usage

~~~ shell
$ skupper listener create <name> <port> [options]
Waiting for status...
Listener "<name>" is ready.
~~~

</section>

<section>

## Examples

~~~
# Create a listener for a database
skupper listener create database 5432

# Set the routing key and host explicitly
skupper listener create backend 8080 --routing-key be1 --host apiserver

# Produce YAML output
skupper listener create backend 8080 --output yaml
~~~

</section>

<section>

## Options

- <h3 id="name">name <span class="option-info">string, required</span></h3>

  The name of the listener resource.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h3 id="port">port <span class="option-info">integer, required</span></h3>

  The port of the local listener.  Clients at this site use
  the listener host and port to establish connections to
  the remote service.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h3 id="routing-key">--routing-key <span class="option-info">string</span></h3>

  The identifier used to route traffic from listeners to
  connectors.  To enable connecting to a service at a
  remote site, the local listener and the remote connector
  must have matching routing keys.

  | | |
  |-|-|
  | Default | _Value of name_ |
  | Platforms | Kubernetes, Docker |
  | See also | [Routing key concept]({{site_prefix}}/concepts/routing-key.html) |
  
- <h3 id="host">--host <span class="option-info">string</span></h3>

  The hostname or IP address of the local listener.  Clients
  at this site use the listener host and port to
  establish connections to the remote service.

  | | |
  |-|-|
  | Default | _Value of name_ |
  | Platforms | Kubernetes, Docker |
  
- <h3 id="tls-secret">tls-secret <span class="option-info">string, optional</span></h3>

  The name of a Kubernetes secret containing TLS
  credentials.  The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  
  This option is used when setting up router-to-server TLS
  encryption.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Site-scoped TLS]() |
  
- <h3 id="type">--type <span class="option-info">string</span></h3>

  The listener type.

  | | |
  |-|-|
  | Default | `tcp` |
  | Platforms | Kubernetes, Docker |
  
- <h3 id="output">--output <span class="option-info">string</span></h3>

  Print resources to the console instead of submitting
  them to the Skupper controller.

  | | |
  |-|-|
  | Choices | <table><tr><td><code>json</code></td><td>Produce JSON output</td></tr><tr><td><code>yaml</code></td><td>Produce YAML output</td></tr></table> |
  | Platforms | Kubernetes, Docker |
  
- <h3 id="namespace">--namespace <span class="option-info">string</span></h3>

  Set the namespace.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Namespace concept]({{site_prefix}}/concepts/namespace.html), [Kubernetes namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) |
  
- <h3 id="context">--context <span class="option-info">string</span></h3>

  Set the kubeconfig context.

  | | |
  |-|-|
  | Platforms | Kubernetes |
  | See also | [Kubernetes kubeconfigs](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) |
  
- <h3 id="platform">--platform <span class="option-info">string</span></h3>

  Set the Skupper platform.

  | | |
  |-|-|
  | Choices | <table><tr><td><code>kubernetes</code></td><td>Kubernetes</td></tr><tr><td><code>docker</code></td><td>Docker or Podman</td></tr></table> |
  | Platforms | Kubernetes, Docker |
  | See also | [Platform concept]({{site_prefix}}/concepts/platform.html) |
  
- <h3 id="help">--help <span class="option-info"></span></h3>

  Display help and exit.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
</section>
