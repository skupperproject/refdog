---
body_class: resource
links:
  - name: Site concept
    url: /concepts/site.html
  - name: site command
    url: /commands/site.html
  - name: Link resource
    url: /resources/link.html
---

# Site resource

<section>

A site is a place where components of your application are
running.  Sites are linked to form application networks.

There can be only one site resource per namespace.

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

## Spec properties

- <h4 id="linkaccess">linkAccess <span class="property-info">string</span></h4>

  Configure external access for links from remote sites.

  | | |
  |-|-|
  | Default | `none` |
  | Choices | `none`, `default`, `route`, `loadbalancer` |
  

- <h4 id="serviceaccount">serviceAccount <span class="property-info">string</span></h4>

  The Kubernetes service account under which to run the
  Skupper controller.

  | | |
  |-|-|
  | Default | `skupper:skupper-controller` |
  | See also | [Kubernetes service accounts]({{site_prefix}}https://kubernetes.io/docs/concepts/security/service-accounts/) |
  

- <h4 id="options">options <span class="property-info">array</span></h4>

  

</section>

<section>

## Status properties

- <h4 id="status">status <span class="property-info">string</span></h4>

  The current state of the resource.

  

- <h4 id="active">active <span class="property-info">boolean</span></h4>

  This thing is working.

  | | |
  |-|-|
  | Default | False |
  

- <h4 id="endpoints">endpoints <span class="property-info">array</span></h4>

  

- <h4 id="sitesinnetwork">sitesInNetwork <span class="property-info">integer</span></h4>

  

- <h4 id="servicesinnetwork">servicesInNetwork <span class="property-info">integer</span></h4>

  

- <h4 id="network">network <span class="property-info">array</span></h4>

  

</section>
