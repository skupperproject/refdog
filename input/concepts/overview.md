# Skupper concept overview

<figure>
  <img src="images/overview-1.svg"/>
  <figcaption>The primary concepts in the Skupper model</figcaption>
</figure>

## Sites

Skupper's job is to provide connectivity for applications that have
parts running in multiple locations and on different platforms.

A ***site*** represents a particular location and a particular
platform.  It's a place where you have real running workloads.

<figure>
  <img src="images/site-1.svg"/>
  <figcaption>A site with three workloads</figcaption>
</figure>

Learn more about **[sites](site.html)** and
**[platforms](platform.html)**.

## Site linking

In a distributed application, those workloads need to communicate with
other workloads in other sites.  Skupper uses ***links*** between sites to
provide site-to-site communication.

When a set of sites are linked, they function as one
application-focused ***network***.

<figure>
  <img src="images/network-1.svg"/>
  <figcaption>A simple network with two sites</figcaption>
</figure>

You typically use short-lived ***access tokens*** to securely create
links.

Learn more about **[links](link.html)**, **[networks](network.html)**,
and **[access tokens](access-token.html)**.

## Service exposure

Services are exposed by creating corresponding ***listeners*** and
***connectors***.  A listener in one site provides a connection
endpoint for clients.  A connector in another site binds to local
servers.

The listener and connector are associated using a ***routing key***.
Skupper routers use the routing key to forward client connections to
the sites where the server workload is running.

<figure>
  <img src="images/overview-3.svg"/>
  <figcaption>A workload exposed as a service in a remote site</figcaption>
</figure>

Learn more about **[listeners](listener.html)**,
**[connectors](connector.html)**, and **[routing
keys](routing-key.html)**.
