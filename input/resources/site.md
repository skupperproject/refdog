---
body_class: resource
links:
  - name: Site concept
    url: /concepts/site.html
  - name: Site command
    url: /commands/skupper-site.html
---

# Site

<section>

A site is a place where components of your application are
running.  Sites are linked to form application networks.

There can be only one site definition per namespace.

_See also:_ [Skupper site command]({{site_prefix}}/commands/skupper-site.html)

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

- <h3 id="linkaccess">linkAccess <span class="property-info">string</span></h3>

  Configure external access for links from remote sites.

  _Default:_ `none`

  _Choices:_
    - `none` - No link access.
    - `default` - Use the default link access.  On OpenShift, `route`
is the default.  For other Kubernetes flavors,
`loadbalancer` is the default.
    - `route` - Use an OpenShift route.
    - `loadbalancer` - Use a Kubernetes load balancer.

- <h3 id="serviceaccount">serviceAccount <span class="property-info">string</span></h3>

  The Kubernetes service account under which to run the
  Skupper controller.

  _Default:_ `skupper:skupper-controller`

  _See also:_ [Kubernetes service accounts]({{site_prefix}}https://kubernetes.io/docs/concepts/security/service-accounts/)

- <h3 id="options">options <span class="property-info">array</span></h3>

</section>

<section>

## Status properties

- <h3 id="active">active <span class="property-info">boolean</span></h3>

- <h3 id="status">status <span class="property-info">string</span></h3>

- <h3 id="endpoints">endpoints <span class="property-info">array</span></h3>

- <h3 id="sitesinnetwork">sitesInNetwork <span class="property-info">integer</span></h3>

- <h3 id="servicesinnetwork">servicesInNetwork <span class="property-info">integer</span></h3>

- <h3 id="network">network <span class="property-info">array</span></h3>

</section>
