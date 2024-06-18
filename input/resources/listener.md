---
body_class: resource
links:
  - name: Listener concept
    url: /concepts/listener.html
  - name: Listener command
    url: /commands/listener.html
  - name: Connector resource
    url: /resources/connector.html
---

# Listener resource

<section>

Binds target workloads in the local site to listeners in
remote sites.

Each site can have multiple listener definitions.

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Listener
metadata:  # Metadata properties
spec:      # Spec properties
status:    # Status properties
~~~

</section>

<section>

## Examples

A listener in site West for the Hello World backend service
in site East:

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Listener
metadata:
  name: backend
  namespace: hello-world-west
spec:
  routingKey: backend
  port: 8080
  host: backend
~~~

</section>

<section>

## Metadata properties

- <h3 id="name">name <span class="property-info">string, required</span></h3>

  The name of the resource.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Kubernetes object names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/) |
  

- <h3 id="namespace">namespace <span class="property-info">string</span></h3>

  The namespace of the resource.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Namespace concept]({{site_prefix}}/concepts/namespace.html), [Kubernetes namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) |
  

</section>

<section>

## Spec properties

- <h3 id="routingkey">routingKey <span class="property-info">string, required</span></h3>

  The identifier used to route traffic from listeners to
  connectors.  To enable connecting to a service at a
  remote site, the local listener and the remote connector
  must have matching routing keys.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Routing key concept]({{site_prefix}}/concepts/routing-key.html) |
  

- <h3 id="host">host <span class="property-info">string, required</span></h3>

  The hostname or IP address of the local listener.  Clients
  at this site use the listener host and port to
  establish connections to the remote service.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="port">port <span class="property-info">integer, required</span></h3>

  The port of the local listener.  Clients at this site use
  the listener host and port to establish connections to
  the remote service.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="tlssecret">tlsSecret <span class="property-info">string</span></h3>

  The name of a Kubernetes secret containing TLS
  credentials.  The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  
  This option is used when setting up router-to-server TLS
  encryption.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Site-scoped TLS]() |
  

- <h3 id="type">type <span class="property-info">string</span></h3>

  The listener type.

  | | |
  |-|-|
  | Default | `tcp` |
  | Platforms | Kubernetes, Docker |
  

- <h3 id="options">options <span class="property-info">object</span></h3>

  Additional settings.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>

<section>

## Status properties

- <h3 id="status">status <span class="property-info">string</span></h3>

  The current state of the resource.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>
