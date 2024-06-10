---
body_class: command
links:
  - name: Listener concept
    url: /concepts/listener.html
  - name: Listener resource
    url: /resources/listener.html
  - name: Listener command
    url: /commands/listener.html
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
skupper listener create frontend 8080 --output yaml
~~~

</section>

<section>

## Options

- <h4 id="name">name <span class="option-info">string, required</span></h4>

  The name of the listener resource.

- <h4 id="port">port <span class="option-info">integer, required</span></h4>

  The port of the local listener.  Clients at this site use
  the listener host and port to establish connections to
  the remote service.

- <h4 id="routing-key">--routing-key <span class="option-info">string</span></h4>

  The identifier used to route traffic from listeners to
  connectors.  To enable connecting to a service at a
  remote site, the local listener and the remote connector
  must have matching routing keys.

  _Default:_ _Value of name_

  _See also:_ [Routing key concept]({{site_prefix}}/concepts/routing-key.html)

- <h4 id="host">--host <span class="option-info">string</span></h4>

  The hostname or IP address of the local listener.  Clients
  at this site use the listener host and port to
  establish connections to the remote service.

  _Default:_ _Value of name_

- <h4 id="tls-secret">--tls-secret <span class="option-info">string</span></h4>

  The name of a Kubernetes secret containing TLS
  credentials.  The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  
  This option is used when setting up router-to-server TLS
  encryption.

  _See also:_ [TLS re-encrypt]({{site_prefix}})

- <h4 id="type">--type <span class="option-info">string</span></h4>

  The listener type.

  _Default:_ `tcp`

### Output options

- <h4 id="output">--output <span class="option-info">string</span></h4>

  Print resources to the console instead of submitting
  them to the Skupper controller.

  _Choices:_
  
   - `json` - Produce JSON output
   - `yaml` - Produce YAML output

### Context options

- <h4 id="namespace">--namespace <span class="option-info">string</span></h4>

  Select the current namespace.

- <h4 id="context">--context <span class="option-info">string</span></h4>

  Select the current kubeconfig context.

- <h4 id="platform">--platform <span class="option-info">string</span></h4>

  Select the current Skupper platform.

### Global options

- <h4 id="help">--help <span class="option-info">None</span></h4>

  Display help and exit.

</section>
