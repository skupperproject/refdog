---
body_class: object command
links:
  - name: Listener concept
    url: /concepts/listener.html
  - name: Listener resource
    url: /resources/listener.html
  - name: Listener command
    url: /commands/listener.html
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
skupper listener update [options]
~~~

</section>

<section>

## Output

~~~ console
$ skupper listener update [options]
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
skupper listener update backend --port 9090 --output yaml
~~~

</section>

<section>

## Options

- <h3 id="port">--port <span class="attribute-info">integer</span></h3>

  The port of the local listener.  Clients at this site use
  the listener host and port to establish connections to
  the remote service.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="output">--output <span class="attribute-info">string</span></h3>

  Print resources to the console instead of submitting
  them to the Skupper controller.

  <table class="fields"><tr><th>Choices</th><td><table class="choices"><tr><th><code>json</code></th><td><p>Produce JSON output</p>
  </td></tr><tr><th><code>yaml</code></th><td><p>Produce YAML output</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="namespace">--namespace <span class="attribute-info">string</span></h3>

  Set the namespace.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="/concepts/namespace.html">Namespace concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a></td></table>

- <h3 id="context">--context <span class="attribute-info">string</span></h3>

  Set the kubeconfig context.

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
