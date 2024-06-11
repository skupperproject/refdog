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

</section>

<section>

## Spec properties

- <h4 id="code">code <span class="property-info">string, required</span></h4>

  The secret code used to authenticate the token when
  submitted for redemption.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="url">url <span class="property-info">string, required</span></h4>

  The URL of the token redemption service at the target
  site.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="ca">ca <span class="property-info">string, required</span></h4>

  The trusted server certificate of the token redemption
  service at the target site.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>

<section>

## Status properties

- <h4 id="status">status <span class="property-info">string</span></h4>

  The current state of the resource.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="redeemed">redeemed <span class="property-info">boolean</span></h4>

  True if the token has been redeemed.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>
