# Refdog

A configuration reference for Skupper

#### Contents

- [Overview](#overview)
- [Site](#site)
- [Connector](#connector)
- [Listener](#listener)
- [Console](#console)

<!-- ## Notes -->

<!-- ### Goals -->

<!-- *Regularize* and *document* Skupper configuration. -->

<!-- - A declarative language for configuring sites, linking sites, and -->
<!--   exposing services. -->
<!-- - A configuration model that operates uniformly across Kubernetes, -->
<!--   Podman, and Systemd bundles, while still allowing for platform -->
<!--   specific variations. -->
<!-- - A central configuration reference for Skupper. -->

<!-- In addition, I'd like to use this exercise to work out what the [CLI -->
<!-- experience][services-cli] should be for provided and required -->
<!-- services. -->

<!-- [services-cli]: services-cli.txt -->

<!-- A related project is mocking up the [GUI equivalent][skuppernetes] in -->
<!-- the context of a Kubernetes console. -->

<!-- [skuppernetes]: https://www.ssorj.net/skuppernetes/ -->

<!-- ### Resources -->

<!-- - [Hello World expressed in YAML](hello-world/resources.yaml) -->
<!-- - [Hello World scripted using the proposed CLI commands](hello-world/cli.txt) -->
<!-- - [Hello World and systemd bundles](hello-world/systemd-bundles.yaml) -->
<!-- - [Skupper KCP demo](https://github.com/grs/skupper-kcp-demo) -->
<!-- - [Skupper syncer demo](https://github.com/grs/skupper-syncer-demo) -->
<!-- - [Kubernetes Service API](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/) -->
<!-- - [Skuppernetes, the GUI equivalent of the operations here](https://www.ssorj.net/skuppernetes/) -->

## Overview

<!-- Enumerate and relate the declarative stuff XXX -->

<img src="images/model.svg" width="320"/>

<!-- Site linking, by contrast, is procedural XXX -->

## Site

A [site][site] is a place where components of your application are
running.  Sites are linked to form application
[networks](terminology.md#networks).

There can be only one `skupper-site` definition per namespace.

[site]: teminology.md#site

_Resource kind_: `ConfigMap`\
_Resource name_: `skupper-site`\
_Type label_: `skupper.io/type: site`

#### YAML example

~~~ yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: skupper-site
  namespace: west
  labels:
    skupper.io/type: site
data: |
  name: west
  ingress: loadbalancer

~~~

#### CLI example

~~~ sh
# skupper site init <options>
$ skupper site init --name west --ingress loadbalancer

~~~

### Settings

#### `name`

A name of your choice for the Skupper site.  This name is
displayed in the console and CLI output.

_Required_: No\
_Type_: String

#### `ingress`

The method for providing access to this site from outside
the cluster.  Cluster ingress enables a site to accept
incoming [links](terminology.md#link).

<!-- XXX enumerate -->

_Required_: No\
_Type_: String\
_Default_: `route` if the environment is OpenShift, otherwise
`loadbalancer`\
_Choices_: `route`, `loadbalancer`, `nodeport`, `nginx-ingress-v1`, `contour-http-proxy`, `ingress`, `none`

## Connector

A [connector][connector] binds local servers to listeners in
remote sites.

Each namespace can contain multiple connector definitions.

[connector]: terminology.md#connector

_Resource kind_: `ConfigMap`\
_Resource name_: `skupper-connector-<qualifier>`\
_Type label_: `skupper.io/type: connector`

#### YAML example

~~~ yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: skupper-connector-backend
  namespace: east
  labels:
    skupper.io/type: connector
data: |
  routing-key: backend:8080
  port: 8080
  selector: app=backend

~~~

#### CLI example

~~~ sh
# skupper connector create <routing-key> <workload>
$ skupper connector create backend:8080 deployment/backend

~~~

### Settings

#### `routing-key`

The identifier used to route traffic from listeners to
connectors.  To connect to a service at a remote site, the
listener and connector must have matching routing keys.

_Required_: Yes\
_Type_: String

#### `selector`

A Kubernetes [label selector][selector] for identifying
server pods.

[selector]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors

_Required_: No\
_Type_: String

#### `hostname`

The hostname or IP address of the server.

XXX I think this should be host, not hostname.  An IP
address here is legit.

XXX We might consider `server` (formatted `<host>:<port>`)
as opposed to hostname and port here.

_Required_: No\
_Type_: String

#### `port`

The port number of the server listener.

_Required_: Yes\
_Type_: Integer

#### `tls-credentials`

The name of a Kubernetes secret containing TLS
credentials.  The secret includes the server certificate
and key.  The connector is configured to trust the
provided server certificate.

XXX Is this correct?

XXX Compare to `tls-trust`.

_Required_: No\
_Type_: String\
_Default_: `*None*`

## Listener

A [listener][listener] is a local connection endpoint bound to
services in remote sites.

Each namespace can contain multiple listener definitions.

[listener]: terminology.md#listener

_Resource kind_: `ConfigMap`\
_Resource name_: `skupper-listener-<qualifier>`\
_Type label_: `skupper.io/type: listener`

#### YAML example

~~~ yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: skupper-listener-backend
  namespace: west
  labels:
    skupper.io/type: listener
data: |
  routing-key: backend:8080
  hostname: backend
  port: 8080

~~~

#### CLI example

~~~ sh
# skupper listener create <routing-key> <options>
$ skupper listener create backend:8080
# skupper listener create abc123 --hostname backend --port 8080

~~~

### Settings

#### `routing-key`

The identifier used to route traffic from listeners to
connectors.  To connect to a service at a remote site, the
listener and connector must have matching routing keys.

_Required_: Yes\
_Type_: String

#### `hostname`

The hostname of the local listener.  Clients at this site
use the listener hostname and port to establish
connections to the remote service.

XXX Is this always a host*name*?  I think in theory we
could have a platform where it is an address.  If so,
going to just `host` may be justified.  (The router itself
can use IP addresses in listener and connector.)

_Required_: Yes\
_Type_: String

#### `port`

The port of the local listener.  Clients at this site use
the listener hostname and port to establish connections to
the remote service.

_Required_: Yes\
_Type_: Integer

#### `tls-credentials`

The name of a Kubernetes secret containing TLS
credentials.  The secret includes the listener certificate
and key.  The secret can optionally include a trusted
client certificate.

XXX Is this correct?

XXX Compare to `tls-cert`.

_Required_: No\
_Type_: String\
_Default_: `*None*`

## Console

A web interface for viewing the application network and monitoring
application traffic.

There can be only one `skupper-console` definition per namespace.

_Resource kind_: `ConfigMap`\
_Resource name_: `skupper-console`\
_Type label_: `skupper.io/type: console`

#### YAML example

~~~ yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: skupper-console
  namespace: west
  labels:
    skupper.io/type: console
data: |
  ingress: loadbalancer
  auth: unsecured

~~~

#### CLI example

~~~ sh
# skupper console init <options>
$ skupper console init --ingress loadbalancer --auth unsecured

~~~

### Settings

#### `ingress`

The method for providing access to the console from outside
the cluster.

<!-- See site ingress for the enumeration XXX -->

_Required_: No\
_Type_: String\
_Default_: `route` if the environment is OpenShift, otherwise
`loadbalancer`\
_Choices_: `route`, `loadbalancer`, `nodeport`, `nginx-ingress-v1`, `contour-http-proxy`, `ingress`, `none`

#### `auth`

The user authentication mode for the console.

`internal` - Use Skupper's built-in authentication.  See
the `users` option.

`openshift` - Use OpenShift authentication, so that users
who have permission to log into OpenShift and view the
namespace (project) can view the console.

`unsecured` - No authentication.  Anyone with the URL can
view the console.

_Required_: No\
_Type_: String\
_Default_: `internal`\
_Choices_: `internal`, `openshift`, `unsecured`

#### `users`

The name of the Kubernetes secret containing the console
users and passwords for the `internal` authentication
mode.

By default, a secret named `skupper-console-users` is
generated with user `admin` and a random password.

<!-- You can query the generated password XXX -->

_Required_: No\
_Type_: String\
_Default_: `skupper-console-users`

