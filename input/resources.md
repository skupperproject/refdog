# Skupper resources

#### Contents
- [Site configuration](#site-configuration)
  - [Site](#site)
- [Site linking](#site-linking)
  - [Claim](#claim)
  - [Grant](#grant)
  - [LinkAccess](#linkaccess)
  - [Link](#link)
- [Service exposure](#service-exposure)
  - [Connector](#connector)
  - [Listener](#listener)
- [Everything else](#everything-else)
## Site configuration

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat.


### Site

A [site][site] is a place where components of your application are
running.  Sites are linked to form application
[networks][network].

There can be only one site definition per namespace.

[site]: concepts.md#site
[network]: concepts.md#network

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

##### `serviceAccount`



_Type_: String\
_Required_: No\
_Default_: None
##### `settings`



_Type_: Array\
_Required_: No\
_Default_: None
##### `name`

A name of your choice for the Skupper site.  This name is
displayed in the console and CLI output.


_Type_: \
_Required_: No\
_Default_: None
##### `enableLinkAccess`

Enable external access for links from remote sites.


_Type_: Boolean\
_Required_: No\
_Default_: False
##### `linkAccessType`

Select the means of opening external access.

The default is `route` on OpenShift and `loadbalancer`
otherwise.


_Type_: String\
_Required_: No\
_Default_: `route` if the environment is OpenShift, otherwise
`loadbalancer`

##### `linkAccessHost`

The host or IP used to expose link access.


_Type_: String\
_Required_: No\
_Default_: None
## Site linking

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat.


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

##### `url`



_Type_: String\
_Required_: Yes\
_Default_: None
##### `secret`



_Type_: String\
_Required_: Yes\
_Default_: None
##### `ca`



_Type_: String\
_Required_: Yes\
_Default_: None
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

##### `claims`



_Type_: Int\
_Required_: No\
_Default_: None
##### `validFor`



_Type_: String\
_Required_: No\
_Default_: None
##### `secret`



_Type_: String\
_Required_: No\
_Default_: None
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

##### `roles`



_Type_: Array\
_Required_: Yes\
_Default_: None
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


_Type_: String\
_Required_: No\
_Default_: None
##### `tlsCredentials`

The name of a Kubernetes secret containing TLS
credentials. The secret contains the trusted server
certificate (typically a CA certificate).

It can optionally include a client certificate and key for
mutual TLS.


_Type_: String\
_Required_: Yes\
_Default_: None
##### `accessType`

accessType is a hint or constraint on the kind of ingress
that can/should be used (route, nodePort, LB, nginx, etc.).


_Type_: String\
_Required_: No\
_Default_: None
##### `options`



_Type_: Object\
_Required_: No\
_Default_: None
### Link

A [link][link] is a site-to-site communication channel. Links
serve as a transport for application connections and requests.

XXX

The Link would has the details from its associated LinkAccess.

[link]: concepts.md#link

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

##### `interRouter`



_Type_: Object\
_Required_: Yes\
_Default_: None
##### `edge`



_Type_: Object\
_Required_: Yes\
_Default_: None
##### `tlsCredentials`

The name of a Kubernetes secret containing TLS
credentials. The secret contains the trusted server
certificate (typically a CA certificate).

It can optionally include a client certificate and key for
mutual TLS.


_Type_: String\
_Required_: No\
_Default_: None
##### `cost`



_Type_: Integer\
_Required_: No\
_Default_: None
##### `noClientAuth`



_Type_: Boolean\
_Required_: No\
_Default_: False
## Service exposure

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat.


### Connector

A [connector][connector] binds local servers to listeners in
remote sites.

Each namespace can contain multiple connector definitions.

[connector]: concepts.md#connector

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


_Type_: String\
_Required_: Yes\
_Default_: None
##### `port`

The port number of the server listener.


_Type_: Integer\
_Required_: Yes\
_Default_: None
##### `selector`

A Kubernetes [label selector][selector] for identifying
server pods.

[selector]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors


_Type_: String\
_Required_: No\
_Default_: None
##### `host`

The hostname or IP address of the server.  This is an
alternative to `selector` for specifying the target
server.


_Type_: String\
_Required_: No\
_Default_: None
##### `tlsCredentials`

The name of a Kubernetes secret containing TLS
credentials.  The secret contains the trusted server
certificate (typically a CA certificate).

It can optionally include a client certificate and key for
mutual TLS.


_Type_: String\
_Required_: No\
_Default_: *None*
##### `type`



_Type_: String\
_Required_: No\
_Default_: None
##### `includeNotReady`



_Type_: Boolean\
_Required_: No\
_Default_: False
### Listener

A [listener][listener] is a local connection endpoint bound to
servers in remote sites.

Each namespace can contain multiple listener definitions.

[listener]: concepts.md#listener

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


_Type_: String\
_Required_: Yes\
_Default_: None
##### `host`

The hostname or IP address of the local listener.  Clients
at this site use the listener host and port to
establish connections to the remote service.


_Type_: String\
_Required_: Yes\
_Default_: None
##### `port`

The port of the local listener.  Clients at this site use
the listener host and port to establish connections to
the remote service.


_Type_: Integer\
_Required_: Yes\
_Default_: None
##### `tlsCredentials`

The name of a Kubernetes secret containing TLS
credentials.  The secret contains the server certificate
and key.

It can optionally include a client certificate for mutual
TLS.


_Type_: String\
_Required_: No\
_Default_: *None*
##### `type`



_Type_: String\
_Required_: No\
_Default_: None
## Everything else

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat.


