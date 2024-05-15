# Skupper resources

#### Contents
- [Site configuration](#site-configuration)
  - [Site](#site)
- [Site linking](#site-linking)
  - [Grant](#grant)
  - [Claim](#claim)
- [Service exposure](#service-exposure)
  - [Connector](#connector)
  - [Listener](#listener)
- [Advanced stuff](#advanced-stuff)
  - [Link](#link)
  - [LinkAccess](#linkaccess)
- [Internal stuff](#internal-stuff)
  - [SecuredAccess](#securedaccess)
  - [Certificate](#certificate)
## Site configuration


### Site

A [site][site] is a place where components of your application are
running.  Sites are linked to form application
[networks][network].

There can be only one site definition per namespace.

[site]: concepts.html#site
[network]: concepts.html#network

#### Examples

A minimal site definition

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Site
metadata:
  name: east
  namespace: hello-world-east
~~~
#### Spec properties

- **enableLinkAccess** _boolean_

  _Default:_ false

  Enable external access for links from remote sites.
  

- **linkAccessType** _string_

  _Default:_ `route` if the environment is OpenShift, otherwise
`loadbalancer`


  Select the means of opening external access.
  

- **linkAccessHost** _string_

  The host or IP address at which to expose link access.
  

- **serviceAccount** _string_

- **settings** _array_

## Site linking


### Grant

An offer to accept links to the local site.  A remote site
can use a claim containing the grant URL and secret to
obtain a certificate signed by the grant's certificate
authority (CA), within a certain expiration period and for a
limited number of claims.

#### Spec properties

- **claims** _integer_

  _Consider maxClaims, claimsAllowed, and maxClaimsAllowed_

- **validFor** _string (duration)_

  _Look for what would be conventional for this._
  _"validFor" doesn't necessarily make it clear that it's_
  _about time: "valid for 3 uses"._

- **secret** _string_

### Claim

A verifiable assertion of permission to link to a remote
site.  A claim contains the URL and secret of a previous
grant.

#### Spec properties

- **url** _string_

- **secret** _string_

- **ca** _string_

## Service exposure


### Connector

A [connector][connector] binds local servers to listeners in
remote sites.

Each site can have multiple connector definitions.

[connector]: concepts.html#connector

#### Examples

A connector in site East for the Hello World backend service


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
#### Spec properties

- **routingKey** _string_

  The identifier used to route traffic from listeners to
  connectors.  To connect to a service at a remote site, the
  listener and connector must have matching routing keys.
  

- **selector** _string_

  A Kubernetes [label selector][selector] for targeting server
  pods.
  
  [selector]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
  

- **host** _string_

  The hostname or IP address of the server.  This is an
  alternative to `selector` for specifying the target
  server.
  

- **port** _integer_

  The port number of the server listener.
  

- **enableTLS** _boolean_

  _Default:_ false

  Use TLS to encrypt communication between the router and servers.
  
  By default, the TLS credentials are generated and stored in
  a secret at XXX.
  

- **tlsCredentials** _string_

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  

- **type** _string_

  _What is this again?  I think we need a qualifier on "type"._

- **includeNotReady** _boolean_

  _Default:_ false

### Listener

A [listener][listener] is a local connection endpoint bound to
servers in remote sites.

Each site can have multiple listener definitions.

[listener]: concepts.html#listener

#### Examples

A listener in site West for the Hello World backend service
in site East


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
#### Spec properties

- **routingKey** _string_

  The identifier used to route traffic from listeners to
  connectors.  To connect to a service at a remote site, the
  listener and connector must have matching routing keys.
  

- **host** _string_

  The hostname or IP address of the local listener.  Clients
  at this site use the listener host and port to
  establish connections to the remote service.
  

- **port** _integer_

  The port of the local listener.  Clients at this site use
  the listener host and port to establish connections to
  the remote service.
  

- **enableTLS** _boolean_

  _Default:_ false

  Use TLS to encrypt communication between clients and the router.
  
  By default, the TLS credentials are generated and stored in
  a secret at XXX.
  

- **tlsCredentials** _string_

  The name of a Kubernetes secret containing TLS
  credentials.  The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  

- **tlsCA** _string_

  _Doesn't this follow, if the TLS credentials can be generated?_

- **type** _string_

  _What is this again?  I think we need a qualifier on "type"._

## Advanced stuff


### Link

A [link][link] is a site-to-site communication channel. Links
serve as a transport for application connections and requests.

[link]: concepts.html#link

#### Examples

A typical link definition

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Link
metadata:
  name: link-to-west
  namespace: hello-world-east
spec:
  [...]
~~~
#### Spec properties

- **tlsCredentials** _string_

  The name of a Kubernetes secret containing TLS
  credentials. The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  

- **cost** _integer_

- **interRouter** _object_

- **edge** _object_

- **noClientAuth** _boolean_

  _Default:_ false

### LinkAccess

A point of external access for links from remote sites.  A
LinkAccess configures the router to accept inter-router
links and creates the Kubernetes resources for external
access.

#### Examples

A typical link access definition

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: LinkAccess
metadata:
  name: skupper-router
spec:
  roles:
  - role: inter-router
    port: 55671
  - role: edge
    port: 45671
  tlsCredentials: skupper-site-server
~~~
#### Spec properties

- **roles** _array_

- **tlsCredentials** _string_

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  

- **ca** _string_

  The name of a Kubernetes secret containing a CA for
  generating TLS credentials.  If the `tlsCredentials`
  property is not set, the controller uses `ca` to
  generate them.
  

  _Consider tlsCA.  And "ca" often means "this is what I trust".  This thing has a different meaning._

- **bindHost** _string_

  _Just host?  What does "bind" do here to clarify?  I have a related attribute on site: linkAccessHost._

- **subjectAlternativeNames** _array_

- **options** _object_

## Internal stuff


### SecuredAccess

A generic resource for exposing a workload by creating the
necessary service and ingress resources and optionally
generating TLS credentials.

#### Spec properties

- **ports** _array_

- **selector** _object_

- **ca** _string_

- **certificate** _string_

- **accessType** _string_

- **options** _object_

### Certificate

#### Spec properties

- **ca** _string_

- **subject** _string_

- **hosts** _array_

- **client** _boolean_

  _Default:_ false

- **server** _boolean_

  _Default:_ false

- **signing** _boolean_

  _Default:_ false

