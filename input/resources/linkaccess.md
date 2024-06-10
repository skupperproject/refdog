---
body_class: resource
---

# RouterAccess resource

<section>

A point of external access for links from remote sites.  A
LinkAccess configures the router to accept inter-router
links and creates the Kubernetes resources for external
access.

</section>

<section>

## Spec properties

- <h4 id="roles">roles <span class="property-info">array, required</span></h4>

  

- <h4 id="tlssecret">tlsSecret <span class="property-info">string, required</span></h4>

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.

  

- <h4 id="ca">ca <span class="property-info">string</span></h4>

  The name of a Kubernetes secret containing a CA for
  generating TLS credentials.  If the `tlsCredentials`
  property is not set, the controller uses `ca` to
  generate them.

  

  Consider tlsCA.  And "ca" often means "this is what I trust".  This thing has a different meaning.

- <h4 id="bindhost">bindHost <span class="property-info">string</span></h4>

  

- <h4 id="subjectalternativenames">subjectAlternativeNames <span class="property-info">array</span></h4>

  

- <h4 id="options">options <span class="property-info">object</span></h4>

  

- <h4 id="accesstype">accessType <span class="property-info">string</span></h4>

  

</section>

<section>

## Status properties

- <h4 id="active">active <span class="property-info">boolean</span></h4>

  

- <h4 id="status">status <span class="property-info">string</span></h4>

  

- <h4 id="urls">urls <span class="property-info">array</span></h4>

  

</section>
