# Skupper terminology

#### Contents

* [Skupper concepts](#skupper-concepts)
  * [Sites](#sites)
  * [Links](#links)
  * [Tokens](#tokens)
  * [Services](#services)
* [Skupper components](#)
  * [Router](#router)
  * [Console](#console)
  * [Flow collector](#flow-collector)
  * [Site controller](#site-controller)

## Skupper concepts

### Sites

Linking sites
Links and tokens

### Links

### Tokens

### Services

Skupper's reason for being is exposing services across sites.

Providing services and requiring services

## Skupper components

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

### Console

The console depends on the flow collector.

### Flow collector

The flow collector stores data about application traffic.

### Site controller

The site controller
