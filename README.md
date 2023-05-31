# Refdog

A configuration reference for Skupper

#### Contents

- [Overview](#overview)
- [Site](#site)
- [Egress binding](#egress-binding)
- [Ingress binding](#ingress-binding)
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

Enumerate and relate the declarative stuff XXX

<img src="images/model.svg" width="360"/>

Site linking, by contrast, is procedural XXX

## Site

A [site](terminology.md#site) is a place where part of your
application is running.  *Examples!*

Sites are linked to form application
[networks](terminology.md#networks).

Only one per namespace XXX

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
skupper init --site-name west --ingress loadbalancer

~~~

### Core options

#### `name`

A name of your choice for the Skupper site.  *Appears in the
console and status stuff!*

_Type_: String

#### `create-network-policy`

Create network policy to restrict access to Skupper services
exposed through this site to the pods currently in the
namespace.

_Type_: Boolean\
_Default_: False

### Ingress options

Options for configuring site [ingress](terminology.md#ingress)
so the site can accept incoming [links](terminology.md#link).

This is different from *service* ingress. XXX

#### `ingress`

Select the method for cluster ingress.  This determines
how Skupper services are exposed outside of the cluster.

_Type_: String\
_Default_: `route` if the environment is OpenShift, otherwise
`loadbalancer`\
_Choices_: `route`, `loadbalancer`, `nodeport`, `nginx-ingress-v1`, `contour-http-proxy`, `ingress`, `none`

#### `ingress-host`

The hostname or alias by which the ingress route or proxy
can be reached.

_Type_: String

#### `load-balancer-ip`

XXX


## Egress binding

Multiple in one namespace XXX

_Resource kind_: `ConfigMap`\
_Resource name_: *User defined*\
_Type label_: `skupper.io/type: egress-binding`

#### YAML example

~~~ yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: skupper-egress-binding-backend
  namespace: east
  labels:
    skupper.io/type: egress-binding
data: |
  routing-key: backend:8080
  port: 8080
  selector: app=backend

~~~

#### CLI example

~~~ sh
skupper service bind-egress backend:8080 deployment/backend

~~~

### Core options

#### `hostname`

The workload that implements this service.

_Type_: String

#### `port`

The port the target workload is listening on.

_Type_: Integer\
_Default_: The value of \`port\`

### TLS options

#### `tls-credentials`

XXX

The name of the Kubernetes secret containing custom
certificates for use in encrypting communication with TLS.

The name of the Kubernetes secret containing the CA for
exposing the service over TLS.

_Type_: String

## Ingress binding

Multiple in one namespace XXX

_Resource kind_: `ConfigMap`\
_Resource name_: *User defined*\
_Type label_: `skupper.io/type: ingress-binding`

#### YAML example

~~~ yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: skupper-ingress-binding-backend
  namespace: west
  labels:
    skupper.io/type: ingress-binding
data: |
  routing-key: backend:8080
  hostname: backend
  port: 8080

~~~

#### CLI example

~~~ sh
skupper service bind-ingress backend:8080

~~~

### Core options

#### `routing-key`

XXX

_Type_: String

### TLS options

#### `tls-credentials`

XXX

The name of the Kubernetes secret containing custom
certificates for use in encrypting communication with TLS.

The name of the Kubernetes secret containing the CA for
exposing the service over TLS.

_Type_: String

## Console

Only one per namespace XXX

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
  users: skupper-console-users

~~~

### Options

#### `auth`

The user authentication mode for the console.

`internal` - Use Skupper's built-in authentication.  See
the `users` option.

`openshift` - Use OpenShift authentication, so that users
who have permission to log into OpenShift and view the
namespace (project) can view the console.

`unsecured` - No authentication.  Anyone with the URL can
view the console.

_Type_: String\
_Default_: `internal`\
_Choices_: `internal`, `openshift`, `unsecured`

#### `users`

The name of the Kubernetes secret containing the console
users and passwords for the `internal` authentication
mode.

If not set, a default is generated with user "admin" and a
random password.  You can query the generated password XXX
...

_Type_: String\
_Default_: *Generated*

