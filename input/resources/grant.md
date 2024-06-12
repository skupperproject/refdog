---
body_class: resource
links:
  - name: AccessToken resource
    url: /resources/claim.html
  - name: token issue command
    url: /commands/token-issue.html
---

# AccessGrant resource

<section>

Permission to redeem access tokens for links to the local
site.  A remote site can use a token containing the grant
URL and secret code to obtain a certificate signed by the
grant's certificate authority (CA), within a certain
expiration window and for a limited number of redemptions.

The `code`, `url`, and `ca` properties of the resource
status are used to generate access tokens from the grant.

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: AccessGrant
metadata:  # Metadata properties
spec:      # Spec properties
status:    # Status poperties
~~~

</section>

<section>

## Spec properties

- <h3 id="redemptionsallowed">redemptionsAllowed <span class="property-info">integer</span></h3>

  The number of times an access token for this grant can
  be redeemed.

  | | |
  |-|-|
  | Default | 1 |
  | Platforms | Kubernetes, Docker |
  

- <h3 id="expirationwindow">expirationWindow <span class="property-info">string (duration)</span></h3>

  The period of time in which an access token for this
  grant can be redeemed.

  | | |
  |-|-|
  | Default | `15m` |
  | Platforms | Kubernetes, Docker |
  

- <h3 id="code">code <span class="property-info">string</span></h3>

  The secret code used to authenticate access tokens
  submitted for redemption.
  
  If not set, a value for the code field in the status is
  generated.

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
  

- <h3 id="redemptions">redemptions <span class="property-info">integer</span></h3>

  The number of times a token for this grant has been
  redeemed.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="expirationtime">expirationTime <span class="property-info">string (date-time)</span></h3>

  The point in time when the grant expires.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

  <section class="notes">

  expirationTime seems to be the most conventional name.

  </section>

- <h3 id="code">code <span class="property-info">string</span></h3>

  The secret code used to authenticate access tokens
  submitted for redemption.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="url">url <span class="property-info">string</span></h3>

  The URL of the token-redemption service for this grant.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="ca">ca <span class="property-info">string</span></h3>

  The trusted server certificate of the token-redemption
  service for this grant.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>
