---
body_class: object resource
links:
  - name: AccessGrant resource
    url: /resources/accessgrant.html
  - name: Token redeem command
    url: /commands/token-redeem.html
---

# AccessToken resource

<section>

A transferrable token redeemable for a link to a remote
site.  An access token contains the URL and secret code of a
corresponding access grant.

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: AccessToken
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

- <h3 id="url">url <span class="attribute-info">string, required</span></h3>

  The URL of the token redemption service at the remote
  site.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="ca">ca <span class="attribute-info">string, required</span></h3>

  The trusted server certificate of the token redemption
  service at the remote site.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="code">code <span class="attribute-info">string, required</span></h3>

  The secret code used to authenticate the token when
  submitted for redemption.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="options">options <span class="attribute-info">object</span></h3>

  Additional settings.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

</section>

<section>

## Status properties

- <h3 id="redeemed">redeemed <span class="attribute-info">boolean</span></h3>

  True if the token has been redeemed.

  <table class="fields"><tr><th>Default</th><td>False</td><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="status">status <span class="attribute-info">string</span></h3>

  The current state of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

</section>
