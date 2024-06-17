---
body_class: command
links:
  - name: Listener update command
    url: /commands/listener-update.html
---

# Connector update command

<section>

Update a connector.

</section>

<section>

## Usage

~~~ shell
$ skupper connector update <name> [options]
Waiting for update to complete...
Connector "<name>" is updated.
~~~

</section>

<section>

## Examples

~~~
# Change the workload and port
skupper connector update database --workload deployment/mysql --port 3306

# Change the routing key
skupper connector update backend --routing-key be2

# Produce YAML output
skupper connector update backend --port 9090 --output yaml
~~~

</section>

<section>

## Options

- <h3 id="port">--port <span class="option-info">integer</span></h3>

  The port on the target workload to forward traffic to.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h3 id="output">--output <span class="option-info">string</span></h3>

  Print resources to the console instead of submitting
  them to the Skupper controller.

  | | |
  |-|-|
  | Choices | <table><tr><td><code>json</code></td><td>Produce JSON output</td></tr><tr><td><code>yaml</code></td><td>Produce YAML output</td></tr></table> |
  | Platforms | Kubernetes, Docker |
  
- <h3 id="namespace">--namespace <span class="option-info">string</span></h3>

  Set the namespace.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Namespace concept]({{site_prefix}}/concepts/namespace.html), [Kubernetes namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) |
  
- <h3 id="context">--context <span class="option-info">string</span></h3>

  Set the kubeconfig context.

  | | |
  |-|-|
  | Platforms | Kubernetes |
  | See also | [Kubernetes kubeconfigs](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) |
  
- <h3 id="platform">--platform <span class="option-info">string</span></h3>

  Set the Skupper platform.

  | | |
  |-|-|
  | Choices | <table><tr><td><code>kubernetes</code></td><td>Kubernetes</td></tr><tr><td><code>docker</code></td><td>Docker or Podman</td></tr></table> |
  | Platforms | Kubernetes, Docker |
  | See also | [Platform concept]({{site_prefix}}/concepts/platform.html) |
  
- <h3 id="help">--help <span class="option-info"></span></h3>

  Display help and exit.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
</section>
