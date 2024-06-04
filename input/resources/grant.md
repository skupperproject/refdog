---
body_class: resource
---

# Grant

<section>

@concept_description@

</section>

<section>

## Spec properties

- <h3 id="claims">claims <span class="property-info">integer</span></h3>

  _Suggest **claimsAllowed**._

- <h3 id="validfor">validFor <span class="property-info">string (duration)</span></h3>

  _Suggest **expirationPeriod**._

- <h3 id="secret">secret <span class="property-info">string</span></h3>

</section>

<section>

## Status properties

- <h3 id="claimed">claimed <span class="property-info">integer</span></h3>

  The number of times the grant has been claimed.

  _Suggest **claimsRedeemed**.  "The number of times a claim on_
  _this grant has been redeemed."_

- <h3 id="status">status <span class="property-info">string</span></h3>

- <h3 id="url">url <span class="property-info">string</span></h3>

- <h3 id="secret">secret <span class="property-info">string</span></h3>

- <h3 id="ca">ca <span class="property-info">string</span></h3>

- <h3 id="expiration">expiration <span class="property-info">string (date-time)</span></h3>

  The point in time when the grant expires.

</section>
