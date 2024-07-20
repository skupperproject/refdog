---
body_class: object resource
links:
  - name: AccessToken resource
    url: /resources/accesstoken.html
  - name: Token issue command
    url: /commands/token/issue.html
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
status:    # Status properties
~~~

</section>

<section>

## Metadata properties

- <h3 id="name">name <span class="attribute-info">string, required</span></h3>

  The name of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

- <h3 id="namespace">namespace <span class="attribute-info">string</span></h3>

  The namespace of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="/concepts/namespace.html">Namespace concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a></td></table>

</section>

<section>

## Spec properties

- <h3 id="redemptionsallowed">redemptionsAllowed <span class="attribute-info">integer</span></h3>

  The number of times an access token for this grant can
  be redeemed.

  <table class="fields"><tr><th>Default</th><td>1</td><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="expirationwindow">expirationWindow <span class="attribute-info">string (duration)</span></h3>

  The period of time in which an access token for this
  grant can be redeemed.

  <table class="fields"><tr><th>Default</th><td><p><code>15m</code></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="code">code <span class="attribute-info">string</span></h3>

  The secret code used to authenticate access tokens
  submitted for redemption.
  
  If not set, a value for the code field in the status is
  generated.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="issuer">issuer <span class="attribute-info">string</span></h3>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

  <section class="notes">

  What is this?

  </section>

- <h3 id="options">options <span class="attribute-info">object</span></h3>

  Additional settings.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

</section>

<section>

## Status properties

- <h3 id="redeemed">redeemed <span class="attribute-info">integer</span></h3>

  The number of times a token for this grant has been
  redeemed.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

  <section class="notes">

  Suggest "redemptions" instead, to match
  "redemptionsAllowed" and avoid the impression that
  it's a boolean.

  </section>

- <h3 id="expiration">expiration <span class="attribute-info">string (date-time)</span></h3>

  The point in time when the grant expires.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

  <section class="notes">

  Suggest "expirationTime" instead.  It seems to be the
  most conventional name.

  </section>

- <h3 id="url">url <span class="attribute-info">string</span></h3>

  The URL of the token-redemption service for this grant.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="ca">ca <span class="attribute-info">string</span></h3>

  The trusted server certificate of the token-redemption
  service for this grant.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="code">code <span class="attribute-info">string</span></h3>

  The secret code used to authenticate access tokens
  submitted for redemption.

  <table class="fields"><tr><th>Default</th><td><p><em>Generated</em></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="status">status <span class="attribute-info">string</span></h3>

  The current state of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

</section>
