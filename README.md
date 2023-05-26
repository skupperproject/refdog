# Refdog

A configuration reference for Skupper

#### Contents

- [Notes](#notes)
- [Overview](#overview)
- [Site](#site)
    - [Examples](#examples)
    - [Core options](#core-options)
    - [Site ingress options](#site-ingress-options)
- [Egress binding](#egress-binding)
    - [Examples](#examples-1)
    - [Core options](#core-options-1)
    - [TLS options](#tls-options)
    - [Advanced options](#advanced-options)
    - [Core options](#core-options-2)
- [Ingress binding](#ingress-binding)
    - [Examples](#examples-2)
    - [Core options](#core-options-3)
    - [TLS options](#tls-options-1)
    - [Advanced options](#advanced-options-1)
- [Console](#console)
    - [Examples](#examples-3)
    - [Options](#options)

## Notes

### Goals

*Regularize* and *document* Skupper configuration.

- A declarative language for configuring sites, linking sites, and
  exposing services.
- A configuration model that operates uniformly across Kubernetes,
  Podman, and Systemd bundles, while still allowing for platform
  specific variations.
- A central configuration reference for Skupper.

In addition, I'd like to use this exercise to work out what the [CLI
experience][services-cli] should be for provided and required
services.

[services-cli]: services-cli.txt

A related project is mocking up the [GUI equivalent][skuppernetes] in
the context of a Kubernetes console.

[skuppernetes]: https://www.ssorj.net/skuppernetes/

### Resources

- [Hello World expressed in YAML](hello-world/resources.yaml)
- [Hello World scripted using the proposed CLI commands](hello-world/cli.txt)
- [Hello World and systemd bundles](hello-world/systemd-bundles.yaml)
- [Skupper KCP demo](https://github.com/grs/skupper-kcp-demo)
- [Skupper syncer demo](https://github.com/grs/skupper-syncer-demo)
- [Kubernetes Service API](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/)
- [Skuppernetes, the GUI equivalent of the operations here](https://www.ssorj.net/skuppernetes/)

## Overview

<img src="images/model.svg" width="640"/>

## Site

A [site](terminology.md#site) is a place where part of your
application is running.  *Examples!*

Sites are linked to form application
[networks](terminology.md#networks).

### Examples

#### YAML

~~~ yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: west
  namespace: west
  labels:
    skupper.io/type: site
data: |
  ingress: loadbalancer
~~~

#### CLI

~~~ sh
skupper init --site-name west --ingress loadbalancer
~~~

### Core options

* **`name`**

  A name of your choice for the Skupper site.  *Appears in the
  console and status stuff!*
  
  _Type_: String

* **`create-network-policy`**

  Create network policy to restrict access to Skupper services
  exposed through this site to the pods currently in the
  namespace.
  
  _Type_: Boolean\
  _Default_: False

### Site ingress options

Options for configuring site [ingress](terminology.md#ingress)
so it can accept incoming site [links](terminology.md#link).

This is different from *service* ingress. XXX

* **`ingress`**

  Select the method for cluster ingress.  This determines
  how Skupper services are exposed outside of the cluster.
  
  _Type_: String\
  _Default_: `route` if the environment is OpenShift, otherwise
`loadbalancer`\
  _Choices_: `route`, `loadbalancer`, `nodeport`, `nginx-ingress-v1`, `contour-http-proxy`, `ingress`, `none`

* **`ingress-host`**

  The hostname or alias by which the ingress route or proxy
  can be reached.
  
  _Type_: String

* **`load-balancer-ip`**

  XXX
  

## Egress binding

### Examples

#### YAML

~~~ yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: backend
  namespace: east
  labels:
    skupper.io/type: egress-binding
data: |
  routing-key: backend-8080
  port: 8080
  selector: app=backend
~~~

#### CLI

~~~ sh
skupper service bind-egress backend:8080 deployment/backend
~~~

### Core options

* **`routing-key`**

  XXX
  
  _Type_: String

### TLS options

* **`generate-tls-secrets`**

  If specified, the service communication will be encrypted using TLS.
  
  _Type_: Boolean\
  _Default_: False

* **`tls-credentials`**

  XXX
  
  The Kubernetes secret name with custom certificates to encrypt
  the communication using TLS.
  
  The Kubernetes secret name with the CA to expose the service
  over TLS.
  
  _Type_: String

### Advanced options

* **`bridge-image`**

  The image to use for a bridge running external to the Skupper
  router.
  
  _Type_: String

### Core options

* **`hostname`**

  The workload that implements this service.
  
  _Type_: String

* **`port`**

  The port the target workload is listening on.
  
  _Type_: Integer\
  _Default_: The value of \`port\`

## Ingress binding

### Examples

#### YAML

~~~ yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: backend
  namespace: west
  labels:
    skupper.io/type: ingress-binding
data: |
  routing-key: backend-8080
  hostname: backend
  port: 8080
~~~

#### CLI

~~~ sh
skupper service bind-ingress backend:8080
~~~

### Core options

* **`routing-key`**

  XXX
  
  _Type_: String

### TLS options

* **`generate-tls-secrets`**

  If specified, the service communication will be encrypted using TLS.
  
  _Type_: Boolean\
  _Default_: False

* **`tls-credentials`**

  XXX
  
  The Kubernetes secret name with custom certificates to encrypt
  the communication using TLS.
  
  The Kubernetes secret name with the CA to expose the service
  over TLS.
  
  _Type_: String

### Advanced options

* **`bridge-image`**

  The image to use for a bridge running external to the Skupper
  router.
  
  _Type_: String

## Console

XXX

### Examples

#### YAML

~~~ yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: console
  namespace: west
  labels:
    skupper.io/type: console
data: |
  ingress: loadbalancer
  user: alice
  password-secret: <secret>
~~~

### Options

* **`auth`**

  The user authentication mode for the console.
  
  `internal` - Use Skupper authentication.  See the
  `console-user` and `console-password` options.
  
  `openshift` - Use OpenShift authentication, so that users
  who have permission to log into OpenShift and view the
  project (namespace) can view the console.
  
  `unsecured` - No authentication.  Anyone with the URL can
  view the console.
  
  _Type_: String\
  _Default_: `internal`\
  _Choices_: `internal`, `openshift`, `unsecured`

* **`user`**

  The console username when using `internal` authentication.
  
  _Type_: String\
  _Default_: `admin`

* **`password`**

  The console password when using `internal` authentication.
  If not set, a random password is generated.
  
  _Type_: String\
  _Default_: *Generated*

