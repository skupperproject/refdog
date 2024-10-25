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

Generate a connector resource and print it to the console.

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

~~~
# Print a connector resource to the console
$ skupper connector generate backend 8080
apiVersion: skupper.io/v2alpha1
kind: Connector
metadata:
  name: backend
spec:
  routingKey: backend
  port: 8080
  selector: app=backend

# Direct the output to a file
$ skupper connector generate backend 8080 > backend.yaml
~~~

</section>

<section>

## Options

- <h3 id="name">name <span class="attribute-info">string, required</span></h3>

  The name of the resource to be generated.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

- <h3 id="port">port <span class="attribute-info">integer, required</span></h3>

  The port on the target workload to forward traffic to.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="output">--output <span class="attribute-info">string</span></h3>

  Select the output format.

  <table class="fields"><tr><th>Default</th><td><p><code>yaml</code></p>
  </td><tr><th>Choices</th><td><table class="choices"><tr><th><code>json</code></th><td><p>Produce JSON output</p>
  </td></tr><tr><th><code>yaml</code></th><td><p>Produce YAML output</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

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

- <h3 id="platform">--platform <span class="attribute-info">string</span></h3>

  Set the Skupper platform.

  <table class="fields"><tr><th>Choices</th><td><table class="choices"><tr><th><code>kubernetes</code></th><td><p>Kubernetes</p>
  </td></tr><tr><th><code>docker</code></th><td><p>Docker or Podman</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="/concepts/platform.html">Platform concept</a></td></table>

- <h3 id="help">--help <span class="attribute-info">boolean</span></h3>

  Display help and exit.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

</section>
