---
body_class: object resource
links:
  - name: Link concept
    url: /concepts/link.html
  - name: Link command
    url: /commands/link/index.html
  - name: AccessGrant resource
    url: /resources/accessgrant.html
  - name: AccessToken resource
    url: /resources/accesstoken.html
---

# Link resource

<section>

A site-to-site communication channel. Links serve as a
transport for application connections and requests.  A set
of linked sites constitute a network.

Links are not usually created directly.  Instead, you
typically use an access token to obtain a link.

~~~ yaml
apiVersion: skupper.io/v2alpha1
kind: Link
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

- <div class="attribute"><h3 id="spec-tlscredentials">tlsCredentials</h3><div>string</div></div>

  The name of a Kubernetes secret containing TLS
  credentials. The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="">Custom certificates</a></td></table>

- <div class="attribute"><h3 id="spec-cost">cost</h3><div>integer</div></div>

  The configured routing cost of sending traffic over
  the link.

  <table class="fields"><tr><th>Default</th><td>1</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="">Load balancing</a></td></table>

- <div class="attribute"><h3 id="spec-endpoints">endpoints</h3><div>array, required</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="spec-settings">settings</h3><div>object</div></div>

  Additional settings.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</section>

<section class="attributes">

## Status properties

- <div class="attribute"><h3 id="status-remotesiteid">remoteSiteId</h3><div>string</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="status-remotesitename">remoteSiteName</h3><div>string</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="status-status">status</h3><div>string</div></div>

  The current state of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="status-message">message</h3><div>string</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="status-conditions">conditions</h3><div>array</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</section>
