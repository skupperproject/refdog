---
body_class: object resource
links:
  - name: Link concept
    url: /concepts/link.html
  - name: Link command
    url: /commands/link.html
  - name: AccessGrant resource
    url: /resources/grant.html
  - name: AccessToken resource
    url: /resources/claim.html
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

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Kubernetes object names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/) |
  

- <h3 id="namespace">namespace <span class="attribute-info">string</span></h3>

  The namespace of the resource.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Namespace concept]({{site_prefix}}/concepts/namespace.html), [Kubernetes namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) |
  

</section>

<section>

## Spec properties

- <h3 id="tlssecret">tlsSecret <span class="attribute-info">string</span></h3>

  The name of a Kubernetes secret containing TLS
  credentials. The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Custom certificates]() |
  

- <h3 id="cost">cost <span class="attribute-info">integer</span></h3>

  The configured "expense" of sending traffic over the
  link.

  | | |
  |-|-|
  | Default | 1 |
  | Platforms | Kubernetes, Docker |
  | See also | [Load balancing]() |
  

- <h3 id="options">options <span class="attribute-info">object</span></h3>

  Additional settings.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>

<section>

## Status properties

- <h3 id="configured">configured <span class="attribute-info">boolean</span></h3>

  | | |
  |-|-|
  | Default | False |
  | Platforms | Kubernetes, Docker |
  

- <h3 id="url">url <span class="attribute-info">string</span></h3>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="site">site <span class="attribute-info">string</span></h3>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Site concept]({{site_prefix}}/concepts/site.html) |
  

  <section class="notes">

  Is this a site name?  Ambiguous.

  </section>

- <h3 id="status">status <span class="attribute-info">string</span></h3>

  The current state of the resource.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>
