---
body_class: resource
links:
  - name: Access grant concept
    url: /concepts/grant.html
  - name: AccessToken resource
    url: /resources/claim.html
  - name: token issue command
    url: /commands/token-issue.html
---

# AccessGrant resource

<section>

Permission to redeem access tokens for links to the current
site.  A remote site can use a token containing the grant
URL and a secret code to obtain a certificate signed by the
grant's certificate authority (CA), within a certain
expiration window and for a limited number of redemptions.

The `code`, `url`, and `ca` properties of the resource
status are used to generate access tokens from the grant.

</section>

<section>

## Spec properties

- <h4 id="redemptionsallowed">redemptionsAllowed <span class="property-info">integer</span></h4>

  The number of times an access token for this grant can
  be redeemed.

  | | |
  |-|-|
  | Default | 1 |
  | Platforms | Kubernetes, Docker |
  

- <h4 id="expirationwindow">expirationWindow <span class="property-info">string (duration)</span></h4>

  The period of time in which an access token for this
  grant can be redeemed.

  | | |
  |-|-|
  | Default | `15m` |
  | Platforms | Kubernetes, Docker |
  

- <h4 id="code">code <span class="property-info">string</span></h4>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

  The secret code used to authenticate access tokens
  submitted for redemption.
  
  If not set, a value for the code field in the status is
  generated.

</section>

<section>

## Status properties

- <h4 id="status">status <span class="property-info">string</span></h4>

  The current state of the resource.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="redemptions">redemptions <span class="property-info">integer</span></h4>

  The number of times a token for this grant has been
  redeemed.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="expirationtime">expirationTime <span class="property-info">string (date-time)</span></h4>

  The point in time when the grant expires.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

  expirationTime seems to be the most conventional name.

- <h4 id="code">code <span class="property-info">string</span></h4>

  The secret code used to authenticate access tokens
  submitted for redemption.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="url">url <span class="property-info">string</span></h4>

  The URL of the token-redemption service for this grant.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="ca">ca <span class="property-info">string</span></h4>

  The trusted server certificate of the token-redemption
  service for this grant.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>
