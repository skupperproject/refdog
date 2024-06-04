---
body_class: command
links:
  - name: Listener resource
    url: /resources/listener.html
---

# skupper listener create

<section>

Create a listener.

A listener is a local connection endpoint bound to servers
in remote sites.

Each site can have multiple listener definitions.

</section>

<section>

## Usage

~~~ shell
$ skupper listener create <name> [options]
Waiting for status...
Listener "<name>" is ready
~~~

</section>

<section>

## Examples

~~~
# Create a listener for a database
skupper listener create database --host database --port 5432
~~~

</section>

<section>

## Arguments

- <h3 id="name">name <span class="argument-info">string</span></h3>

  The name of the listener resource.

- <h3 id="--routing-key">--routing-key <span class="argument-info">string</span></h3>

  The identifier used to route traffic from listeners to
  connectors.  To connect to a service at a remote site, the
  listener and connector must have matching routing keys.

  _Default:_ _value of name_

- <h3 id="--host">--host <span class="argument-info">string, required</span></h3>

  The hostname or IP address of the local listener.  Clients
  at this site use the listener host and port to
  establish connections to the remote service.

- <h3 id="--port">--port <span class="argument-info">integer, required</span></h3>

  The port of the local listener.  Clients at this site use
  the listener host and port to establish connections to
  the remote service.

- <h3 id="--tls-secret">--tls-secret <span class="argument-info">string</span></h3>

  The name of a Kubernetes secret containing TLS
  credentials.  The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.

- <h3 id="--type">--type <span class="argument-info">string</span></h3>

  What is this again?  I think we need a qualifier on "type".

</section>
