---
body_class: resource
links:
  - name: link command
    url: /commands/link.html
  - name: AccessGrant resource
    url: /resources/grant.html
  - name: AccessToken resource
    url: /resources/claim.html
---

# Link resource

<section>

A site-to-site communication channel. Links serve as a
transport for application connections and requests.  A set
of linked sites constitute a network.

Links are not usually created directly.  Instead, you
typically use an access token to obtain a link.

</section>

<section>

## Spec properties

- <h4 id="tlssecret">tlsSecret <span class="property-info">string</span></h4>

  The name of a Kubernetes secret containing TLS
  credentials. The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="cost">cost <span class="property-info">integer</span></h4>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="interrouter">interRouter <span class="property-info">object, required</span></h4>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="edge">edge <span class="property-info">object, required</span></h4>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="noclientauth">noClientAuth <span class="property-info">boolean</span></h4>

  | | |
  |-|-|
  | Default | False |
  | Platforms | Kubernetes, Docker |
  

</section>

<section>

## Status properties

- <h4 id="status">status <span class="property-info">string</span></h4>

  The current state of the resource.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="configured">configured <span class="property-info">boolean</span></h4>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="active">active <span class="property-info">boolean</span></h4>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="url">url <span class="property-info">string</span></h4>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h4 id="site">site <span class="property-info">string</span></h4>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>
