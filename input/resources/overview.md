---
refdog_links:
  - title: Resource index
    url: index.html
  - title: Concept overview
    url: /concepts/overview.html
  - title: Command overview
    url: /commands/overview.html
---

<!-- - Some resource fields are "updatable" - you can change their values -->
<!--   without . -->

# Skupper resource overview

Skupper provides custom resource definitions (CRDs) that define the
API for configuring and deploying Skupper networks.  Skupper uses
custom resources not only for Kubernetes but also for Docker, Podman,
and Linux.  The Skupper resources are designed to provide a uniform
declarative interface that simplifies automation and supports
integration with other tools.

#### Capabilities

- **Site configuration:** Create and update Skupper sites.
- **Site linking:** Create and update site-to-site links.
- **Service exposure:** Expose application workloads on Skupper
  networks.

#### Controller

The Skupper controller is responsible for taking the desired state
expressed in your Skupper custom resources and producing a
corresponding runtime state.  It does this by generating
platform-specific output resources that configure the local site and
router.

For example, a Site input resource on Kubernetes results in the
following output resources:

- A Deployment and ConfigMap for the router
- A ServiceAccount, Role, and RoleBinding for running site components
- A Secret containing a signing CA for site linking

#### Operations

On Kubernetes:

- *Create and update:* `kubectl apply -f <yaml-file>`
- *Delete:* `kubectl delete -f <yaml-file>`

On Docker, Podman, and Linux:

- *Create and update:* `skupper system apply -f <yaml-file>`
- *Delete:* `skupper system delete -f <yaml-file>`

On Docker, Podman, and Linux, resources are stored on the local
filesystem under
`~/.local/share/skupper/namespaces/default/input/resources`.

The Skupper CLI provides additional type-specific commands to help
create and configure Skupper resources.

<!-- #### Common properties -->

<!-- - spec.settings -->
<!-- - spec.tlsCredentials -->
<!-- - status.Status -->
<!-- - status.Message -->
<!-- - status.Conditions -->

<!-- #### Labels and annotations -->

## Primary resources

- [Site](site.html): A place on the network where application workloads are running
- [Link](link.html): A channel for communication between sites
- [Listener](listener.html): Binds a local connection endpoint to connectors in remote sites
- [Connector](connector.html): Binds a local workload to listeners in remote sites

A site is a central concept in Skupper, representing a location on the
network where part of your application is running.  It functions as
the foundational building block for your Skupper network, carrying all
the necessary configuration for that specific location. You can think
of it as the starting point for setting up your application network.

A link is a secure communication channel that joins two Skupper sites,
enabling your application to connect across sites.  Links are the
backbone of a Skupper network, providing connectivity for distributed
applications to communicate across geographical boundaries and various
platforms.

Listeners and connectors enable you expose services on Skupper
networks.  They work in tandem to bind client connection endpoints to
workloads that run in different locations.

## Site linking resources

- [Link](link.html): A channel for communication between sites
- [AccessGrant](access-grant.html): Permission to redeem access tokens for links to the local site
- [AccessToken](access-token.html): A short-lived credential used to create a link
- [RouterAccess](router-access.html): Configuration for secure access to the site router

## Service exposure resources

- [Listener](listener.html): Binds a local connection endpoint to connectors in remote sites
- [Connector](connector.html): Binds a local workload to listeners in remote sites
- [AttachedConnector](attached-connector.html): A connector in a peer namespace
- [AttachedConnectorBinding](attached-connector-binding.html): A binding to an attached connector in a peer namespace

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
