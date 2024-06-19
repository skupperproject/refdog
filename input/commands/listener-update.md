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
skupper listener update backend --port 9090 --output yaml
~~~

</section>

<section>

## Options

- <h3 id="port">--port <span class="attribute-info">integer</span></h3>

  The port of the local listener.  Clients at this site use
  the listener host and port to establish connections to
  the remote service.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h3 id="output">--output <span class="attribute-info">string</span></h3>

  Print resources to the console instead of submitting
  them to the Skupper controller.

  | | |
  |-|-|
  | Choices | <table class="choices"><tr><td><code>json</code></td><td>Produce JSON output</td></tr><tr><td><code>yaml</code></td><td>Produce YAML output</td></tr></table> |
  | Platforms | Kubernetes, Docker |
  
- <h3 id="namespace">--namespace <span class="attribute-info">string</span></h3>

  Set the namespace.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Namespace concept]({{site_prefix}}/concepts/namespace.html), [Kubernetes namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) |
  
- <h3 id="context">--context <span class="attribute-info">string</span></h3>

  Set the kubeconfig context.

  | | |
  |-|-|
  | Platforms | Kubernetes |
  | See also | [Kubernetes kubeconfigs](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) |
  
- <h3 id="platform">--platform <span class="attribute-info">string</span></h3>

  Set the Skupper platform.

  | | |
  |-|-|
  | Choices | <table class="choices"><tr><td><code>kubernetes</code></td><td>Kubernetes</td></tr><tr><td><code>docker</code></td><td>Docker or Podman</td></tr></table> |
  | Platforms | Kubernetes, Docker |
  | See also | [Platform concept]({{site_prefix}}/concepts/platform.html) |
  
- <h3 id="help">--help <span class="attribute-info"></span></h3>

  Display help and exit.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
</section>
