# Refdog

- [Notes](#notes)
- [Diagram](#diagram)
- [Resource _site_](#resource-site)
    - [Site examples](#site-examples)
    - [Site options](#site-options)
    - [Ingress options](#ingress-options)
    - [Console options](#console-options)
    - [Flow collector options](#flow-collector-options)
    - [Router options](#router-options)
    - [Skupper resource options](#skupper-resource-options)
- [Resource _link_](#resource-link)
    - [Link diagram](#link-diagram)
    - [Link examples](#link-examples)
    - [Link options](#link-options)
- [Resource _token_](#resource-token)
    - [Token diagram](#token-diagram)
    - [Token examples](#token-examples)
    - [Token options](#token-options)
- [Resource _provided-service_](#resource-provided-service)
    - [Provided service diagram](#provided-service-diagram)
    - [Provided service examples](#provided-service-examples)
    - [Provided service options](#provided-service-options)
    - [Provided service port options](#provided-service-port-options)
    - [Provided service port TLS options](#provided-service-port-tls-options)
- [Resource _required-service_](#resource-required-service)
    - [Required service diagram](#required-service-diagram)
    - [Required service examples](#required-service-examples)
    - [Required service options](#required-service-options)
    - [Required service port options](#required-service-port-options)
    - [Required service port TLS options](#required-service-port-tls-options)

## Notes

### Goals

*Regularize* and *document* Skupper configuration.

- A declarative language for creating sites, linking sites, and
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

- [Hello World expressed in YAML](hello-world.yaml)
- [Hello World as YAML embedded in ConfigMaps](hello-world-config-map.yaml)
- [Hello World scripted using the proposed CLI commands](hello-world-cli-script.txt)
- [Hello World and systemd bundles](hello-world-systemd-bundles.yaml)
- [Skupper KCP demo](https://github.com/grs/skupper-kcp-demo)
- [Skupper syncer demo](https://github.com/grs/skupper-syncer-demo)
- [Kubernetes Service API](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/)
- [Skuppernetes, the GUI equivalent of the operations here](https://www.ssorj.net/skuppernetes/)

<h2 id="yo">Diagram</h2>

<img src="images/model.svg" width="640"/>

## Resource _site_

### Site examples

<table>
<tbody>
<tr><th>Skupper YAML</th></tr>
<tr><td><pre>apiVersion: skupper.io/v1alpha1
kind: Site
metadata:
  name: east
  namespace: east
spec:
  ingress: loadbalancer
  enableConsole: true</pre></td></tr>
<tr><th>Skupper CLI</th></tr>
<tr><td><pre>skupper init --site-name east --ingress loadbalancer --enable-console</pre></td></tr>
</tbody>
</table>

<dl>

### Site options

<dl>
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
</dl>

### Ingress options

<dl>
<dt><p>ingress</p></dt>
<dd>
<p>Select the method for cluster ingress.  Determines how XXX
is exposed outside of the cluster.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> route if available, else loadbalancer</div>
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
<p>XXX xxxIngress, xxxIngressHost, xxxLoadBalancerIP (console, controller, router)</p>
<div><b>Type:</b> XXX</div>
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
routers do XXX.  Edge routers only do YYY.
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

### Skupper resource options

<dl>
<dt><p>resourceRequests</p></dt>
<dd>
<p>XXX</p>
<div><b>Type:</b> XXX</div>
</dd>
<dt><p>resourceLimits</p></dt>
<dd>
<p>XXX</p>
<div><b>Type:</b> XXX</div>
</dd>
<dt><p>resourceAnnotations</p></dt>
<dd>
<p>XXX</p>
<div><b>Type:</b> XXX</div>
</dd>
<dt><p>resourceLabels</p></dt>
<dd>
<p>XXX</p>
<div><b>Type:</b> XXX</div>
</dd>
<dt><p>resourceNodeAffinity</p></dt>
<dd>
<p>XXX</p>
<div><b>Type:</b> XXX</div>
</dd>
<dt><p>resourcePodAffinity</p></dt>
<dd>
<p>XXX</p>
<div><b>Type:</b> XXX</div>
</dd>
</dl>

</dl>

## Resource _link_

### Link diagram

<img src="images/link.svg" width="480"/>

### Link examples

<table>
<tbody>
<tr><th>Skupper YAML</th></tr>
<tr><td><pre>apiVersion: skupper.io/v1alpha1
kind: Link
metadata:
  name: link-to-west
  namespace: east
spec:
  secret: west-token-1</pre></td></tr>
<tr><th>Skupper CLI</th></tr>
<tr><td><pre>skupper link create west-token-1.yaml --name link-to-west</pre></td></tr>
</tbody>
</table>

<dl>

### Link options

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
</dl>

## Resource _token_

### Token diagram

<img src="images/token.svg" width="480"/>

### Token examples

<table>
<tbody>
<tr><th>Skupper YAML</th></tr>
<tr><td><pre>apiVersion: skupper.io/v1alpha1
kind: Token
metadata:
  name: west-token-1
  namespace: west
spec:
  secret: west-token-1
  expiry: 1h</pre></td></tr>
<tr><th>Skupper CLI</th></tr>
<tr><td><pre>skupper token create west-token-1.yaml --expiry 1h</pre></td></tr>
</tbody>
</table>

<dl>

### Token options

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
</dl>

## Resource _provided-service_

### Provided service diagram

<img src="images/provided-service.svg" width="480"/>

### Provided service examples

<table>
<tbody>
<tr><th>Skupper YAML</th></tr>
<tr><td><pre>apiVersion: skupper.io/v1alpha1
kind: ProvidedService
metadata:
  name: backend
  namespace: east
spec:
  target: deployment/backend
  ports:
    - port: 8080
      targetPort: 9090</pre></td></tr>
<tr><th>Skupper CLI</th></tr>
<tr><td><pre>#
# Current
#
skupper service create backend 8080
skupper service bind backend deployment/backend --target-port 9090
#
# Proposed (general purpose form)
#
skupper provided-service create backend deployment/backend
skupper provided-service create-port backend 8080 --target-port 9090
#
# Proposed (simplified form for the common case)
#
skupper provide backend:8080 deployment/backend --target-port 9090</pre></td></tr>
</tbody>
</table>

<dl>

### Provided service options

<dl>
<dt><p>name</p></dt>
<dd>
<p>The service name.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>ports[]</p></dt>
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
</dl>

### Provided service port options

<dl>
<dt><p>ports[].port</p></dt>
<dd>
<p>The port number.
</p>
<div><b>Type:</b> Integer</div>
</dd>
<dt><p>ports[].name</p></dt>
<dd>
<p>The port name.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> The value of ports[].port</div>
</dd>
<dt><p>ports[].protocol</p></dt>
<dd>
<p>The protocol mapping in use for this service address.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> tcp</div>
<div><b>Choices:</b> tcp, http, http2</div>
</dd>
<dt><p>ports[].targetPort</p></dt>
<dd>
<p>The port the target is listening on (you can also use
colon to map source-port to a target-port).
</p>
<div><b>Type:</b> List of strings</div>
<div><b>Default:</b> The value of ports[].port</div>
</dd>
<dt><p>ports[].bridgeImage</p></dt>
<dd>
<p>The image to use for a bridge running external to the
skupper router
</p>
<div><b>Type:</b> String</div>
</dd>
</dl>

### Provided service port TLS options

<dl>
<dt><p>ports[].generateTLSSecrets</p></dt>
<dd>
<p>If specified, the service communication will be encrypted using TLS
</p>
<div><b>Type:</b> Boolean</div>
</dd>
<dt><p>ports[].tlsCert</p></dt>
<dd>
<p>The Kubernetes secret name with custom certificates to encrypt
the communication using TLS.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>ports[].tlsTrust</p></dt>
<dd>
<p>The Kubernetes secret name with the CA to expose the service
over TLS.
</p>
<div><b>Type:</b> String</div>
</dd>
</dl>

</dl>

## Resource _required-service_

### Required service diagram

<img src="images/required-service.svg" width="480"/>

### Required service examples

<table>
<tbody>
<tr><th>Skupper YAML</th></tr>
<tr><td><pre>apiVersion: skupper.io/v1alpha1
kind: RequiredService
metadata:
  name: backend
  namespace: west
spec:
  ports:
    - port: 8080</pre></td></tr>
<tr><th>Skupper CLI</th></tr>
<tr><td><pre>#
# Current
#
skupper service create backend 8080
#
# Proposed (general purpose form)
#
skupper required-service create backend
skupper required-service create-port backend 8080
#
# Proposed (simplified form for the common case)
#
skupper require backend:8080</pre></td></tr>
</tbody>
</table>

<dl>

### Required service options

<dl>
<dt><p>name</p></dt>
<dd>
<p>The service name.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>ports[]</p></dt>
<dd>
<p>A list of ports.
</p>
<div><b>Type:</b> List</div>
</dd>
<dt><p>publishNotReadyAddresses</p></dt>
<dd>
<p>If specified, skupper will not wait for pods to be ready
</p>
<div><b>Type:</b> Boolean</div>
</dd>
</dl>

### Required service port options

<dl>
<dt><p>ports[].port</p></dt>
<dd>
<p>The port number.
</p>
<div><b>Type:</b> Integer</div>
</dd>
<dt><p>ports[].name</p></dt>
<dd>
<p>The port name.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> The value of ports[].port</div>
</dd>
<dt><p>ports[].protocol</p></dt>
<dd>
<p>The protocol mapping in use for this service address.

XXX Consequences for observability.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> tcp</div>
<div><b>Choices:</b> tcp, http, http2</div>
</dd>
<dt><p>ports[].bridgeImage</p></dt>
<dd>
<p>The image to use for a bridge running external to the
skupper router
</p>
<div><b>Type:</b> String</div>
</dd>
</dl>

### Required service port TLS options

<dl>
<dt><p>ports[].generateTLSSecrets</p></dt>
<dd>
<p>If specified, the service communication will be encrypted using TLS
</p>
<div><b>Type:</b> Boolean</div>
</dd>
<dt><p>ports[].tlsCert</p></dt>
<dd>
<p>The Kubernetes secret name with custom certificates to encrypt
the communication using TLS.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>ports[].tlsTrust</p></dt>
<dd>
<p>The Kubernetes secret name with the CA to expose the service
over TLS.
</p>
<div><b>Type:</b> String</div>
</dd>
</dl>

</dl>
