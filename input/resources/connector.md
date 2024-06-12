---
body_class: resource
links:
  - name: connector command
    url: /commands/connector.html
  - name: Listener resource
    url: /resources/listener.html
---

# Connector resource

<section>

Binds target workloads in the local site to listeners in
remote sites.

Each site can have multiple connector resources.

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Connector
metadata:  # Metadata properties
spec:      # Spec properties
status:    # Status poperties
~~~

</section>

<section>

## Examples

A connector in site East for the Hello World backend service:

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Connector
metadata:
  name: backend
  namespace: hello-world-east
spec:
  routingKey: backend
  port: 8080
  selector: app=backend
~~~

</section>

<section>

## Spec properties

- <h3 id="routingkey">routingKey <span class="property-info">string, required</span></h3>

  The identifier used to route traffic from listeners to
  connectors.  To expose a local workload to a remote
  site, the remote listener and the local connector must
  have matching routing keys.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [Routing key concept]({{site_prefix}}/concepts/routing-key.html) |
  

- <h3 id="port">port <span class="property-info">integer, required</span></h3>

  The port on the target workload to forward traffic to.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="selector">selector <span class="property-info">string</span></h3>

  A Kubernetes label selector for specifying target server
  pods.
  
  On Kubernetes, you usually want to use this.  As an
  alternative, you can use `host`.

  | | |
  |-|-|
  | Platforms | Kubernetes |
  | See also | [Kubernetes label selectors]({{site_prefix}}https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors), [Kubernetes pods]({{site_prefix}}https://kubernetes.io/docs/concepts/workloads/pods/) |
  

- <h3 id="host">host <span class="property-info">string</span></h3>

  The hostname or IP address of the server.  This is an
  alternative to `selector` for specifying the target
  server.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="tlssecret">tlsSecret <span class="property-info">string</span></h3>

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  
  This option is used when setting up client-to-router TLS
  encryption.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  | See also | [TLS re-encrypt]({{site_prefix}}) |
  

- <h3 id="includenotready">includeNotReady <span class="property-info">boolean</span></h3>

  If set, include server pods that are not in the ready
  state.

  | | |
  |-|-|
  | Default | False |
  | Platforms | Kubernetes |
  

- <h3 id="type">type <span class="property-info">string</span></h3>

  The connector type.

  | | |
  |-|-|
  | Default | `tcp` |
  | Platforms | Kubernetes, Docker |
  

</section>

<section>

## Status properties

- <h3 id="status">status <span class="property-info">string</span></h3>

  The current state of the resource.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

- <h3 id="active">active <span class="property-info">boolean</span></h3>

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  

</section>
