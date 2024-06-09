---
body_class: resource
links:
  - name: Grant concept
    url: /concepts/grant.html
  - name: Grant command
    url: /commands/grant.html
  - name: Token resource
    url: /resources/claim.html
---

# Grant resource

<section>

Permission to redeem tokens for links to the local site.  A
remote site can use a token containing the grant URL and
secret to obtain a certificate signed by the grant's
certificate authority (CA), within a certain expiration
period and for a limited number of redemptions.

</section>

<section>

## Spec properties

- <h4 id="redemptionsallowed">redemptionsAllowed <span class="property-info">integer</span></h4>

  The number of times a token for this grant can be
  redeemed.

  _Default:_ 1

- <h4 id="expirationperiod">expirationPeriod <span class="property-info">string (duration)</span></h4>

  The period of time in which a token for this grant can
  be redeemed.

  _Default:_ `15m`

- <h4 id="secret">secret <span class="property-info">string</span></h4>

  What is this secret as compared to the one in the
  status?  The description above says "containing the
  grant URL and secret".  Which secret is it referring to?
  
  "The certificate authority (CA) used to sign the
  certificate resulting from successful redemption"?

</section>

<section>

## Status properties

- <h4 id="status">status <span class="property-info">string</span></h4>

  The current state of the resource.

- <h4 id="redemptions">redemptions <span class="property-info">integer</span></h4>

  The number of times a token for this grant has been
  redeemed.

- <h4 id="expiration">expiration <span class="property-info">string (date-time)</span></h4>

  The point in time when the grant expires.

- <h4 id="redemptionsecret">redemptionSecret <span class="property-info">string</span></h4>

  The secret used to authenticate tokens submitted for
  redemption.

- <h4 id="redemptionurl">redemptionURL <span class="property-info">string</span></h4>

  The URL of the token redemption service for this grant.

- <h4 id="redemptionca">redemptionCA <span class="property-info">string</span></h4>

  The trusted server certificate of the token redemption
  service for this grant.

</section>
