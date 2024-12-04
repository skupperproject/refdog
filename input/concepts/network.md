---
body_class: object concept
refdog_object_links:
- title: Site concept
  url: /concepts/site.html
- title: Link concept
  url: /concepts/link.html
---

# Network concept

<section>

A **network** is a set of **[sites](site.html)** joined by
**[links](link.html)**. A Skupper network is also known as an
**application network** or **virtual application network** (VAN).

Each site in the network can expose services to other sites in the
network. In turn, each site in the network can access those exposed
services.  Each network is meant for one distributed application.
This provides isolation from other applications and networks.

<figure>
  <img src="images/network-1.svg"/>
  <figcaption>A simple two-site network</figcaption>
</figure>

<figure>
  <img src="images/network-2.svg"/>
  <figcaption>A larger network</figcaption>
</figure>

</section>
