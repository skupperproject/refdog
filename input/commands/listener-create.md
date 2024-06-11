---
body_class: command
links:
  - name: Listener concept
    url: /concepts/listener.html
  - name: Listener resource
    url: /resources/listener.html
  - name: listener command
    url: /commands/listener.html
  - name: connector create command
    url: /commands/connector-create.html
---

# listener create command

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
skupper listener create frontend 8080 --output yaml
~~~

</section>

<section>

## Options

- <h4 id="name">name <span class="option-info">string, required</span></h4>

  The name of the listener resource.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h4 id="port">port <span class="option-info">integer, required</span></h4>

  The port of the local listener.  Clients at this site use
  the listener host and port to establish connections to
  the remote service.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h4 id="routing-key">--routing-key <span class="option-info">string</span></h4>

  The identifier used to route traffic from listeners to
  connectors.  To enable connecting to a service at a
  remote site, the local listener and the remote connector
  must have matching routing keys.

  | | |
  |-|-|
  | Default | _Value of name_ |
  | Platforms | Kubernetes, Docker |
  | See also | [Routing key concept]({{site_prefix}}/concepts/routing-key.html) |
  
- <h4 id="host">--host <span class="option-info">string</span></h4>

  The hostname or IP address of the local listener.  Clients
  at this site use the listener host and port to
  establish connections to the remote service.

  | | |
  |-|-|
  | Default | _Value of name_ |
  | Platforms | Kubernetes, Docker |
  
- <h4 id="tls-secret">--tls-secret <span class="option-info">string</span></h4>

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
  | See also | [TLS re-encrypt]({{site_prefix}}) |
  
- <h4 id="type">--type <span class="option-info">string</span></h4>

  The listener type.

  | | |
  |-|-|
  | Default | `tcp` |
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
