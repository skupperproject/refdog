---
body_class: command
---

# Site update command

<section>

Change site settings.

</section>

<section>

## Usage

~~~ shell
$ skupper site update [name] [options]
Waiting for update to complete...
Site "<name>" is updated.
~~~

</section>

<section>

## Examples

~~~
# Update the site to accept links
skupper site update --enable-link-access

# Update multiple settings
skupper site update --enable-link-access --service-account app1:alice
~~~

</section>

<section>

## Options

- <h3 id="name">name <span class="option-info">string, optional</span></h3>

  The name of the site resource.
  
  If not specified, the name is that of the site
  associated with the current namespace.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h3 id="enable-link-access">--enable-link-access <span class="option-info">boolean</span></h3>

  Allow access for incoming links from remote sites.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Link access concept]({{site_prefix}}/concepts/link-access.html) |
  
- <h3 id="link-access-type">--link-access-type <span class="option-info">string</span></h3>

  Configure external access for links from remote sites.

  | | |
  |-|-|
  | Default | `default` |
  | Choices | <table><tr><td><code>default</code></td><td>Use the default link access.  On OpenShift, the default is `route`.  For other Kubernetes flavors, the default is `loadbalancer`.</td></tr><tr><td><code>route</code></td><td>Use an OpenShift route.  _OpenShift only._</td></tr><tr><td><code>loadbalancer</code></td><td>Use a Kubernetes load balancer.  _Kubernetes only._</td></tr></table> |
  | Platforms | Kubernetes, Docker |
  | See also | [Link access concept]({{site_prefix}}/concepts/link-access.html), [Kubernetes load balancer services](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer) |
  
- <h3 id="service-account">--service-account <span class="option-info">string</span></h3>

  The Kubernetes service account under which to run the
  Skupper controller.

  | | |
  |-|-|
  | Default | `skupper:skupper-controller` |
  | Platforms | Kubernetes |
  | See also | [Kubernetes service accounts](https://kubernetes.io/docs/concepts/security/service-accounts/) |
  
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

<section>

## Errors

- **No site resource exists**

  There is no existing Skupper site resource to update.

</section>
