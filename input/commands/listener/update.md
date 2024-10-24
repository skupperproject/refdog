---
body_class: object command
links:
  - name: Listener concept
    url: /concepts/listener.html
  - name: Listener resource
    url: /resources/listener.html
  - name: Connector update command
    url: /commands/connector/update.html
---

# Listener update command

<section>

Update a listener.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>Waits for</th><td>Configured</td></table>

</section>

<section>

## Usage

~~~ shell
skupper listener update <name> [options]
~~~

</section>

<section>

## Output

~~~ console
Waiting for update to complete...
Listener "<name>" is configured.
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
skupper listener update backend --port 9090 --output yaml
~~~

</section>

<section>

## Options

- <h3 id="name">name <span class="attribute-info">string, required</span></h3>

  The name of the resource to be updated.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

- <h3 id="port">--port <span class="attribute-info">integer</span></h3>

  The port of the local listener.  Clients at this site use
  the listener host and port to establish connections to
  the remote service.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="output">--output <span class="attribute-info">string</span></h3>

  Print the resource to the console in a structured output format
  instead of submitting it to the Skupper controller.

  <table class="fields"><tr><th>Choices</th><td><table class="choices"><tr><th><code>json</code></th><td><p>Produce JSON output</p>
  </td></tr><tr><th><code>yaml</code></th><td><p>Produce YAML output</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="wait">--wait <span class="attribute-info">string</span></h3>

  Wait for the given status before exiting.

  <table class="fields"><tr><th>Default</th><td><p><code>ready</code></p>
  </td><tr><th>Choices</th><td><table class="choices"><tr><th><code>pending</code></th><td><p>Pending</p>
  </td></tr><tr><th><code>configured</code></th><td><p>Configured</p>
  </td></tr><tr><th><code>ready</code></th><td><p>Ready</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="timeout">--timeout <span class="attribute-info">string (duration)</span></h3>

  Raise an error if the operation does not complete in the given
  period of time.

  <table class="fields"><tr><th>Default</th><td><p><code>60s</code></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

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

- <h3 id="tls-secret">--tls-secret <span class="attribute-info">string</span></h3>

  The name of a Kubernetes secret containing TLS
  credentials.  The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  
  This option is used when setting up router-to-server TLS
  encryption.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="type">--type <span class="attribute-info">string</span></h3>

  The listener type.

  <table class="fields"><tr><th>Default</th><td><p><code>tcp</code></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="namespace">--namespace <span class="attribute-info">string</span></h3>

  Set the namespace.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="/concepts/namespace.html">Namespace concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a></td></table>

- <h3 id="context">--context <span class="attribute-info">string</span></h3>

  Set the kubeconfig context.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/">Kubernetes kubeconfigs</a></td></table>

- <h3 id="kubeconfig">--kubeconfig <span class="attribute-info">string</span></h3>

  Set the path to the kubeconfig file.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/">Kubernetes kubeconfigs</a></td></table>

- <h3 id="platform">--platform <span class="attribute-info">string</span></h3>

  Set the Skupper platform.

  <table class="fields"><tr><th>Choices</th><td><table class="choices"><tr><th><code>kubernetes</code></th><td><p>Kubernetes</p>
  </td></tr><tr><th><code>docker</code></th><td><p>Docker or Podman</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="/concepts/platform.html">Platform concept</a></td></table>

- <h3 id="help">--help <span class="attribute-info"></span></h3>

  Display help and exit.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

</section>
