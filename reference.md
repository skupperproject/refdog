# Refdog

A configuration reference for Skupper

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
  - [Certificate](#certificate)
  - [SecuredAccess](#securedaccess)
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
## Site linking

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat.


### Claim

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



_Type_: String\
_Required_: No\
_Default_: None
##### `tlsCredentials`



_Type_: String\
_Required_: Yes\
_Default_: None
##### `accessType`



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
_Default_: None
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
_Default_: None
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


### Certificate

#### Examples

#### Spec properties

##### `ca`



_Type_: String\
_Required_: Yes\
_Default_: None
##### `subject`



_Type_: String\
_Required_: Yes\
_Default_: None
##### `hosts`



_Type_: Array\
_Required_: No\
_Default_: None
##### `client`



_Type_: Boolean\
_Required_: No\
_Default_: None
##### `server`



_Type_: Boolean\
_Required_: No\
_Default_: None
##### `signing`



_Type_: Boolean\
_Required_: No\
_Default_: None
### SecuredAccess

#### Examples

#### Spec properties

##### `ports`



_Type_: Array\
_Required_: Yes\
_Default_: None
##### `selector`



_Type_: Object\
_Required_: Yes\
_Default_: None
##### `ca`



_Type_: String\
_Required_: No\
_Default_: None
##### `certificate`



_Type_: String\
_Required_: No\
_Default_: None
##### `accessType`



_Type_: String\
_Required_: No\
_Default_: None
##### `options`



_Type_: Object\
_Required_: No\
_Default_: None
