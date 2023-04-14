# Refdog

A configuration reference for Skupper.

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

<dl>

### Options

<dt><p>name</p></dt>
<dd>
<p>A name of your choice for the Skupper site.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>createNetworkPolicy</p></dt>
<dd>
<p>Create network policy to restrict access to Skupper services
exposed through this site to the pods currently in the
namespace.
</p>
<div><b>Type:</b> Boolean</div>
</dd>

### Ingress options

<dl>
<dt><p>ingress</p></dt>
<dd>
<p>Select the method for cluster ingress.  Determines how X
and Y are exposed outside of the cluster.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> "route" if OpenShift, else loadbalancer
</div>
<div><b>Choices:</b> route, loadbalancer, nodeport, nginx-ingress-v1, contour-http-proxy, ingress, none</div>
</dd>
<dt><p>ingressHost</p></dt>
<dd>
<p>The hostname or alias by which the ingress route or proxy
can be reached.

The host through which the node is accessible when using
nodeport as ingress.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>loadBalancerIP</p></dt>
<dd>
<p>The load balancer IP address that will be used for XXX, if
supported by the cloud provider.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>ingressOptions</p></dt>
<dd>
<p>Set ingress, ingressHost, and loadBalancerIP for specific
Skupper services.
</p>
</dd>
</dl>

### Console options

<dl>
<dt><p>enableConsole</p></dt>
<dd>
<p>Enable skupper console must be used in conjunction with
'--enable-flow-collector' flag
</p>
<div><b>Type:</b> Boolean</div>
</dd>
<dt><p>consoleAuth</p></dt>
<dd>
<p>The user authentication method for the console.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> internal</div>
<div><b>Choices:</b> internal, openshift, unsecured</div>
</dd>
<dt><p>consoleUser</p></dt>
<dd>
<p>The console username when using internal authentication.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> admin</div>
</dd>
<dt><p>consolePassword</p></dt>
<dd>
<p>The console password when using internal authentication.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> [generated]</div>
</dd>
</dl>

### Flow collector options

<dl>
<dt><p>enableFlowCollector</p></dt>
<dd>
<p>Enable cross-site flow collection for the application network
</p>
<div><b>Type:</b> Boolean</div>
</dd>
<dt><p>flowCollectorRecordTTL</p></dt>
<dd>
<p>Time after which terminated flow records are deleted,
i.e. those flow records that have an end time set.
</p>
<div><b>Type:</b> Duration</div>
<div><b>Default:</b> 30m</div>
</dd>
</dl>

### Router options

<dl>
<dt><p>routerMode</p></dt>
<dd>
<p>The role of the router in the router topology.  Interior
routers do X.  Edge routers only do Y.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> interior</div>
<div><b>Choices:</b> interior, edge</div>
</dd>
<dt><p>routerLogging</p></dt>
<dd>
<p>Logging settings for the router.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> info</div>
<div><b>Choices:</b> trace, debug, info, notice, warning, error</div>
</dd>
<dt><p>routerDebugMode</p></dt>
<dd>
<p>Enable debug mode for the router.
</p>
<div><b>Type:</b> String</div>
<div><b>Choices:</b> asan, gdb</div>
</dd>
<dt><p>routers</p></dt>
<dd>
<p>The number of router replicas to start.
</p>
<div><b>Type:</b> Integer</div>
</dd>
</dl>

### Resource options

<dl>
<dt><p>resourceLimits</p></dt>
<dd>
<p>Resource requests and limits</p>
</dd>
<dt><p>resourceAnnotations</p></dt>
<dd>
</dd>
<dt><p>resourceLabels</p></dt>
<dd>
</dd>
<dt><p>resourceNodeAffinity</p></dt>
<dd>
</dd>
<dt><p>resourcePodAffinity</p></dt>
<dd>
</dd>
</dl>

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

<dl>

### Options

<dt><p>name</p></dt>
<dd>
<p>An optional name for the link.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> [Generated]</div>
</dd>
<dt><p>secret</p></dt>
<dd>
<p>The path to the file or resource that contains the token data.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>cost</p></dt>
<dd>
<p>The weighted cost of routing connections and requests over
this link.  The cost of this link relative to others, plus the
current backlog at each endpoint and the number of hops
required, determines how traffic is routed across the network.
</p>
<div><b>Type:</b> Integer</div>
<div><b>Default:</b> 1</div>
</dd>

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

<dl>

### Options

<dt><p>name</p></dt>
<dd>
<p>The name of the token.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> [Generated]</div>
</dd>
<dt><p>secret</p></dt>
<dd>
<p>The path to the file or resource that is to contain the
generated token data.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>type</p></dt>
<dd>
<p>The type of token to create.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> claim</div>
<div><b>Choices:</b> claim, cert</div>
</dd>
<dt><p>expiry</p></dt>
<dd>
<p>The expiration time for the token.  Valid only if the token
type is claim.
</p>
<div><b>Type:</b> Duration</div>
<div><b>Default:</b> 15m</div>
</dd>
<dt><p>password</p></dt>
<dd>
<p>A password for the token.  Valid only if the token type is
claim.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> ['Generated']</div>
</dd>
<dt><p>uses</p></dt>
<dd>
<p>The max number of uses the token allows.  Valid only if
the token type is claim.
</p>
<div><b>Type:</b> Integer</div>
<div><b>Default:</b> 1</div>
</dd>
<dt><p>authName</p></dt>
<dd>
<p>Provide a specific identity as which connecting skupper
installation will be authenticated.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> skupper (?)</div>
</dd>

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

<dl>

### Options

<dt><p>name</p></dt>
<dd>
<p>The service name.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>ports</p></dt>
<dd>
<p>A list of ports.
</p>
<div><b>Type:</b> List</div>
</dd>
<dt><p>target</p></dt>
<dd>
<p>The workload that implements this service.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>enableIngress</p></dt>
<dd>
<p>Determines whether access to the Skupper service is enabled in
this site.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> Always</div>
<div><b>Choices:</b> Always, Never</div>
</dd>
<dt><p>publishNotReadyAddresses</p></dt>
<dd>
<p>If specified, skupper will not wait for pods to be ready
</p>
<div><b>Type:</b> Boolean</div>
</dd>

## ProvidedPort

### Examples

#### CLI

~~~ sh
skupper provided-service create-port backend 8080 --target-port 9090
~~~

<dl>

### Options

<dt><p>port</p></dt>
<dd>
<p>The port number.
</p>
<div><b>Type:</b> Integer</div>
</dd>
<dt><p>name</p></dt>
<dd>
<p>The port name.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> The value of port</div>
</dd>
<dt><p>protocol</p></dt>
<dd>
<p>The protocol mapping in use for this service address.

XXX Consequences for observability.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> tcp</div>
<div><b>Choices:</b> tcp, http, http2</div>
</dd>
<dt><p>bridgeImage</p></dt>
<dd>
<p>The image to use for a bridge running external to the
skupper router
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>targetPort</p></dt>
<dd>
<p>The port the target is listening on (you can also use
colon to map source-port to a target-port).
</p>
<div><b>Type:</b> Integer</div>
<div><b>Default:</b> The value of port</div>
</dd>

### TLS options

<dl>
<dt><p>generateTLSSecrets</p></dt>
<dd>
<p>If specified, the service communication will be encrypted using TLS
</p>
<div><b>Type:</b> Boolean</div>
</dd>
<dt><p>tlsCert</p></dt>
<dd>
<p>The Kubernetes secret name with custom certificates to encrypt
the communication using TLS.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>tlsTrust</p></dt>
<dd>
<p>The Kubernetes secret name with the CA to expose the service
over TLS.
</p>
<div><b>Type:</b> String</div>
</dd>
</dl>

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

<dl>

### Options

<dt><p>name</p></dt>
<dd>
<p>The service name.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>ports</p></dt>
<dd>
<p>A list of ports.
</p>
<div><b>Type:</b> List</div>
</dd>

## RequiredPort

### Examples

#### CLI

~~~ sh
skupper required-service create-port backend 8080 --target-port 9090
~~~

<dl>

### Options

<dt><p>port</p></dt>
<dd>
<p>The port number.
</p>
<div><b>Type:</b> Integer</div>
</dd>
<dt><p>name</p></dt>
<dd>
<p>The port name.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> The value of port</div>
</dd>
<dt><p>protocol</p></dt>
<dd>
<p>The protocol mapping in use for this service address.

XXX Consequences for observability.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> tcp</div>
<div><b>Choices:</b> tcp, http, http2</div>
</dd>
<dt><p>bridgeImage</p></dt>
<dd>
<p>The image to use for a bridge running external to the
skupper router
</p>
<div><b>Type:</b> String</div>
</dd>

### TLS options

<dl>
<dt><p>generateTLSSecrets</p></dt>
<dd>
<p>If specified, the service communication will be encrypted using TLS
</p>
<div><b>Type:</b> Boolean</div>
</dd>
<dt><p>tlsCert</p></dt>
<dd>
<p>The Kubernetes secret name with custom certificates to encrypt
the communication using TLS.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>tlsTrust</p></dt>
<dd>
<p>The Kubernetes secret name with the CA to expose the service
over TLS.
</p>
<div><b>Type:</b> String</div>
</dd>
</dl>

