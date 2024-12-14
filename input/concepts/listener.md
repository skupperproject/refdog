---
body_class: object concept
refdog_object_links:
- title: Service exposure
  url: /concepts/overview.html#service-exposure
- title: Listener resource
  url: /resources/listener.html
- title: Listener command
  url: /commands/listener/index.html
- title: Connector concept
  url: /concepts/connector.html
- title: Routing key concept
  url: /concepts/routing-key.html
---

# Listener concept

<section>

A **listener** binds a local connection endpoint to
**[connectors](connector.html)** in remote **[sites](site.html)**.
Listeners and connectors are matched using **[routing
keys](routing-key.html)**.

<figure>
  <img src="images/listener-model.svg"/>
  <figcaption>The listener model</figcaption>
</figure>

A site has zero or more listeners.  Each listener has an associated
connection endpoint and routing key.  The connection endpoint
exposes a host and port for accepting connections from local
clients.

<figure>
  <img src="images/routing-key-model.svg"/>
  <figcaption>Listeners and connectors associated by routing key</figcaption>
</figure>

The routing key is a string identifier that binds the listener to
connectors in remote sites.  Skupper routers forward client
connections across the network from listeners to connectors with
matching routing keys.  The connectors then forward the client
connections to the workload servers.

<figure>
  <img src="images/listener-1.svg"/>
  <figcaption>A listener with multiple clients connecting
  through it</figcaption>
</figure>

</section>
