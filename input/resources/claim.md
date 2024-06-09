---
body_class: resource
links:
  - name: Token concept
    url: /concepts/claim.html
  - name: Token redeem command
    url: /commands/token-redeem.html
  - name: Grant resource
    url: /resources/grant.html
---

# Token resource

<section>

@concept_description@

</section>

<section>

## Spec properties

- <h4 id="redemptionsecret">redemptionSecret <span class="property-info">string, required</span></h4>

  The secret used to authenticate the token when submitted
  for redemption.

- <h4 id="redemptionurl">redemptionURL <span class="property-info">string, required</span></h4>

  The URL of the token redemption service at the target
  site.

- <h4 id="redemptionca">redemptionCA <span class="property-info">string, required</span></h4>

  The trusted server certificate of the token redemption
  service at the target site.

</section>

<section>

## Status properties

- <h4 id="status">status <span class="property-info">string</span></h4>

  The current state of the resource.

- <h4 id="redeemed">redeemed <span class="property-info">boolean</span></h4>

  True if the token has been redeemed.

</section>
