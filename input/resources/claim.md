---
body_class: object resource
links:
  - name: AccessGrant resource
    url: /resources/grant.html
  - name: Token redeem command
    url: /commands/token-redeem.html
---

# AccessToken resource

<section>

A transferrable token redeemable for a link to a remote
site.  An access token contains the URL and secret code of a
corresponding access grant.

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: AccessToken
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

- <h3 id="url">url <span class="attribute-info">string, required</span></h3>

  The URL of the token redemption service at the remote
  site.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="ca">ca <span class="attribute-info">string, required</span></h3>

  The trusted server certificate of the token redemption
  service at the remote site.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="code">code <span class="attribute-info">string, required</span></h3>

  The secret code used to authenticate the token when
  submitted for redemption.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="options">options <span class="attribute-info">object</span></h3>

  Additional settings.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>

<section>

## Status properties

- <h3 id="redeemed">redeemed <span class="attribute-info">boolean</span></h3>

  True if the token has been redeemed.

  | | |
  |-|-|
  | Default | False |
  | Platforms | Kubernetes, Docker |
  

- <h3 id="status">status <span class="attribute-info">string</span></h3>

  The current state of the resource.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>
