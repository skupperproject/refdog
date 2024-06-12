---
body_class: resource
links:
  - name: token redeem command
    url: /commands/token-redeem.html
  - name: AccessGrant resource
    url: /resources/grant.html
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
status:    # Status poperties
~~~

</section>

<section>

## Spec properties

- <h3 id="url">url <span class="property-info">string, required</span></h3>

  The URL of the token redemption service at the remote
  site.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="ca">ca <span class="property-info">string, required</span></h3>

  The trusted server certificate of the token redemption
  service at the remote site.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="code">code <span class="property-info">string, required</span></h3>

  The secret code used to authenticate the token when
  submitted for redemption.

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
  

- <h3 id="redeemed">redeemed <span class="property-info">boolean</span></h3>

  True if the token has been redeemed.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>
