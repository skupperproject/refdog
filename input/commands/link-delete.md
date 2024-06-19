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

# Link delete command

<section>

Delete a link.

</section>

<section>

## Usage

~~~ shell
$ skupper link delete <name>
Waiting for deletion to complete...
Link "<name>" is deleted.
~~~

</section>

<section>

## Options

- <h3 id="name">name <span class="attribute-info">string, required</span></h3>

  | | |
  |-|-|
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
