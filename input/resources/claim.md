---
body_class: resource
links:
  - name: Access token concept
    url: /concepts/claim.html
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

- <h4 id="redemptionsecret">redemptionSecret <span class="property-info">string, required</span></h4>

  The secret used to authenticate the token when submitted
  for redemption.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="redemptionurl">redemptionURL <span class="property-info">string, required</span></h4>

  The URL of the token redemption service at the target
  site.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="redemptionca">redemptionCA <span class="property-info">string, required</span></h4>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

  The trusted server certificate of the token redemption
  service at the target site.

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
