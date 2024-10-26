---
body_class: object command
links:
  - name: Connector concept
    url: /concepts/connector.html
  - name: Connector resource
    url: /resources/connector.html
  - name: Listener update command
    url: /commands/listener/update.html
---

# Connector update command

<section>

Update a connector.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>Waits for</th><td>Configured</td></table>

</section>

<section>

## Usage

~~~ shell
skupper connector update <name> <port> [options]
~~~

</section>

<section>

## Examples

~~~
# Change the workload and port
$ skupper connector update database --workload deployment/mysql --port 3306
Waiting for status...
Connector "database" is configured.

# Change the routing key
$ skupper connector update backend --routing-key be2
~~~

</section>

<section>

## Options

- <h3 id="name">name <span class="attribute-info">string, required</span></h3>

  The name of the resource to be updated.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

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

- <h3 id="port">port <span class="attribute-info">integer, required</span></h3>

  The port on the target workload to forward traffic to.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="routing-key">--routing-key <span class="attribute-info">string</span></h3>

  The identifier used to route traffic from listeners to
  connectors.  To expose a local workload to a remote
  site, the remote listener and the local connector must
  have matching routing keys.

  <table class="fields"><tr><th>Default</th><td><p><em>Value of name</em></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="host">--host <span class="attribute-info">string</span></h3>

  The hostname or IP address of the server.  This is an
  alternative to `selector` for specifying the target
  server.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="type">--type <span class="attribute-info">string</span></h3>

  The connector type.

  <table class="fields"><tr><th>Default</th><td><p><code>tcp</code></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="tls-credentials">--tls-credentials <span class="attribute-info">string</span></h3>

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  
  This option is used when setting up router-to-server TLS
  encryption.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="selector">--selector <span class="attribute-info">string</span></h3>

  A Kubernetes label selector for specifying target server
  pods.
  
  On Kubernetes, you usually want to use this.  As an
  alternative, you can use `host`.

  <table class="fields"><tr><th>Default</th><td><p><code>app=[value-of-name]</code></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="workload">--workload <span class="attribute-info">string (resource name)</span></h3>

  A Kubernetes resource name that identifies a workload.
  It resolves to an equivalent pod selector.
  
  This is an alternative to setting the `--selector` or
  `--host` options.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/workloads/">Kubernetes workloads</a></td></table>

- <h3 id="include-not-ready">--include-not-ready <span class="attribute-info">boolean</span></h3>

  If set, include server pods that are not in the ready
  state.

  <table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

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

- <h3 id="help">--help <span class="attribute-info">boolean</span></h3>

  Display help and exit.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

</section>
