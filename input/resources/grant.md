---
body_class: resource
links:
  - name: Grant concept
    url: /concepts/grant.html
  - name: Token create command
    url: /commands/skupper-token-create.html
---

# Grant

<section>

An offer to accept links to the local site.  A remote site
can use a claim containing the grant URL and secret to
obtain a certificate signed by the grant's certificate
authority (CA), within a certain expiration period and for a
limited number of claims.

</section>

<section>

## Spec properties

- <h3 id="claims">claims <span class="property-info">integer</span></h3>

  Suggest **redemptionsAllowed**.

- <h3 id="validfor">validFor <span class="property-info">string (duration)</span></h3>

  Suggest **expirationPeriod**.

- <h3 id="secret">secret <span class="property-info">string</span></h3>

</section>

<section>

## Status properties

- <h3 id="claimed">claimed <span class="property-info">integer</span></h3>

  The number of times the grant has been claimed.

  Suggest **redemptions**.  "The number of times a claim on
  this grant has been redeemed."

- <h3 id="status">status <span class="property-info">string</span></h3>

- <h3 id="url">url <span class="property-info">string</span></h3>

- <h3 id="secret">secret <span class="property-info">string</span></h3>

- <h3 id="ca">ca <span class="property-info">string</span></h3>

- <h3 id="expiration">expiration <span class="property-info">string (date-time)</span></h3>

  The point in time when the grant expires.

</section>

<section>

## Notes

Suggest **AccessGrant**.

</section>
