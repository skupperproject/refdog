---
body_class: object resource
links:
  - name: Link concept
    url: /concepts/link.html
  - name: Link command
    url: /commands/link.html
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
apiVersion: skupper.io/v1alpha1
kind: Link
metadata:  # Metadata properties
spec:      # Spec properties
status:    # Status properties
~~~

</section>

<section>

## Metadata properties

- <h3 id="name">name <span class="attribute-info">string, required</span></h3>

  The name of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

- <h3 id="namespace">namespace <span class="attribute-info">string</span></h3>

  The namespace of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="/concepts/namespace.html">Namespace concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a></td></table>

</section>

<section>

## Spec properties

- <h3 id="tlssecret">tlsSecret <span class="attribute-info">string</span></h3>

  The name of a Kubernetes secret containing TLS
  credentials. The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="">Custom certificates</a></td></table>

- <h3 id="cost">cost <span class="attribute-info">integer</span></h3>

  The configured "expense" of sending traffic over the
  link.

  <table class="fields"><tr><th>Default</th><td>1</td><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="">Load balancing</a></td></table>

- <h3 id="endpoints">endpoints <span class="attribute-info">array, required</span></h3>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="options">options <span class="attribute-info">object</span></h3>

  Additional settings.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

</section>

<section>

## Status properties

- <h3 id="configured">configured <span class="attribute-info">boolean</span></h3>

  <table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="status">status <span class="attribute-info">string</span></h3>

  The current state of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="active">active <span class="attribute-info">boolean</span></h3>

  This thing is working.

  <table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

</section>
