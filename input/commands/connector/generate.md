---
body_class: object command
links:
  - name: Connector concept
    url: /concepts/connector.html
  - name: Connector resource
    url: /resources/connector.html
---

# Connector generate command

<section>

Generate a Connector resource.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

</section>

<section>

## Usage

~~~ shell
skupper connector generate <name> <port> [options]
~~~

</section>

<section>

## Examples

~~~ console
# Generate a Connector resource and print it to the console
$ skupper connector generate backend 8080
apiVersion: skupper.io/v2alpha1
kind: Connector
metadata:
  name: backend
spec:
  routingKey: backend
  port: 8080
  selector: app=backend

# Generate a Connector resource and direct the output to a file
$ skupper connector generate backend 8080 > backend.yaml
~~~

</section>

<section>

## Options

- <div class="attribute"><h3 id="option-name">&lt;name&gt;</h3><div>string, required</div></div>

  The name of the resource to be generated.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

- <div class="attribute"><h3 id="option-port">&lt;port&gt;</h3><div>integer, required</div></div>

  The port on the target workload to forward traffic to.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <div class="attribute"><h3 id="option-output">--output</h3><div>&lt;string&gt;</div></div>

  Select the output format.

  <table class="fields"><tr><th>Default</th><td><p><code>yaml</code></p>
  </td><tr><th>Choices</th><td><table class="choices"><tr><th><code>json</code></th><td><p>Produce JSON output</p>
  </td></tr><tr><th><code>yaml</code></th><td><p>Produce YAML output</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <div class="attribute"><h3 id="option-routing-key">--routing-key</h3><div>&lt;string&gt;</div></div>

  The identifier used to route traffic from listeners to
  connectors.  To expose a local workload to a remote
  site, the remote listener and the local connector must
  have matching routing keys.

  <table class="fields"><tr><th>Default</th><td><p><em>Value of name</em></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <div class="attribute"><h3 id="option-host">--host</h3><div>&lt;string&gt;</div></div>

  The hostname or IP address of the server.  This is an
  alternative to `selector` for specifying the target
  server.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <div class="attribute"><h3 id="option-type">--type</h3><div>&lt;string&gt;</div></div>

  The connector type.

  <table class="fields"><tr><th>Default</th><td><p><code>tcp</code></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <div class="attribute"><h3 id="option-tls-credentials">--tls-credentials</h3><div>&lt;string&gt;</div></div>

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  
  This option is used when setting up router-to-server TLS
  encryption.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <div class="attribute"><h3 id="option-selector">--selector</h3><div>&lt;string&gt;</div></div>

  A Kubernetes label selector for specifying target server
  pods.
  
  On Kubernetes, you usually want to use this.  As an
  alternative, you can use `host`.

  <table class="fields"><tr><th>Default</th><td><p><code>app=[value-of-name]</code></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <div class="attribute"><h3 id="option-workload">--workload</h3><div>&lt;string&gt; (resource name)</div></div>

  A Kubernetes resource name that identifies a workload.
  It resolves to an equivalent pod selector.
  
  This is an alternative to setting the `--selector` or
  `--host` options.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/workloads/">Kubernetes workloads</a></td></table>

- <div class="attribute"><h3 id="option-include-not-ready">--include-not-ready</h3><div>boolean</div></div>

  If set, include server pods that are not in the ready
  state.

  <table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <div class="attribute"><h3 id="option-platform">--platform</h3><div>&lt;string&gt;</div></div>

  Set the Skupper platform.

  <table class="fields"><tr><th>Default</th><td><p><code>kubernetes</code></p>
  </td><tr><th>Choices</th><td><table class="choices"><tr><th><code>kubernetes</code></th><td><p>Kubernetes</p>
  </td></tr><tr><th><code>docker</code></th><td><p>Docker</p>
  </td></tr><tr><th><code>podman</code></th><td><p>Podman</p>
  </td></tr><tr><th><code>systemd</code></th><td><p>Systemd</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="/concepts/platform.html">Platform concept</a></td></table>

- <div class="attribute"><h3 id="option-help">--help (-h)</h3><div>boolean</div></div>

  Display help and exit.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

</section>
