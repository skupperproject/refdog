---
body_class: object concept
refdog_object_links:
- title: Application concept
  url: /concepts/application.html
- title: Workload concept
  url: /concepts/workload.html
---

# Component concept

<section>

A component is a logical part of an [application](application.html).
It has a set of responsibilities in achieving the goals of the
application.  Components provide and require **interfaces** such as
network protocols or APIs.  A component is implemented by
[workloads](workload.html).

<figure>
  <img src="images/component-model.svg"/>
  <figcaption>The component model</figcaption>
</figure>

An application has one or more components.  Each component provides
and requires zero or more interfaces.  Each component is implemented
by zero or more workloads.

<figure>
  <img src="images/component-1.svg"/>
  <figcaption>A component with workloads in two different
  sites</figcaption>
</figure>

<figure>
  <img src="images/component-2.svg"/>
  <figcaption>Hello World with its components implemented by
  workloads in three different sites</figcaption>
</figure>

</section>