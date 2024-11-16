---
body_class: object concept
refdog_object_links:
- title: Site concept
  url: /concepts/site.html
---

# Platform concept

<section>

A _platform_ is a system for running workloads.  A platform
hosts sites.  Skupper supports Kubernetes, Docker, Podman, and
Linux.

Platforms provide namespaces for related workloads and
resources.  Skupper uses namespaces to host multiple independent
sites on one instance of a platform.

<figure>
  <img src="images/platform-1.svg"/>
  <figcaption>A platform hosting a site with three workloads</figcaption>
</figure>

<figure>
  <img src="images/platform-2.svg"/>
  <figcaption>Three networks spanning three different platforms</figcaption>
</figure>

</section>
