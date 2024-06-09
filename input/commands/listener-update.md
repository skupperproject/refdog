---
body_class: command
links:
  - name: Listener concept
    url: /concepts/listener.html
  - name: Listener resource
    url: /resources/listener.html
  - name: Connector update command
    url: /commands/connector-update.html
---

# Listener update command

<section>

Update a listener.

</section>

<section>

## Usage

~~~ shell
$ skupper listener update <name> [options]
Waiting for update to complete...
Listener "<name>" is updated.
~~~

</section>

<section>

## Examples

~~~
# Change the host and port
skupper listener update database --host mysql --port 3306

# Change the routing key
skupper listener update backend --routing-key be2

# Produce YAML output
skupper listener update frontend --port 9090 --output yaml
~~~

</section>

<section>

## Options

- <h4 id="name">name <span class="argument-info">string, required</span></h4>

  The name of the listener resource.

- <h4 id="port">--port <span class="argument-info">integer</span></h4>

  The port of the local listener.  Clients at this site use
  the listener host and port to establish connections to
  the remote service.

- <h4 id="routing-key">--routing-key <span class="argument-info">string</span></h4>

  The identifier used to route traffic from listeners to
  connectors.  To enable connecting to a service at a
  remote site, the local listener and the remote connector
  must have matching routing keys.

  _Default:_ _Value of name_

  _See also:_ [Routing key concept]({{site_prefix}}/concepts/routing-key.html)

- <h4 id="host">--host <span class="argument-info">string</span></h4>

  The hostname or IP address of the local listener.  Clients
  at this site use the listener host and port to
  establish connections to the remote service.

  _Default:_ _Value of name_

- <h4 id="tls-secret">--tls-secret <span class="argument-info">string</span></h4>

  The name of a Kubernetes secret containing TLS
  credentials.  The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  
  This option is used when setting up router-to-server TLS
  encryption.

  _See also:_ [TLS re-encrypt]({{site_prefix}})

- <h4 id="type">--type <span class="argument-info">string</span></h4>

  The listener type.

  _Default:_ `tcp`

### Output options

- <h4 id="output">--output <span class="argument-info">string</span></h4>

  Print resources to the console instead of submitting
  them to the Skupper controller.

  _Choices:_
  
   - `json` - Produce JSON output
   - `yaml` - Produce YAML output

### Context options

- <h4 id="namespace">--namespace <span class="argument-info">string</span></h4>

  Select the current namespace.

- <h4 id="context">--context <span class="argument-info">string</span></h4>

  Select the current kubeconfig context.

- <h4 id="platform">--platform <span class="argument-info">string</span></h4>

  Select the current Skupper platform.

### Global options

- <h4 id="help">--help <span class="argument-info">None</span></h4>

  Display help and exit.

</section>

<section>

## Errors

</section>
