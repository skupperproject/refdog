---
body_class: resource
links:
  - name: site command
    url: /commands/site.html
  - name: Link resource
    url: /resources/link.html
---

# Site resource

<section>

A place where components of your application are running.
Sites are linked to form application networks.

There can be only one site resource per namespace.

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Site
metadata:  # Metadata properties
spec:      # Spec properties
status:    # Status poperties
~~~

</section>

<section>

## Examples

A minimal site:

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Site
metadata:
  name: east
  namespace: hello-world-east
~~~

A site configured to accept links:

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Site
metadata:
  name: west
  namespace: hello-world-west
spec:
  linkAccess: default
~~~

</section>

<section>

## Metadata properties

- <h3 id="name">name <span class="property-info">string, required</span></h3>

  The name of the resource.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="namespace">namespace <span class="property-info">string, required</span></h3>

  The namespace of the resource.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Namespace concept]({{site_prefix}}/concepts/namespace.html), [Kubernetes namespaces]() |
  

</section>

<section>

## Spec properties

- <h3 id="linkaccess">linkAccess <span class="property-info">string</span></h3>

  Configure external access for links from remote sites.

  | | |
  |-|-|
  | Default | `none` |
  | Choices | <table><tr><td><code>none</code></td><td>No linking to this site is permitted.</td></tr><tr><td><code>default</code></td><td>Use the default link access.  On OpenShift, the default is `route`.  For other Kubernetes flavors, the default is `loadbalancer`.</td></tr><tr><td><code>route</code></td><td>Use an OpenShift route.  _OpenShift only._</td></tr><tr><td><code>loadbalancer</code></td><td>Use a Kubernetes load balancer.  _Kubernetes only._</td></tr></table> |
  | Platforms | Kubernetes, Docker |
  | See also | [Link access concept]({{site_prefix}}/concepts/link-access.html), [Kubernetes load balancer services](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer) |
  

- <h3 id="serviceaccount">serviceAccount <span class="property-info">string</span></h3>

  The Kubernetes service account under which to run the
  Skupper controller.

  | | |
  |-|-|
  | Default | `skupper:skupper-controller` |
  | Platforms | Kubernetes |
  | See also | [Kubernetes service accounts](https://kubernetes.io/docs/concepts/security/service-accounts/) |
  

- <h3 id="options">options <span class="property-info">object</span></h3>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>

<section>

## Status properties

- <h3 id="status">status <span class="property-info">string</span></h3>

  The current state of the resource.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="active">active <span class="property-info">boolean</span></h3>

  This thing is working.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="endpoints">endpoints <span class="property-info">array</span></h3>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="sitesinnetwork">sitesInNetwork <span class="property-info">integer</span></h3>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="servicesinnetwork">servicesInNetwork <span class="property-info">integer</span></h3>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="network">network <span class="property-info">array</span></h3>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>
