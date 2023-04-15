# Notes

## Terminology

### Sites

### Linking sites

Links and tokens

### Exposing services

Providing services and requiring services

### Skupper components

#### Routers

Each site has at least one router.
Routers listen for client connections.
Routers connect to servers.
Routers link to eachother to form a router network.
Routers carry client and server traffic.

## The CLI for services

### Provided services

General purpose operations:

~~~ sh
# skupper provided-service create SERVICE-NAME TARGET [OPTIONS]
# skupper provided-service create-port SERVICE-NAME PORT [OPTIONS]

skupper provided-service create orders deployment/orders --publish-not-ready-addresses=false
skupper provided-service create-port orders 8080 --name api --protocol tcp --target-port 9090
~~~

Simplified form for the common case:

~~~ sh
# skupper provide SERVICE-NAME:PORT TARGET [OPTIONS]

skupper provide orders:8080 deployment/orders --name api --protocol tcp --target-port 9090
~~~

### Required services

General purpose operations:

~~~ sh
# skupper required-service create SERVICE-NAME [OPTIONS]
# skupper required-service create-port SERVICE-NAME PORT [OPTIONS]

skupper required-service create orders --publish-not-ready-addresses=false
skupper required-service create-port orders 8080 --name api --protocol tcp
~~~

Simplified form for the common case:

~~~ sh
# skupper require SERVICE-NAME:PORT [OPTIONS]

skupper require orders:8080 --name api --protocol tcp
~~~

### Named ports

As an alternative to port numbers:

~~~ sh
skupper provide orders:api deployment/orders --target-port 8080
skupper require orders:api --port 8080
~~~
