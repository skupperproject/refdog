# Skupper terminology

#### Contents

* [Skupper networks and sites](#skupper-networks-and-sites)
  * [Networks](#networks)
  * [Sites](#sites)
  * [Links](#links)
  * [Tokens](#tokens)
  * [Ingress](#ingress)
  * [Platforms](#platforms)
* [Skupper services and ports](#skupper-services-and-ports)
  * [Services](#services)
  * [Ports](#ports)
  * [Addresses](#addresses)
  * [Protocols](#protocols)
* [Skupper applications and components](#skupper-applications-and-components)
  * [Applications](#applications)
  * [Components](#components)
  * [Processes](#processes)
* [Skupper components](#skupper-components)
  * [Bridge](#bridge)
  * [Command line interface (CLI)](#command-line-interface-cli)
  * [Console](#console)
  * [Flow collector](#flow-collector)
  * [Router](#router)
  * [Site controller](#site-controller)

## Skupper networks and sites

~~~
+--------------------------------------------------+
|               Network "Hello World"              |
|                                                  |
| +-------------+     +------+     +-------------+ |
| | Site "west" |-----| Link |-----| Site "east" | |
| +-------------+     +------+     +-------------+ |
+--------------------------------------------------+
~~~

~~~
+----------------------------------------------------------+
|                   Network "Hello World"                  |
|                                                          |
| +--------------------------+   +-----------------------+ |
| |        Site "west"       |   |       Site "east"     | |
| |                          |   |                       | |
| | +--------+   +---------+ |   | +------+   +--------+ | |
| | | Router |<--| Ingress |-------| Link |---| Router | | |
| | +--------+   +---------+ |   | +------+   +--------+ | |
| +--------------------------+   +-----------------------+ |
+----------------------------------------------------------+
~~~

### Networks

A network is formed by linking together sites.

A network corresponds to one application.
The network here is an *application* network.

### Sites

Linking sites
Links and tokens

### Links

Links are inter-site links.
Links are communication channels encrypted using mutual TLS.

### Tokens

A token is required to create a link.

A token contains a URL, which represents the target site.
A token contains a secret, which represents the authority to create a link.

Tokens can be restricted....
Tokens are restricted by default....

### Ingress

Understanding ingress is important for creating site-to-site links.

### Platforms

## Skupper services and ports

~~~
+--------------------------------+                        +--------------------------------+
|          Site "west"           |                        |          Site "east"           |
|                                |                        |                                |
| +----------------------------+ |                        | +----------------------------+ |
| | Required service "backend" | |                        | | Provided service "backend" | |
| |                            | |   +----------------+   | |                            | |
| |   +--------------------+   | |   |    Address     |   | |   +--------------------+   | |
| |   | Required port 8080 |---------| "backend:8080" |---------| Provided port 8080 |   | |
| |   +--------------------+   | |   +----------------+   | |   +--------------------+   | |
| +----------------------------+ |                        | +----------------------------+ |
+--------------------------------+                        +--------------------------------+
~~~

### Services

service - a logical representation of a service\
server - an actual pod implementing a given service\
client - something that uses a service

The ultimate purpose of Skupper is to enable application components (microservices) to communicate across distinct sites.
Providing services and requiring services.

A service can have multiple ports.
Each port represents a routable *address*.

A provided service has a target.

### Ports

### Addresses

Routers deal in addresses.
An address is service name plus port.  One communication channel.  Each one has a protocol.

### Protocols

Some protocols work at the granularity of connections.  Each connection is an opaque stream.  Load balancing!
Some protocols work at the granularity of requests (and responses).  Load balancing!

## Skupper applications and components

~~~
              +-----------------------------------------------------------------------+
              |                        Application "Hello World"                      |
              |                                                                       |
              | +--------------------------------+   +------------------------------+ |
              | |      Component "frontend"      |   |      Component "backend"     | |
              | |                                |   |                              | |
              | | +----------------------------+ |   | +--------------------------+ | |
              | | | Process "south/frontend-1" | |   | | Process "east/backend-1" | | |
              | | +----------------------------+ |   | +--------------------------+ | |
              | | +----------------------------+ |   | +--------------------------+ | |
              | | | Process "south/frontend-2" | |   | | Process "east/backend-2" | | |
              | | +----------------------------+ |   | +--------------------------+ | |
              | | +----------------------------+ |   |                              | |
              | | | Process "west/frontend-1"  | |   |                              | |
              | | +----------------------------+ |   |                              | |
              | | +----------------------------+ |   |                              | |
              | | | Process "west/frontend-2"  | |   |                              | |
              | | +----------------------------+ |   |                              | |
              | +--------------------------------+   +------------------------------+ |
              +-----------------------------------------------------------------------+

+------------------------------+   +-----------------------------+   +------------------------------+
|          Site "west"         |   |          Site "east"        |   |         Site "south"         |
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
  +-----+    |  +-----------------+    |   |  +-----------------+   |    +-----+
  | CLI |-------| Site controller |    |   |  | Site controller |--------| CLI |
  +-----+    |  +-----------------+    |   |  +-----------------+   |    +-----+
             |  +----------------+     |   |                        |
             |  | Flow collector |     |   |                        |
             |  +----------------+     |   |                        |
+---------+  |      +---------+        |   |                        |
| Browser |---------| Console |        |   |                        |
+---------+  |      +---------+        |   |                        |
             +-------------------------+   +------------------------+
~~~

<!-- ### Bridge -->

<!-- client-side bridge - the component within a proxy instance that -->
<!-- translates from the application protocol (http or tcp) to amqp so that -->
<!-- the communication can be routed -->

<!-- server-side bridge - the component within a proxy instance that -->
<!-- translates from amqp back into the application protocol (http or tcp) -->
<!-- so that communication can be delivered to the intended server pod -->

### Command line interface (CLI)

### Console

The console displays the application traffic on your network.
The console is scoped to one Skupper network.
The console is read only.
The console depends on the flow collector.

### Flow collector

The flow collector stores data about application traffic.

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

### Site controller

The site controller
