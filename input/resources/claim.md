---
body_class: resource
links:
  - name: Access token concept
    url: /concepts/claim.html
  - name: Token redeem command
    url: /commands/token-redeem.html
  - name: AccessGrant resource
    url: /resources/grant.html
---

# AccessToken resource

<section>

A transferrable authentication token redeemable for a link
to a remote site.  An access token contains the URL and
secret of a corresponding access grant.

</section>

<section>

## Spec properties

- <h3 id="redemptionsecret">redemptionSecret <span class="property-info">string, required</span></h3>

  The secret used to authenticate the token when submitted
  for redemption.

- <h3 id="redemptionurl">redemptionURL <span class="property-info">string, required</span></h3>

  The URL of the token redemption service at the target
  site.

- <h3 id="redemptionca">redemptionCA <span class="property-info">string, required</span></h3>

  The trusted server certificate of the token redemption
  service at the target site.

</section>

<section>

## Status properties

- <h3 id="status">status <span class="property-info">string</span></h3>

  The current state of the resource.

- <h3 id="redeemed">redeemed <span class="property-info">boolean</span></h3>

  True if the token has been redeemed.

</section>
