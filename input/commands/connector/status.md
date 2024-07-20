---
body_class: object command
links:
  - name: Connector concept
    url: /concepts/connector.html
  - name: Connector resource
    url: /resources/connector.html
  - name: Connector command
    url: /commands/connector.html
---

# Connector status command

<section>

Display the status of connectors in the current site.

</section>

<section>

## Usage

~~~ shell
skupper connector status [name] [options]
~~~

</section>

<section>

## Output

~~~ console
$ skupper connector status
NAME       STATUS   ROUTING-KEY   SELECTOR         HOST     PORT   LISTENERS
backend    Ready    backend       app=backend      <none>   8080   1
database   Ready    database      app=postgresql   <none>   5432   1

$ skupper connector status backend
Name:         backend
Status:       Ready
Routing key:  backend
Selector:     app=backend
Host:         <none>
Port:         8080
Listeners:    1
~~~

</section>

<section>

## Options

- <h3 id="name">name <span class="attribute-info">string, optional</span></h3>

  An optional resource name.  If set, the status command reports
  status for the named resource only.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

- <h3 id="output">--output <span class="attribute-info">string</span></h3>

  Print status to the console in a structured output format.

  <table class="fields"><tr><th>Choices</th><td><table class="choices"><tr><th><code>json</code></th><td><p>Produce JSON output</p>
  </td></tr><tr><th><code>yaml</code></th><td><p>Produce YAML output</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="timeout">--timeout <span class="attribute-info">string (duration)</span></h3>

  Raise an error if the operation does not complete in the given
  period of time.

  <table class="fields"><tr><th>Default</th><td><p><code>60s</code></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="namespace">--namespace <span class="attribute-info">string</span></h3>

  Set the namespace.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="/concepts/namespace.html">Namespace concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a></td></table>

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
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="/concepts/platform.html">Platform concept</a></td></table>

- <h3 id="help">--help <span class="attribute-info"></span></h3>

  Display help and exit.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

</section>
