---
body_class: object concept
refdog_object_links:
- title: Site concept
  url: /concepts/site.html
---

# Platform concept

<section>

A **platform** is a system for running application workloads.  A
platform hosts sites.  Skupper supports Kubernetes, Docker, Podman,
and Linux.

Platforms provide **namespaces** for related workloads and
resources.  Skupper uses namespaces to host multiple independent
sites on one instance of a platform.

<figure>
  <img src="images/platform-model.svg"/>
  <figcaption>The platform model</figcaption>
</figure>

A platform has zero or more namespaces.  Each namespace is
associated with zero or more workloads.  A namespace is associated
with zero sites or one site.

<figure>
  <img src="images/platform-1.svg"/>
  <figcaption>A simple network with sites on two different
  platforms</figcaption>
</figure>

<figure>
  <img src="images/platform-2.svg"/>
  <figcaption>A platform with three namespaces, two of which
  host Skupper sites</figcaption>
</figure>

</section>
