---
body_class: command
links:
  - name: Site resource
    url: /resources/site.html
  - name: site command
    url: /commands/site.html
---

# site delete command

<section>

Delete a site.

</section>

<section>

## Usage

~~~ shell
$ skupper site delete [name]
Waiting for deletion to complete...
Site "<name>" is deleted.
~~~

</section>

<section>

## Options

- <h4 id="name">name <span class="option-info">string, optional</span></h4>

  The name of the site resource.
  
  If not specified, the name is that of the site
  associated with the current namespace.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
### Context options

- <h4 id="namespace">--namespace <span class="option-info">string</span></h4>

  Set the namespace.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Namespace concept]({{site_prefix}}/concepts/namespace.html), [Kubernetes namespaces]({{site_prefix}}https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) |
  
- <h4 id="context">--context <span class="option-info">string</span></h4>

  Set the kubeconfig context.

  | | |
  |-|-|
  | Platforms | Kubernetes |
  | See also | [Kubernetes kubeconfigs]({{site_prefix}}https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/) |
  
- <h4 id="platform">--platform <span class="option-info">string</span></h4>

  Set the Skupper platform.

  | | |
  |-|-|
  | Choices | <table><tr><td><code>kubernetes</code></td><td>Kubernetes</td></tr><tr><td><code>docker</code></td><td>Docker or Podman</td></tr></table> |
  | Platforms | Kubernetes, Docker |
  | See also | [Platform concept]({{site_prefix}}/concepts/platform.html) |
  
### Global options

- <h4 id="help">--help <span class="option-info"></span></h4>

  Display help and exit.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
</section>

<section>

## Errors

- **No site resource exists**

  There is no existing Skupper site resource to delete.

</section>
