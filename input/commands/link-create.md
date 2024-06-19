---
body_class: object command
links:
  - name: Link concept
    url: /concepts/link.html
  - name: Link resource
    url: /resources/link.html
  - name: Link command
    url: /commands/link.html
---

# Link create command

<section>

Create a link.

</section>

<section>

## Usage

~~~ shell
$ skupper link create <name> <tls-secret>
Waiting for status...
Link "<name>" is ready.
~~~

</section>

<section>

## Options

- <h3 id="name">name <span class="attribute-info">string, required</span></h3>

  The name of the link.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h3 id="tls-secret">tls-secret <span class="attribute-info">string, required</span></h3>

  The name of a Kubernetes secret containing TLS
  credentials. The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Custom certificates]() |
  
- <h3 id="cost">--cost <span class="attribute-info">integer</span></h3>

  The configured "expense" of sending traffic over the
  link.

  | | |
  |-|-|
  | Default | 1 |
  | Platforms | Kubernetes, Docker |
  | See also | [Load balancing]() |
  
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
