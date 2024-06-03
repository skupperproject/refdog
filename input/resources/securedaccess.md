---
body_class: resource
---

# SecuredAccess

<section>

A generic resource for exposing a workload by creating the
necessary service and ingress resources and optionally
generating TLS credentials.

</section>

<section>

## Spec properties

- <h3 id="ports">ports <span class="property-info">array, required</span></h3>

- <h3 id="selector">selector <span class="property-info">object, required</span></h3>

- <h3 id="ca">ca <span class="property-info">string</span></h3>

- <h3 id="certificate">certificate <span class="property-info">string</span></h3>

- <h3 id="accesstype">accessType <span class="property-info">string</span></h3>

- <h3 id="options">options <span class="property-info">object</span></h3>

</section>

<section>

## Status properties

- <h3 id="active">active <span class="property-info">boolean</span></h3>

- <h3 id="status">status <span class="property-info">string</span></h3>

- <h3 id="urls">urls <span class="property-info">array</span></h3>

- <h3 id="ca">ca <span class="property-info">string</span></h3>

</section>
