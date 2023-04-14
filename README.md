# Refdog

A configuration reference for Skupper

#### Contents

- [Notes](#notes)
- [Overview](#overview)
- [Site](#Site)
    - [Examples](#examples)
    - [Options](#options)
    - [Ingress options](#ingress-options)
    - [Console options](#console-options)
    - [Flow collector options](#flow-collector-options)
    - [Router options](#router-options)
    - [Resource options](#resource-options)
- [Link](#Link)
    - [Examples](#examples-1)
    - [Options](#options-1)
- [Token](#Token)
    - [Examples](#examples-2)
    - [Options](#options-2)
- [ProvidedService](#ProvidedService)
    - [Examples](#examples-3)
    - [Options](#options-3)
- [ProvidedPort](#ProvidedPort)
    - [Examples](#examples-4)
    - [Options](#options-4)
    - [TLS options](#tls-options)
- [RequiredService](#RequiredService)
    - [Examples](#examples-5)
    - [Options](#options-5)
- [RequiredPort](#RequiredPort)
    - [Examples](#examples-6)
    - [Options](#options-6)
    - [TLS options](#tls-options-1)

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

### Examples

#### YAML

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Site
metadata:
  name: east
  namespace: east
spec:
  ingress: loadbalancer
  enableConsole: true
~~~

#### CLI

~~~ sh
skupper init --site-name east --ingress loadbalancer --enable-console
~~~

### Options

* **`name`**

  A name of your choice for the Skupper site.
  
  **Type**: String

* **`createNetworkPolicy`**

  Create network policy to restrict access to Skupper services
  exposed through this site to the pods currently in the
  namespace.
  
  **Type**: Boolean


### Ingress options

* **`ingress`**

  Select the method for cluster ingress.  Determines how X
  and Y are exposed outside of the cluster.
  
  **Type**: String\
  **Default**: `route` if OpenShift, else loadbalancer\
  **Choices**: `route`, `loadbalancer`, `nodeport`, `nginx-ingress-v1`, `contour-http-proxy`, `ingress`, `none`

* **`ingressHost`**

  The hostname or alias by which the ingress route or proxy
  can be reached.
  
  The host through which the node is accessible when using
  nodeport as ingress.
  
  **Type**: String

* **`loadBalancerIP`**

  The load balancer IP address that will be used for XXX, if
  supported by the cloud provider.
  
  **Type**: String

* **`ingressOptions`**

  Set ingress, ingressHost, and loadBalancerIP for specific
  Skupper services.
  


### Console options

* **`enableConsole`**

  Enable skupper console must be used in conjunction with
  '--enable-flow-collector' flag
  
  **Type**: Boolean

* **`consoleAuth`**

  The user authentication method for the console.
  
  **Type**: String\
  **Default**: `internal`\
  **Choices**: `internal`, `openshift`, `unsecured`

* **`consoleUser`**

  The console username when using internal authentication.
  
  **Type**: String\
  **Default**: `admin`

* **`consolePassword`**

  The console password when using internal authentication.
  
  **Type**: String\
  **Default**: *Generated*


### Flow collector options

* **`enableFlowCollector`**

  Enable cross-site flow collection for the application network
  
  **Type**: Boolean

* **`flowCollectorRecordTTL`**

  Time after which terminated flow records are deleted,
  i.e. those flow records that have an end time set.
  
  **Type**: Duration\
  **Default**: `30m`


### Router options

* **`routerMode`**

  The role of the router in the router topology.  Interior
  routers do X.  Edge routers only do Y.
  
  **Type**: String\
  **Default**: `interior`\
  **Choices**: `interior`, `edge`

* **`routerLogging`**

  Logging settings for the router.
  
  **Type**: String\
  **Default**: `info`\
  **Choices**: `trace`, `debug`, `info`, `notice`, `warning`, `error`

* **`routerDebugMode`**

  Enable debug mode for the router.
  
  **Type**: String\
  **Default**: `asan`\
  **Choices**: `asan`, `gdb`

* **`routers`**

  The number of router replicas to start.
  
  **Type**: Integer


### Resource options

* **`resourceLimits`**

  Resource requests and limits
  

* **`resourceAnnotations`**

  

* **`resourceLabels`**

  

* **`resourceNodeAffinity`**

  

* **`resourcePodAffinity`**

  


## Link

#### Diagram

<img src="images/Link.svg" height="180"/>

### Examples

#### YAML

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Link
metadata:
  name: link-to-west
  namespace: east
spec:
  secret: west-token-1
~~~

#### CLI

~~~ sh
skupper link create west-token-1.yaml --name link-to-west
~~~

### Options

* **`name`**

  An optional name for the link.
  
  **Type**: String\
  **Default**: *Generated*

* **`secret`**

  The path to the file or resource that contains the token data.
  
  **Type**: String

* **`cost`**

  The weighted cost of routing connections and requests over
  this link.  The cost of this link relative to others, plus the
  current backlog at each endpoint and the number of hops
  required, determines how traffic is routed across the network.
  
  **Type**: Integer\
  **Default**: 1


## Token

#### Diagram

<img src="images/Token.svg" height="180"/>

### Examples

#### YAML

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Token
metadata:
  name: west-token-1
  namespace: west
spec:
  secret: west-token-1
  expiry: 1h
~~~

#### CLI

~~~ sh
skupper token create west-token-1.yaml --expiry 1h
~~~

### Options

* **`name`**

  The name of the token.
  
  **Type**: String\
  **Default**: *Generated*

* **`secret`**

  The path to the file or resource that is to contain the
  generated token data.
  
  **Type**: String

* **`type`**

  The type of token to create.
  
  **Type**: String\
  **Default**: `claim`\
  **Choices**: `claim`, `cert`

* **`expiry`**

  The expiration time for the token.  Valid only if the token
  type is claim.
  
  **Type**: Duration\
  **Default**: `15m`

* **`password`**

  A password for the token.  Valid only if the token type is
  claim.
  
  **Type**: String\
  **Default**: *Generated*

* **`uses`**

  The max number of uses the token allows.  Valid only if
  the token type is claim.
  
  **Type**: Integer\
  **Default**: 1

* **`authName`**

  Provide a specific identity as which connecting skupper
  installation will be authenticated.
  
  **Type**: String\
  **Default**: `skupper` (?)


## ProvidedService

#### Diagram

<img src="images/ProvidedService.svg" height="180"/>

### Examples

#### YAML

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: ProvidedService
metadata:
  name: backend
  namespace: east
spec:
  target: deployment/backend
~~~

#### CLI

~~~ sh
skupper provided-service create backend deployment/backend
~~~

### Options

* **`name`**

  The service name.
  
  **Type**: String

* **`ports`**

  A list of ports.
  
  **Type**: List

* **`target`**

  The workload that implements this service.
  
  **Type**: String

* **`enableIngress`**

  Determines whether access to the Skupper service is enabled in
  this site.
  
  **Type**: String\
  **Default**: `Always`\
  **Choices**: `Always`, `Never`

* **`publishNotReadyAddresses`**

  If specified, skupper will not wait for pods to be ready
  
  **Type**: Boolean


## ProvidedPort

### Examples

#### CLI

~~~ sh
skupper provided-service create-port backend 8080 --target-port 9090
~~~

### Options

* **`port`**

  The port number.
  
  **Type**: Integer

* **`name`**

  The port name.
  
  **Type**: String\
  **Default**: The value of port

* **`protocol`**

  The protocol mapping in use for this service address.
  
  XXX Consequences for observability.
  
  **Type**: String\
  **Default**: `tcp`\
  **Choices**: `tcp`, `http`, `http2`

* **`bridgeImage`**

  The image to use for a bridge running external to the
  skupper router
  
  **Type**: String

* **`targetPort`**

  The port the target is listening on (you can also use
  colon to map source-port to a target-port).
  
  **Type**: Integer\
  **Default**: The value of port


### TLS options

* **`generateTLSSecrets`**

  If specified, the service communication will be encrypted using TLS
  
  **Type**: Boolean

* **`tlsCert`**

  The Kubernetes secret name with custom certificates to encrypt
  the communication using TLS.
  
  **Type**: String

* **`tlsTrust`**

  The Kubernetes secret name with the CA to expose the service
  over TLS.
  
  **Type**: String


## RequiredService

#### Diagram

<img src="images/RequiredService.svg" height="180"/>

### Examples

#### YAML

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: RequiredService
metadata:
  name: backend
  namespace: west
spec:
  ports:
    - port: 8080
~~~

#### CLI

~~~ sh
skupper required-service create backend
~~~

### Options

* **`name`**

  The service name.
  
  **Type**: String

* **`ports`**

  A list of ports.
  
  **Type**: List


## RequiredPort

### Examples

#### CLI

~~~ sh
skupper required-service create-port backend 8080 --target-port 9090
~~~

### Options

* **`port`**

  The port number.
  
  **Type**: Integer

* **`name`**

  The port name.
  
  **Type**: String\
  **Default**: The value of port

* **`protocol`**

  The protocol mapping in use for this service address.
  
  XXX Consequences for observability.
  
  **Type**: String\
  **Default**: `tcp`\
  **Choices**: `tcp`, `http`, `http2`

* **`bridgeImage`**

  The image to use for a bridge running external to the
  skupper router
  
  **Type**: String


### TLS options

* **`generateTLSSecrets`**

  If specified, the service communication will be encrypted using TLS
  
  **Type**: Boolean

* **`tlsCert`**

  The Kubernetes secret name with custom certificates to encrypt
  the communication using TLS.
  
  **Type**: String

* **`tlsTrust`**

  The Kubernetes secret name with the CA to expose the service
  over TLS.
  
  **Type**: String


