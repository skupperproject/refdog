# Skupper terminology

#### Contents

* [Skupper sites and links](#skupper-sites-and-links)
  * [Networks](#networks)
  * [Sites](#sites)
  * [Links](#links)
  * [Tokens](#tokens)
* [Skupper listeners and connectors](#skupper-listeners-and-connectors)
  * [Listeners](#listeners)
  * [Connectors](#connectors)
  * [Routing keys](#routing-keys)
* [Skupper applications and components](#skupper-applications-and-components)
  * [Applications](#applications)
  * [Components](#components)
  * [Processes](#processes)
* [Skupper components](#skupper-components)
  * [CLI (command line interface)](#cli-command-line-interface)
  * [Collector](#collector)
  * [Console](#console)
  * [Controller](#controller)
  * [Router](#router)

## Skupper sites and links

A Skupper network is composed of sites.  A site is a place where
components of your distributed application are running.

Sites are linked together to form a dedicated network for your
application.  These links are the basis for site-to-site and
service-to-service communication.  Links are always secured using
mutual TLS authentication and encryption.

In this example, site "west" and site "east" are linked to form the
network for the "Hello World" application.

~~~
+--------------------------------------------+
|            Network "Hello World"           |
|                                            |
| +-------------+            +-------------+ |
| | Site "west" |--- Link ---| Site "east" | |
| +-------------+            +-------------+ |
+--------------------------------------------+
~~~

To create a link, the site that is to be the target of the link must
have a point of ingress, so it can accept a TCP connection.

In this example, site "west" accepts incoming TCP connections through
its ingress, and site "east" creates the site-to-site link by
establishing an outbound TCP connection to "west".

~~~
+-----------------------------------------+
|           Network "Hello World"         |
|                                         |
| +---------------+       +-------------+ |
| |  Site "west"  |       | Site "east" | |
| |               |       |             | |
| |  +---------+  |       |  +-------+  | |
| |  | Ingress |<------------| Link  |  | |
| |  +---------+  |       |  +-------+  | |
| +---------------+       +-------------+ |
+-----------------------------------------+
~~~

Creating a link also requires explicit permission from the target
site.  This permission is granted using tokens.  A token contains a
URL for the target site and a secret key.

In this example, site "west" wishes to allow "east" to create a link.
Site "west" creates a token.  The owner of "west" gives the token to
the owner of "east".  The owner of "east" then uses the token to
create the link.

~~~
  +-------------+             +-------------+
  | Site "west" |             | Site "east" |
  +-------------+             +-------------+
         |                           |
+-----------------+                  |
| 1. Create token |                  |
+-----------------+                  |
         |                           |
         |   +-------------------+   |
         |---| 2. Transfer token |-->|
         |   +-------------------+   |
         |                           |
         |    +----------------+     |
         |<---| 3. Create link |-----|
         |    +----------------+     |
         |                           |
~~~

Skupper works on multiple platforms: Kubernetes, Podman, VMs, and bare
metal hosts.  Each site in a network can run on any supported
platform.

~~~
+---------------------------+   +-------------------------+   +-------------------------+
|    Kubernetes cluster     |   |         Podman          |   |            VM           |
|                           |   |                         |   |                         |
|  +---------------------+  |   |  +-------------------+  |   |  +-------------------+  |
|  |     Site "west":    |  |   |  |  Site "central":  |  |   |  |    Site "east":   |  |
|  |   Namespace "west"  |---------|  Podman network   |---------|     VM network    |  |
|  |                     |  |   |  |    "skupper"      |  |   |  |     "skupper"     |  |
|  +---------------------+  |   |  +-------------------+  |   |  +-------------------+  |
+---------------------------+   +-------------------------+   +-------------------------+
~~~

A site does not need to be directly linked to all the other sites in a
network.  A site only needs to be *reachable* through the site
network.  Skupper is responsible for routing connections and requests
to the sites providing the required services.

~~~
 +-----------+                                   +-----------+
 | Site "nw" |---.                           .---| Site "ne" |
 +-----------+    \   +-----------------+   /    +-----------+
       |           :--| Site "central1" |--:           |
+-------------+   /   +-----------------+   \   +-------------+
| Site "west" |--:             |             :--| Site "east" |
+-------------+   \   +-----------------+   /   +-------------+
       |           :--| Site "central2" |--:           |
 +-----------+    /   +-----------------+   \    +-----------+
 | Site "sw" |---'                           '---| Site "se" |
 +-----------+                                   +-----------+
~~~

### Networks

A network (also called an "application network" or "service network")
is a set of linked sites.  Each site in the network can expose
services to other sites in the network.  Each site in the network can
access those exposed services.

A network is scoped to one distributed application and is fully
isolated from any other application network.

### Sites

A site is a network location where components of your application are
running.  Sites are linked together to form networks.

Sites have different kinds based on platform.  These currently include
Kubernetes, Podman, VMs, and bare metal.

### Links

A link is a site-to-site communication channel.  Links serve as a
transport for application traffic such as connections and requests.
Links are always encrypted using mutual TLS.

### Tokens

A token is required to create a link.  The token contains a URL, which
locates the ingress of the target site, and a secret, which represents
the authority to create a link.

Tokens can be restricted to a chosen number of uses and a particular
window of time.  By default, tokens allow only one use and expire
after 15 minutes.

## Skupper listeners and connectors

Site-to-site links are distinct from service-to-service connections.
Site links form the underlying transport for your network.  Service
connections are carried on top of this transport.

In this example, sites "west" and "east" have links to site "central".
Workload "frontend" is running on "west", and workload "backend" on
"east".  When "frontend" connects to "backend", it can ignore the
underlying link topology.  Skupper ensures that "frontend" can connect
directly to "backend".

~~~
Service connection    +---------------------+                       +--------------------+
layer                 | Workload "frontend" |---------------------->| Workload "backend" |
                      +---------------------+                       +--------------------+
                                 |                                            |
------------------------------------------------------------------------------------------
                                 |                                            |
Site link layer           +-------------+      +----------------+      +-------------+
                          | Site "west" |----->| Site "central" |<-----| Site "east" |
                          +-------------+      +----------------+      +-------------+
~~~

In site "west", workload "frontend" needs to connect to
`backend:8080`.  Skupper provides a local connection listener for that host
and port.

In site "east", workload "backend" is running and ready to handle
requests.  Skupper configures a local connector for "backend".

Listeners and connectors are linked by matching routing keys.
Connections to a listener with routing key "backend:8080" are
forwarded to remote connectors with the same routing key
"backend:8080".

~~~
+-------------------------------+                        +--------------------------------+
|          Site "west"          |                        |           Site "east"          |
|                               |                        |                                |
|    +---------------------+    |                        |     +--------------------+     |
|    | Workload "frontend" |    |                        |     | Workload "backend" |     |
|    +---------------------+    |                        |     +--------------------+     |
|               |               |                        |                ^               |
|               v               |   +----------------+   |                |               |
|   +-----------------------+   |   |  Routing key   |   |   +------------------------+   |
|   | Listener backend:8080 |-------| "backend:8080" |-------| Connector backend:8080 |   |
|   +-----------------------+   |   +----------------+   |   +------------------------+   |
+-------------------------------+                        +--------------------------------+
~~~

XXX Multiple providers at different sites (load balancing, HA)

~~~
XXX
~~~

### Listeners

### Connectors

### Routing keys

<!-- ### Services -->

<!-- service - a logical representation of a service\ -->
<!-- server - an actual pod implementing a given service\ -->
<!-- client - something that uses a service -->

<!-- The ultimate purpose of Skupper is to enable application components (microservices) to communicate across distinct sites. -->
<!-- Providing services and requiring services. -->

<!-- A service can have multiple ports. -->
<!-- Each port represents a routable *address*. -->

<!-- A provided service has a target. -->

<!-- ### Ports -->

<!-- ### Addresses -->

<!-- Routers deal in addresses. -->
<!-- An address is service name plus port.  One communication channel.  Each one has a protocol. -->

<!-- ### Protocols -->

<!-- Some protocols work at the granularity of connections.  Each connection is an opaque stream.  Load balancing! -->
<!-- Some protocols work at the granularity of requests (and responses).  Load balancing! -->



## Skupper applications and components

Part of Skupper's job is modeling how a multi-site application works.

~~~
              +-------------------------------------------------------------------------+
              |                        Application "Hello World"                        |
              |                                                                         |
              | +-------------------------------+   +---------------------------------+ |
              | |      Component "frontend"     |   |        Component "backend"      | |
              | |                               |   |                                 | |
              | | +---------------------------+ |   | +-----------------------------+ | |
              | | | Process "west/frontend-1" | |   | | Process "central/backend-1" | | |
              | | +---------------------------+ |   | +-----------------------------+ | |
              | | +---------------------------+ |   | +-----------------------------+ | |
              | | | Process "west/frontend-2" | |   | | Process "central/backend-2" | | |
              | | +---------------------------+ |   | +-----------------------------+ | |
              | | +---------------------------+ |   |                                 | |
              | | | Process "east/frontend-1" | |   |                                 | |
              | | +---------------------------+ |   |                                 | |
              | | +---------------------------+ |   |                                 | |
              | | | Process "east/frontend-2" | |   |                                 | |
              | | +---------------------------+ |   |                                 | |
              | +-------------------------------+   +---------------------------------+ |
              +-------------------------------------------------------------------------+

+------------------------------+   +-----------------------------+   +------------------------------+
|          Site "west"         |   |        Site "central"       |   |          Site "east"         |
|                              |   |                             |   |                              |
| +--------------------------+ |   | +-------------------------+ |   | +--------------------------+ |
| |    Workload "frontend"   | |   | |    Workload "backend"   | |   | |    Workload "frontend"   | |
| |                          | |   | |                         | |   | |                          | |
| | +----------------------+ | |   | | +---------------------+ | |   | | +----------------------+ | |
| | | Process "frontend-1" | | |   | | | Process "backend-1" | | |   | | | Process "frontend-1" | | |
| | +----------------------+ | |   | | +---------------------+ | |   | | +----------------------+ | |
| | +----------------------+ | |   | | +---------------------+ | |   | | +----------------------+ | |
| | | Process "frontend-2" | | |   | | | Process "backend-2" | | |   | | | Process "frontend-2" | | |
| | +----------------------+ | |   | | +---------------------+ | |   | | +----------------------+ | |
| +--------------------------+ |   | +-------------------------+ |   | +--------------------------+ |
+------------------------------+   +-----------------------------+   +------------------------------+
~~~

### Applications

### Components

### Processes

A process represents running application code.
On Kubernetes, a process is a pod.
On Docker or Podman, a process is a container.
On bare-metal hosts or VMs, a process is a "process".

## Skupper components

The software components that implement Skupper's features.

~~~
             +-------------------------+   +------------------------+
             |       Site "west"       |   |       Site "east"      |
             |                         |   |                        |
             | +---------------------+ |   | +--------------------+ |
             | | Workload "frontend" | |   | | Workload "backend" | |
             | +---------------------+ |   | +--------------------+ |
             |       +--------+        |   |       +--------+       |
             |       | Router |--------------------| Router |       |
             |       +--------+        |   |       +--------+       |
  +-----+    |     +------------+      |   |     +------------+     |    +-----+
  | CLI |----------| Controller |      |   |     | Controller |----------| CLI |
  +-----+    |     +------------+      |   |     +------------+     |    +-----+
             |     +-----------+       |   |                        |
             |     | Collector |       |   |                        |
             |     +-----------+       |   |                        |
+---------+  |      +---------+        |   |                        |
| Browser |---------| Console |        |   |                        |
+---------+  |      +---------+        |   |                        |
             +-------------------------+   +------------------------+
~~~

### CLI (command line interface)

### Collector

The collector stores data about network configuration and application
traffic.

### Console

The console displays the application traffic on your network.
The console is scoped to one Skupper network.
The console is read only.
The console depends on the flow collector.

### Controller

The site controller and service controller.
This is the Skupper control plane.

### Router

Routers transfer application traffic.
Routers listen for client connections.
Routers connect to servers.

Each site has at least one router.
Routers link to eachother to form a router network.

The routers in a network are responsible for transporting application traffic.
The routers in a network constitute the Skupper data plane.

Routers implement application-layer addressing based on names.
Routers know where the target processes are for each named address.

Routers have two modes, interior and edge.
