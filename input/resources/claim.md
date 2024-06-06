---
body_class: resource
links:
  - name: Claim concept
    url: /concepts/claim.html
  - name: Token redeem command
    url: /commands/token-redeem.html
---

# Claim resource

<section>

XXX A verifiable assertion of permission to link to a remote
site.  A claim contains the URL and secret of an existing
grant.

A claim is redeemed for a link and a secret.

</section>

<section>

## Spec properties

- <h3 id="url">url <span class="property-info">string, required</span></h3>

  The URL at which the claim is redeemed.

- <h3 id="secret">secret <span class="property-info">string, required</span></h3>

- <h3 id="ca">ca <span class="property-info">string, required</span></h3>

</section>

<section>

## Status properties

- <h3 id="claimed">claimed <span class="property-info">boolean</span></h3>

  True if the claim has been redeemed.

  Suggest **redeemed**.

- <h3 id="status">status <span class="property-info">string</span></h3>

</section>

<section>

## Notes

Suggest **AccessToken**.

</section>
