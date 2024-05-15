# Skupper resources

#### Contents
- [Site configuration](#site-configuration)
  - [Site](#site)
- [Site linking](#site-linking)
  - [Link](#link)
  - [LinkAccess](#linkaccess)
  - [Grant](#grant)
  - [Claim](#claim)
- [Service exposure](#service-exposure)
  - [Connector](#connector)
  - [Listener](#listener)
- [Internal](#internal)
  - [SecuredAccess](#securedaccess)
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

##### `enableLinkAccess`

Enable external access for links from remote sites.


_Type:_ Boolean\
_Required:_ No\
_Default:_ False
##### `linkAccessType`

Select the means of opening external access.


_Type:_ String\
_Required:_ No\
_Default:_ `route` if the environment is OpenShift, otherwise
`loadbalancer`

##### `linkAccessHost`

The host or IP address at which to expose link access.


_Type:_ String\
_Required:_ No\
_Default:_ None
##### `serviceAccount`



_Type:_ String\
_Required:_ No\
_Default:_ None
## Site linking


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

##### `tlsCredentials`

The name of a Kubernetes secret containing TLS
credentials. The secret contains the trusted server
certificate (typically a CA certificate).

It can optionally include a client certificate and key for
mutual TLS.


_Type:_ String\
_Required:_ No\
_Default:_ None
##### `cost`



_Type:_ Integer\
_Required:_ No\
_Default:_ None
### LinkAccess

A [link access][link-access] defines a point of external access
for links from remote sites.

XXX

LinkAccess is specifically about configuring and providing
access to router Listeners.

LinkAccess is a way of configuring and exposing router listeners.

A LinkAccess will be implemented in part by the controller
creating an underlying SecuredAccess object, but LinkAccess will
also cause the router config to be adjusted.

[link-access]: XXX

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
  accessType: loadbalancer
  tlsCredentials: skupper-site-server

~~~
#### Spec properties

##### `tlsCredentials`

The name of a Kubernetes secret containing TLS
credentials. The secret contains the trusted server
certificate (typically a CA certificate).

It can optionally include a client certificate and key for
mutual TLS.


_Type:_ String\
_Required:_ Yes\
_Default:_ None
##### `ca`

XXX

A reference to a secret.

Why have this when tlsCredentials has a CA?  The CA is only
needed if you want the controller to generate the
tlsCredentials for you, and must then refer to a secret
containing the private key of the CA as well as its
certificate.

So ca and tlsCredentials are alternatives.

If the CA is supplied in a LinkAccess, it is assumed it
exists already (for the current mode of certificate
management).


_Type:_ String\
_Required:_ No\
_Default:_ None
##### `accessType`

accessType is a hint or constraint on the kind of ingress
that can/should be used (route, nodePort, LB, nginx, etc.).


_Type:_ String\
_Required:_ No\
_Default:_ None
### Grant

XXX

Grant is the offering of access.

It is the 'server side' of a Claim.

A Grant is essentially a way to declare that someone with the
given secret can present that in exchange for a certificate
signed by the ca associated with the grant, up to the given
expiration and for the number of allowed claims.

Then, on the site you want to use that, you create a Claim.

#### Examples

#### Spec properties

##### `validFor`



_Type:_ String\
_Required:_ No\
_Default:_ None
##### `claims`



_Type:_ Int\
_Required:_ No\
_Default:_ None
### Claim

XXX

The Claim declares desire to initiate access based on a previous
Grant.

Does "claim" mean something more than an asserted grant?  That
is essentially what it is.

The Claim url is obtained from the status of the grant along
with the secret and the ca, i.e. the information for a Claim
comes from the Grant.

The Claim has the details from its associated Grant.

#### Examples

#### Spec properties

## Service exposure


### Connector

A [connector][connector] binds local servers to listeners in
remote sites.

Each namespace can contain multiple connector definitions.

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

##### `routingKey`

The identifier used to route traffic from listeners to
connectors.  To connect to a service at a remote site, the
listener and connector must have matching routing keys.


_Type:_ String\
_Required:_ Yes\
_Default:_ None
##### `selector`

A Kubernetes [label selector][selector] for targeting server
pods.

[selector]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors


_Type:_ String\
_Required:_ No\
_Default:_ None
##### `host`

The hostname or IP address of the server.  This is an
alternative to `selector` for specifying the target
server.


_Type:_ String\
_Required:_ No\
_Default:_ None
##### `port`

The port number of the server listener.


_Type:_ Integer\
_Required:_ Yes\
_Default:_ None
##### `enableTLS`

Use TLS to encrypt communication between the router and servers.

By default, the TLS credentials are generated and stored in
a secret at XXX.


_Type:_ Boolean\
_Required:_ No\
_Default:_ False
##### `tlsCredentials`

The name of a Kubernetes secret containing TLS
credentials.  The secret contains the trusted server
certificate (typically a CA certificate).

It can optionally include a client certificate and key for
mutual TLS.


_Type:_ String\
_Required:_ No\
_Default:_ None
##### `type`



_Type:_ String\
_Required:_ No\
_Default:_ None
##### `includeNotReady`



_Type:_ Boolean\
_Required:_ No\
_Default:_ False
### Listener

A [listener][listener] is a local connection endpoint bound to
servers in remote sites.

Each namespace can contain multiple listener definitions.

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

##### `routingKey`

The identifier used to route traffic from listeners to
connectors.  To connect to a service at a remote site, the
listener and connector must have matching routing keys.


_Type:_ String\
_Required:_ Yes\
_Default:_ None
##### `host`

The hostname or IP address of the local listener.  Clients
at this site use the listener host and port to
establish connections to the remote service.


_Type:_ String\
_Required:_ Yes\
_Default:_ None
##### `port`

The port of the local listener.  Clients at this site use
the listener host and port to establish connections to
the remote service.


_Type:_ Integer\
_Required:_ Yes\
_Default:_ None
##### `enableTLS`

Use TLS to encrypt communication between clients and the router.

By default, the TLS credentials are generated and stored in
a secret at XXX.


_Type:_ Boolean\
_Required:_ No\
_Default:_ False
##### `tlsCredentials`

The name of a Kubernetes secret containing TLS
credentials.  The secret contains the server certificate
and key.

It can optionally include a client certificate for mutual
TLS.


_Type:_ String\
_Required:_ No\
_Default:_ None
##### `type`



_Type:_ String\
_Required:_ No\
_Default:_ None
## Internal


### SecuredAccess

XXX

SecuredAccess is a generic way of exposing a workload (a set of
pods).

SecuredAccess just creates and necessary service/ingress
resources and optionally any secrets with tls credentials.

The implementation of LinkAccess creates a SecuredAccess and
also configures the router.

SecuredAccess is a lower level concept.  It just exposes a
workload, including if desired, generation of necessary certs
(though those can also be provided if preferred).

SecuredAccess is not in any way tied to the router.  LInkAccess
*is* tied to the router.  LinkAccess can be thought of as a
specialization of SecuredAccess.

#### Examples

#### Spec properties

