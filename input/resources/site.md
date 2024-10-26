---
body_class: object resource
links:
  - name: Site concept
    url: /concepts/site.html
  - name: Site commands
    url: /commands/site/index.html
  - name: Network concept
    url: /concepts/network.html
  - name: Namespace concept
    url: /concepts/namespace.html
  - name: Link resource
    url: /resources/link.html
---

# Site resource

<section>

A place where components of your application are running.
Sites are linked to form application networks.

There can be only one Site resource per namespace.

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Site
metadata:  # Metadata properties
spec:      # Spec properties
status:    # Status properties
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

- <h3 id="name">name <span class="attribute-info">string, required</span></h3>

  The name of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

- <h3 id="namespace">namespace <span class="attribute-info">string</span></h3>

  The namespace of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="/concepts/namespace.html">Namespace concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a></td></table>

</section>

<section>

## Spec properties

- <h3 id="linkaccess">linkAccess <span class="attribute-info">string</span></h3>

  Configure external access for links from remote sites.

  <table class="fields"><tr><th>Default</th><td><p><code>none</code></p>
  </td><tr><th>Choices</th><td><table class="choices"><tr><th><code>none</code></th><td><p>No linking to this site is permitted.</p>
  </td></tr><tr><th><code>default</code></th><td><p>Use the default link access.  On OpenShift, the default is <code>route</code>.  For other Kubernetes flavors, the default is <code>loadbalancer</code>.</p>
  </td></tr><tr><th><code>route</code></th><td><p>Use an OpenShift route.  <em>OpenShift only.</em></p>
  </td></tr><tr><th><code>loadbalancer</code></th><td><p>Use a Kubernetes load balancer.  <em>Kubernetes only.</em></p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="/concepts/link-access.html">Link access concept</a>, <a href="https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer">Kubernetes load balancer services</a></td></table>

- <h3 id="serviceaccount">serviceAccount <span class="attribute-info">string</span></h3>

  The Kubernetes service account under which to run the
  Skupper controller.

  <table class="fields"><tr><th>Default</th><td><p><code>skupper-router</code></p>
  </td><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/security/service-accounts/">Kubernetes service accounts</a></td></table>

- <h3 id="ha">ha <span class="attribute-info">boolean</span></h3>

  <table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="routermode">routerMode <span class="attribute-info">string</span></h3>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="defaultissuer">defaultIssuer <span class="attribute-info">string</span></h3>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="settings">settings <span class="attribute-info">object</span></h3>

  Additional settings.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

</section>

<section>

## Status properties

- <h3 id="endpoints">endpoints <span class="attribute-info">array</span></h3>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="sitesinnetwork">sitesInNetwork <span class="attribute-info">integer</span></h3>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="network">network <span class="attribute-info">array</span></h3>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="/concepts/network.html">Network concept</a></td></table>

- <h3 id="defaultissuer">defaultIssuer <span class="attribute-info">string</span></h3>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="status">status <span class="attribute-info">string</span></h3>

  The current state of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="message">message <span class="attribute-info">string</span></h3>

  XXX

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="conditions">conditions <span class="attribute-info">array</span></h3>

  XXX

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

</section>
