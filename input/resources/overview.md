---
refdog_links:
  - title: Skupper concept overview
    url: /concepts/overview.html
  - title: Skupper command overview
    url: /commands/overview.html
---

# Skupper resource overview

- CRDs and the Skupper controller (and system equivalent)
- A declarative API.
- It is the basis for all Skupper configuration.
- Skupper uses YAML resources for configuration
- These are Kubernetes custom resources.  They are used for non-Kube platforms as well.

- The resources are primary.  Everything goes through the standard
  resources.  All of Skupper's logic is in the controller that
  processes the resources.  The CLI's job is to create and submit
  resources.

- Some resource fields are "updatable" - you can change their values
  without recreating the resource.

- Where do resources go in Kubernetes?
- Where do they go in non-Kube?  FS location.  system apply.

## Sites

## Site linking

- You may want to use the CLI (or some other automation) to do the
  linking part

## Service exposure

<!-- ## Hello World using YAML -->

<!-- Site West: -->

<!-- ~~~ -->
<!-- apiVersion: skupper.io/v2alpha1 -->
<!-- kind: Site -->
<!-- metadata: -->
<!--   name: west -->
<!--   namespace: hello-world-west -->
<!-- spec: -->
<!--   linkAccess: default -->
<!-- --- -->
<!-- apiVersion: skupper.io/v2alpha1 -->
<!-- kind: Listener -->
<!-- metadata: -->
<!--   name: backend -->
<!--   namespace: hello-world-west -->
<!-- spec: -->
<!--   routingKey: backend -->
<!--   port: 8080 -->
<!--   host: backend -->
<!-- ~~~ -->

<!-- ~~~ -->
<!-- skupper token issue ~/west-token.yaml -->
<!-- ~~~ -->

<!-- Site East: -->

<!-- ~~~ -->
<!-- apiVersion: skupper.io/v2alpha1 -->
<!-- kind: Site -->
<!-- metadata: -->
<!--   name: east -->
<!--   namespace: hello-world-east -->
<!-- --- -->
<!-- apiVersion: skupper.io/v2alpha1 -->
<!-- kind: Connector -->
<!-- metadata: -->
<!--   name: backend -->
<!--   namespace: hello-world-east -->
<!-- spec: -->
<!--   routingKey: backend -->
<!--   port: 8080 -->
<!--   selector: app=backend -->
<!-- ~~~ -->

<!-- ~~~ -->
<!-- skupper token redeem ~/west-token.yaml -->
<!-- ~~~ -->
