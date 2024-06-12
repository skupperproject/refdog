---
body_class: resource
---

# Certificate resource

<section>

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Certificate
metadata:  # Metadata properties
spec:      # Spec properties
status:    # Status poperties
~~~

</section>

<section>

## Spec properties

- <h4 id="ca">ca <span class="property-info">string, required</span></h4>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="subject">subject <span class="property-info">string, required</span></h4>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="hosts">hosts <span class="property-info">array</span></h4>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="client">client <span class="property-info">boolean</span></h4>

  | | |
  |-|-|
  | Default | False |
  | Platforms | Kubernetes, Docker |
  

- <h4 id="server">server <span class="property-info">boolean</span></h4>

  | | |
  |-|-|
  | Default | False |
  | Platforms | Kubernetes, Docker |
  

- <h4 id="signing">signing <span class="property-info">boolean</span></h4>

  | | |
  |-|-|
  | Default | False |
  | Platforms | Kubernetes, Docker |
  

</section>

<section>

## Status properties

- <h4 id="status">status <span class="property-info">string</span></h4>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="expiration">expiration <span class="property-info">string (date-time)</span></h4>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>
