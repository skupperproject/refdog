---
body_class: object resource
links:
  - name: Site concept
    url: /concepts/site.html
  - name: Site command
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
apiVersion: skupper.io/v2alpha1
kind: Site
~~~

</section>

<section>

## Examples

A minimal site:

~~~ yaml
apiVersion: skupper.io/v2alpha1
kind: Site
metadata:
  name: east
  namespace: hello-world-east
~~~

A site configured to accept links:

~~~ yaml
apiVersion: skupper.io/v2alpha1
kind: Site
metadata:
  name: west
  namespace: hello-world-west
spec:
  linkAccess: default
~~~

</section>

<section class="attributes">

## Metadata properties

- <div class="attribute"><h3 id="metadata-name">name</h3><div>string, required</div></div>

  The name of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

- <div class="attribute"><h3 id="metadata-namespace">namespace</h3><div>string</div></div>

  The namespace of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/namespace.html">Namespace concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a></td></table>

</section>

<section class="attributes">

## Spec properties

- <div class="attribute"><h3 id="spec-linkaccess">linkAccess</h3><div>string</div></div>

  Configure external access for links from remote sites.

  <table class="fields"><tr><th>Default</th><td><p><code>none</code></p>
  </td><tr><th>Choices</th><td><table class="choices"><tr><th><code>none</code></th><td><p>No linking to this site is permitted.</p>
  </td></tr><tr><th><code>default</code></th><td><p>Use the default link access for the current platform. On OpenShift, the default is <code>route</code>.  For other Kubernetes flavors, the default is <code>loadbalancer</code>.</p>
  </td></tr><tr><th><code>route</code></th><td><p>Use an OpenShift route.  <em>OpenShift only.</em></p>
  </td></tr><tr><th><code>loadbalancer</code></th><td><p>Use a Kubernetes load balancer.  <em>Kubernetes only.</em></p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/link-access.html">Link access concept</a>, <a href="https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer">Kubernetes load balancer services</a></td></table>

- <div class="attribute"><h3 id="spec-serviceaccount">serviceAccount</h3><div>string</div></div>

  The Kubernetes service account under which to run the
  Skupper controller.

  <table class="fields"><tr><th>Default</th><td><p><code>skupper-router</code></p>
  </td><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/security/service-accounts/">Kubernetes service accounts</a></td></table>

- <div class="attribute"><h3 id="spec-ha">ha</h3><div>boolean</div></div>

  <table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="spec-routermode">routerMode</h3><div>string</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="spec-defaultissuer">defaultIssuer</h3><div>string</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="spec-settings">settings</h3><div>object</div></div>

  Additional settings.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</section>

<section class="attributes">

## Status properties

- <div class="attribute"><h3 id="status-endpoints">endpoints</h3><div>array</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="status-sitesinnetwork">sitesInNetwork</h3><div>integer</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="status-network">network</h3><div>array</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/network.html">Network concept</a></td></table>

- <div class="attribute"><h3 id="status-defaultissuer">defaultIssuer</h3><div>string</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="status-status">status</h3><div>string</div></div>

  The current state of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="status-message">message</h3><div>string</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="status-conditions">conditions</h3><div>array</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</section>
