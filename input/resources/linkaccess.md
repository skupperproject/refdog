---
body_class: resource
---

# RouterAccess resource

<section>

A point of external access for links from remote sites.  A
LinkAccess configures the router to accept inter-router
links and creates the Kubernetes resources for external
access.

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: RouterAccess
metadata:  # Metadata properties
spec:      # Spec properties
status:    # Status poperties
~~~

</section>

<section>

## Spec properties

- <h3 id="roles">roles <span class="property-info">array, required</span></h3>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="tlssecret">tlsSecret <span class="property-info">string, required</span></h3>

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="ca">ca <span class="property-info">string</span></h3>

  The name of a Kubernetes secret containing a CA for
  generating TLS credentials.  If the `tlsCredentials`
  property is not set, the controller uses `ca` to
  generate them.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

  <section class="notes">

  Consider tlsCA.  And "ca" often means "this is what I trust".  This thing has a different meaning.

  </section>

- <h3 id="bindhost">bindHost <span class="property-info">string</span></h3>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="subjectalternativenames">subjectAlternativeNames <span class="property-info">array</span></h3>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="options">options <span class="property-info">object</span></h3>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="accesstype">accessType <span class="property-info">string</span></h3>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>

<section>

## Status properties

- <h3 id="active">active <span class="property-info">boolean</span></h3>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="status">status <span class="property-info">string</span></h3>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="urls">urls <span class="property-info">array</span></h3>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>
