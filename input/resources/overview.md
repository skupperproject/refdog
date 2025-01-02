---
refdog_links:
  - title: Resource index
    url: index.html
  - title: Concept overview
    url: /concepts/overview.html
  - title: Command overview
    url: /commands/overview.html
---

# Skupper resource overview

Skupper uses Kubernetes-style custom resources to configure and deploy
Skupper networks, for both Kubernetes and non-Kubernetes platforms.
The Skupper resources provide a declarative interface that simplifies
automation and supports integration with other tools.

#### Capabilities

- **Site configuration:** Create and update Skupper sites.
- **Site linking:** Create and update site-to-site links.
- **Service exposure:** Expose application workloads on Skupper
  networks.

#### Controller

The Skupper controller consumes the standard Skupper resources as
input and produces platform-specific resources as output.  The output
resources configure the local site and router for the desired
connectivity.

On Kubernetes, a Site input resource results in the following output
resources:

- A Deployment and ConfigMap for the router
- A ServiceAccount, Role, and RoleBinding (if `serviceAccount` is
  not set)
- A Secret containing a signing CA for site linking (if
  `defaultIssuer` is not set)

#### Operations

Creation, updates, deletion

- Some resource fields are "updatable" - you can change their values
  without recreating the resource.
- Where do resources go in Kubernetes?
- Where do they go in non-Kube?  FS location.  system apply.
- You can use the CLI do these things.
- On Kubernetes, use kubectl apply and delete.  On Docker, Podman, and
  Linux, use skupper system apply and delete.

#### Common properties

- spec.settings
- spec.tlsCredentials
- status.Status
- status.Message
- status.Conditions

#### Labels and annotations

{{lipsum()}}

## Primary resources

- **Site:** {{lipsum(10)}}
- **Link:** {{lipsum(10)}}
- **Listener:** {{lipsum(10)}}
- **Connector:** {{lipsum(10)}}

These are the main resources you interact with.  The others are for
less common scenarios.

Site is the heart of things.  The Site resource represents a location
in a Skupper network.  It carries all the configuration for the site.
The starting point.  The parent of other Skupper resources.

Links....  The Link resource is usually not created directly.
Instead, you use access tokens.

Listener and connector are the key resources for service exposure.

## Site linking resources

- **Link:** {{lipsum(10)}}
- **AccessGrant:** {{lipsum(10)}}
- **AccessToken:** {{lipsum(10)}}
- **RouterAccess:** {{lipsum(10)}}

You may want to use the CLI (or some other automation) to do the
linking part.

## Service exposure resources

- **Listener:** {{lipsum(10)}}
- **Connector:** {{lipsum(10)}}
- **AttachedConnector:** {{lipsum(10)}}
- **AttachedConnectorBinding:** {{lipsum(10)}}

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
