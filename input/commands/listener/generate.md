---
body_class: object command
links:
  - name: Listener concept
    url: /concepts/listener.html
  - name: Listener resource
    url: /resources/listener.html
---

# Listener generate command

<section>

Generate a Listener resource.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

</section>

<section>

## Usage

~~~ shell
skupper listener generate <name> <port> [options]
~~~

</section>

<section>

## Examples

~~~
# Generate a Listener resource and print it to the console
$ skupper listener generate backend 8080
apiVersion: skupper.io/v2alpha1
kind: Listener
metadata:
  name: backend
spec:
  routingKey: backend
  port: 8080
  host: backend

# Generate a Listener resource and direct the output to a file
$ skupper listener generate backend 8080 > backend.yaml
~~~

</section>

<section>

## Options

- <h3 id="name">name <span class="attribute-info">string, required</span></h3>

  The name of the resource to be generated.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

- <h3 id="port">port <span class="attribute-info">integer, required</span></h3>

  The port of the local listener.  Clients at this site use
  the listener host and port to establish connections to
  the remote service.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="output">--output <span class="attribute-info">string</span></h3>

  Select the output format.

  <table class="fields"><tr><th>Default</th><td><p><code>yaml</code></p>
  </td><tr><th>Choices</th><td><table class="choices"><tr><th><code>json</code></th><td><p>Produce JSON output</p>
  </td></tr><tr><th><code>yaml</code></th><td><p>Produce YAML output</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="routing-key">--routing-key <span class="attribute-info">string</span></h3>

  The identifier used to route traffic from listeners to
  connectors.  To enable connecting to a service at a
  remote site, the local listener and the remote connector
  must have matching routing keys.

  <table class="fields"><tr><th>Default</th><td><p><em>Value of name</em></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="host">--host <span class="attribute-info">string</span></h3>

  The hostname or IP address of the local listener.  Clients
  at this site use the listener host and port to
  establish connections to the remote service.

  <table class="fields"><tr><th>Default</th><td><p><em>Value of name</em></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="tls-credentials">--tls-credentials <span class="attribute-info">string</span></h3>

  The name of a Kubernetes secret containing TLS
  credentials.  The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  
  This option is used when setting up client-to-router TLS
  encryption.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="type">--type <span class="attribute-info">string</span></h3>

  The listener type.

  <table class="fields"><tr><th>Default</th><td><p><code>tcp</code></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="platform">--platform <span class="attribute-info">string</span></h3>

  Set the Skupper platform.

  <table class="fields"><tr><th>Choices</th><td><table class="choices"><tr><th><code>kubernetes</code></th><td><p>Kubernetes</p>
  </td></tr><tr><th><code>docker</code></th><td><p>Docker or Podman</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="/concepts/platform.html">Platform concept</a></td></table>

- <h3 id="help">--help <span class="attribute-info">boolean</span></h3>

  Display help and exit.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

</section>
