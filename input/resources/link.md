---
body_class: resource
---

# Link

<section>

A link is a site-to-site communication channel. Links serve
as a transport for application connections and requests.

_See also:_ [Skupper links](/concepts.html#link)

</section>

<section>

## Spec properties

- <h3 id="tlssecret">tlsSecret <span class="property-info">string</span></h3>

  The name of a Kubernetes secret containing TLS
  credentials. The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.

- <h3 id="cost">cost <span class="property-info">integer</span></h3>

- <h3 id="interrouter">interRouter <span class="property-info">object, required</span></h3>

- <h3 id="edge">edge <span class="property-info">object, required</span></h3>

- <h3 id="noclientauth">noClientAuth <span class="property-info">boolean</span></h3>

</section>

<section>

## Status properties

- <h3 id="configured">configured <span class="property-info">boolean</span></h3>

- <h3 id="active">active <span class="property-info">boolean</span></h3>

- <h3 id="status">status <span class="property-info">string</span></h3>

- <h3 id="url">url <span class="property-info">string</span></h3>

- <h3 id="site">site <span class="property-info">string</span></h3>

</section>
