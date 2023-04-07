# Refdog

- [Notes](#notes)
- [Resource _site_](#resource-site)
    - [Site examples](#site-examples)
    - [Site options](#site-options)
    - [Ingress options](#ingress-options)
    - [Console options](#console-options)
    - [Service sync options](#service-sync-options)
    - [Config sync options](#config-sync-options)
    - [Controller options](#controller-options)
    - [Flow collector options](#flow-collector-options)
    - [Router options](#router-options)
- [Resource _link_](#resource-link)
    - [Link examples](#link-examples)
    - [Link options](#link-options)
- [Resource _token_](#resource-token)
    - [Token examples](#token-examples)
    - [Token options](#token-options)
- [Resource _provided-service_](#resource-provided-service)
    - [Provided service examples](#provided-service-examples)
    - [Provided service options](#provided-service-options)
- [Resource _required-service_](#resource-required-service)
    - [Required service examples](#required-service-examples)
    - [Required service options](#required-service-options)

## Notes

### Goals

- A unified declarative language ("Skupper site YAML") for creating sites,
  linking sites, and exposing services.
- A configuration model that operates uniformly across Kubernetes,
  Podman, and generated bundles, while still allowing for some
  platform specific variations.
- A simple translation from Skupper site YAML to Kubernetes custom
  resources.
- As an alternative to CRDs, allow use of Skupper site YAML as the
  content of a Kubernetes ConfigMap.
- A single source of truth for documentation of Skupper configuration.

### Clarifications

- A token is special in that it is not yet "fulfilled" - and therefore
  usable for linking - until it has an associated token file or
  secret.

### Questions

- What *are* address and host on ProvidedService?  Router tcpConnector
  stuff?

### Resources

- [Skupper syncer demo](https://github.com/grs/skupper-syncer-demo)
- [Kubernetes Service API](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/)

## Resource _site_

### Site examples

<table>
<tr><th>Skupper site YAML</th><th>Kubernetes custom resource</th></tr>
<tr><td><pre>version: 1
site:
  name: east
  ingress: none
  router-cpu-limit: 2</pre></td><td><pre>apiVersion: skupper.io/v1alpha1
kind: Site
metadata:
  name: east
  namespace: east
spec:
  ingress: none
  routerCpuLimit: 2</pre></td></tr>
<tr><th colspan="2">Skupper CLI</th></tr>
<tr><td colspan="2">skupper init --site-name east --ingress none --router-cpu-limit 2</td></tr>
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
<dt><p>annotations</p></dt>
<dd>
<p>Annotations to add to Skupper pods.
</p>
<div><b>Type:</b> Strings</div>
</dd>
<dt><p>labels</p></dt>
<dd>
<p>Labels to add to skupper pods
</p>
<div><b>Type:</b> Strings</div>
</dd>
<dt><p>create-network-policy</p></dt>
<dd>
<p>Create network policy to restrict access to Skupper services
exposed through this site to the pods currently in the
namespace.
</p>
<div><b>Type:</b> Boolean</div>
<div><b>Default:</b> n</div>
</dd>
<dt><p>enable-rest-api</p></dt>
<dd>
<p>Enable REST API
</p>
<div><b>Type:</b> Boolean</div>
</dd>
</dl>

### Ingress options

<dl>
<dt><p>ingress</p></dt>
<dd>
<p>Setup Skupper ingress to one of
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> route if available, else loadbalancer</div>
<div><b>Choices:</b> route, loadbalancer, nodeport, nginx-ingress-v1, contour-http-proxy, ingress, none</div>
</dd>
<dt><p>ingress-host</p></dt>
<dd>
<p>The hostname or alias by which the ingress route or proxy can
be reached.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>ingress-annotations</p></dt>
<dd>
<p>Annotations to add to skupper ingress
</p>
<div><b>Type:</b> Strings</div>
</dd>
</dl>

### Console options

<dl>
<dt><p>console-enabled</p></dt>
<dd>
<p>Enable skupper console must be used in conjunction with
'--enable-flow-collector' flag
</p>
<div><b>Type:</b> Boolean</div>
<div><b>Default:</b> n</div>
</dd>
<dt><p>console-auth</p></dt>
<dd>
<p>The user authentication method for the console.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> internal</div>
<div><b>Choices:</b> internal, openshift, unsecured</div>
</dd>
<dt><p>console-user</p></dt>
<dd>
<p>The console username when using internal authentication.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> admin</div>
</dd>
<dt><p>console-password</p></dt>
<dd>
<p>The console password when using internal authentication.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> [generated]</div>
</dd>
<dt><p>console-ingress</p></dt>
<dd>
<p>Determines if/how console is exposed outside cluster. If
not specified uses value of --ingress.
</p>
<div><b>Type:</b> String</div>
<div><b>Choices:</b> route, loadbalancer, nodeport, nginx-ingress-v1, contour-http-proxy, ingress, none</div>
</dd>
</dl>

### Service sync options

<dl>
<dt><p>service-sync-enabled</p></dt>
<dd>
<p>Participate in cross-site service synchronization
</p>
<div><b>Type:</b> Boolean</div>
<div><b>Default:</b> y</div>
</dd>
<dt><p>service-sync-site-ttl</p></dt>
<dd>
<p>Time after which stale services, i.e. those whose site has not been heard from, created through service-sync are removed.
</p>
<div><b>Type:</b> Duration</div>
</dd>
</dl>

### Config sync options

<dl>
<dt><p>config-sync-cpu</p></dt>
<dd>
<p>CPU request for config-sync pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>config-sync-memory</p></dt>
<dd>
<p>Memory request for config-sync pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>config-sync-cpu-limit</p></dt>
<dd>
<p>CPU limit for config-sync pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>config-sync-memory-limit</p></dt>
<dd>
<p>Memory limit for config-sync pods
</p>
<div><b>Type:</b> String</div>
</dd>
</dl>

### Controller options

<dl>
<dt><p>controller-cpu</p></dt>
<dd>
<p>CPU request for controller pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>controller-memory</p></dt>
<dd>
<p>Memory request for controller pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>controller-cpu-limit</p></dt>
<dd>
<p>CPU limit for controller pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>controller-memory-limit</p></dt>
<dd>
<p>Memory limit for controller pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>controller-node-selector</p></dt>
<dd>
<p>Node selector to control placement of controller pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>controller-pod-affinity</p></dt>
<dd>
<p>Pod affinity label matches to control placement of controller pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>controller-pod-antiaffinity</p></dt>
<dd>
<p>Pod antiaffinity label matches to control placement of controller pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>controller-ingress-host</p></dt>
<dd>
<p>Host through which node is accessible when using nodeport as ingress.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>controller-load-balancer-ip</p></dt>
<dd>
<p>Load balancer ip that will be used for controller service, if supported by cloud provider
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>controller-service-annotation</p></dt>
<dd>
<p>Annotations to add to skupper controller service
</p>
<div><b>Type:</b> Strings</div>
</dd>
</dl>

### Flow collector options

<dl>
<dt><p>flow-collector-enabled</p></dt>
<dd>
<p>Enable cross-site flow collection for the application network
</p>
<div><b>Type:</b> Boolean</div>
<div><b>Default:</b> n</div>
</dd>
<dt><p>flow-collector-record-ttl</p></dt>
<dd>
<p>Time after which terminated flow records are deleted,
i.e. those flow records that have an end time set.
</p>
<div><b>Type:</b> Duration</div>
<div><b>Default:</b> 30m</div>
</dd>
<dt><p>flow-collector-cpu</p></dt>
<dd>
<p>CPU request for flow collector pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>flow-collector-memory</p></dt>
<dd>
<p>Memory request for flow collector pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>flow-collector-cpu-limit</p></dt>
<dd>
<p>CPU limit for flow collector pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>flow-collector-memory-limit</p></dt>
<dd>
<p>Memory limit for flow collector pods
</p>
<div><b>Type:</b> String</div>
</dd>
</dl>

### Router options

<dl>
<dt><p>router-mode</p></dt>
<dd>
<p>The role of the router in the router topology.  Interior
routers do XXX.  Edge routers only do YYY.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> interior</div>
<div><b>Choices:</b> interior, edge</div>
</dd>
<dt><p>router-logging</p></dt>
<dd>
<p>Logging settings for router
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> info</div>
<div><b>Choices:</b> trace, debug, info, notice, warning, error</div>
</dd>
<dt><p>router-debug-mode</p></dt>
<dd>
<p>Enable debug mode for the router
</p>
<div><b>Type:</b> String</div>
<div><b>Choices:</b> asan, gdb</div>
</dd>
<dt><p>routers</p></dt>
<dd>
<p>Number of router replicas to start
</p>
<div><b>Type:</b> Integer</div>
</dd>
<dt><p>router-cpu</p></dt>
<dd>
<p>CPU request for router pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>router-memory</p></dt>
<dd>
<p>Memory request for router pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>router-cpu-limit</p></dt>
<dd>
<p>CPU limit for router pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>router-memory-limit</p></dt>
<dd>
<p>Memory limit for router pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>router-node-selector</p></dt>
<dd>
<p>Node selector to control placement of router pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>router-pod-affinity</p></dt>
<dd>
<p>Pod affinity label matches to control placement of router pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>router-pod-antiaffinity</p></dt>
<dd>
<p>Pod antiaffinity label matches to control placement of router pods
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>router-ingress-host</p></dt>
<dd>
<p>Host through which node is accessible when using nodeport as ingress.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>router-load-balancer-ip</p></dt>
<dd>
<p>Load balancer ip that will be used for router service, if supported by cloud provider
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>router-service-annotations</p></dt>
<dd>
<p>Annotations to add to skupper router service
</p>
<div><b>Type:</b> Strings</div>
</dd>
</dl>

</dl>

## Resource _link_

### Link examples

<table>
<tr><th>Skupper site YAML</th><th>Kubernetes custom resource</th></tr>
<tr><td><pre>version: 1
site:
  name: east
  links:
    - name: link-to-west
      token-file: west-token-1.yaml</pre></td><td><pre>apiVersion: skupper.io/v1alpha1
kind: Link
metadata:
  name: link-to-west
  namespace: east
spec:
  tokenSecret: west-token-1</pre></td></tr>
<tr><th colspan="2">Skupper CLI</th></tr>
<tr><td colspan="2">skupper link create west-token-1.yaml --namespace east --name link-to-west</td></tr>
</table>

<dl>

### Link options

<dt><p>name</p></dt>
<dd>
<p>An optional name for the link (used when deleting it).
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> [Generated]</div>
</dd>
<dt><p>token-file</p></dt>
<dd>
<p>The path to the file that contains the token.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>token-secret</p></dt>
<dd>
<p>The path to the secret that contains the token.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>cost</p></dt>
<dd>
<p>Specify a cost for this link.
</p>
<div><b>Type:</b> Integer</div>
<div><b>Default:</b> 1</div>
</dd>
</dl>

## Resource _token_

### Token examples

<table>
<tr><th>Skupper site YAML</th><th>Kubernetes custom resource</th></tr>
<tr><td><pre>version: 1
site:
  name: west
  token:
    token-file: west-token-1.yaml
    expiry: 1h</pre></td><td><pre>apiVersion: skupper.io/v1alpha1
kind: Token
metadata:
  name: west-token-1
  namespace: west
spec:
  tokenSecret: west-token-1
  expiry: 1h</pre></td></tr>
<tr><th colspan="2">Skupper CLI</th></tr>
<tr><td colspan="2">skupper token create west-token-1.yaml --namespace west --expiry 1h</td></tr>
</table>

<dl>

### Token options

<dt><p>token-file</p></dt>
<dd>
<p>The path to the file that is to contain the generated token
data.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>token-secret</p></dt>
<dd>
<p>The name of the Kubernetes secret that is to contain the
generated token data.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>expiry</p></dt>
<dd>
<p>Expiration time for claim (only valid if --token-type=claim).
</p>
<div><b>Type:</b> Duration</div>
<div><b>Default:</b> 15m</div>
</dd>
<dt><p>uses</p></dt>
<dd>
<p>Number of uses for which claim will be valid (only valid if
--token-type=claim).
</p>
<div><b>Type:</b> Integer</div>
<div><b>Default:</b> 1</div>
</dd>
<dt><p>name</p></dt>
<dd>
<p>An optional name for the remote site that will use this token
to create a link.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> skupper (?)</div>
</dd>
</dl>

## Resource _provided-service_

### Provided service examples

<table>
<tr><th>Skupper site YAML</th><th>Kubernetes custom resource</th></tr>
<tr><td><pre>version: 1
site:
  name: east
  provided-services:
    - name: backend
      ports:
        - port: 8080
          target-port: 9090</pre></td><td><pre>apiVersion: skupper.io/v1alpha1
kind: ProvidedService
metadata:
  name: backend
  namespace: east
spec:
  ports:
    - port: 8080
      targetPort: 9090</pre></td></tr>
<tr><th colspan="2">Skupper CLI</th></tr>
<tr><td colspan="2"></td></tr>
</table>

<dl>

### Provided service options

<dt><p>target-port</p></dt>
<dd>
<p>The port the target is listening on (you can also use colon to map source-port to a target-port).
</p>
<div><b>Type:</b> Strings</div>
</dd>
<dt><p>tls-trust</p></dt>
<dd>
<p>The Kubernetes secret name with the CA to expose the service
over TLS.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>publish-not-ready-addresses</p></dt>
<dd>
<p>If specified, skupper will not wait for pods to be ready
</p>
<div><b>Type:</b> Boolean</div>
<div><b>Default:</b> n</div>
</dd>
</dl>

## Resource _required-service_

### Required service examples

<table>
<tr><th>Skupper site YAML</th><th>Kubernetes custom resource</th></tr>
<tr><td><pre>version: 1
site:
  name: west
  required-services:
    - name: backend
      ports:
        - port: 8080</pre></td><td><pre>apiVersion: skupper.io/v1alpha1
kind: RequiredService
metadata:
  name: backend
  namespace: west
spec:
  ports:
    - port: 8080</pre></td></tr>
<tr><th colspan="2">Skupper CLI</th></tr>
<tr><td colspan="2"></td></tr>
</table>

<dl>

### Required service options

<dt><p>protocol</p></dt>
<dd>
<p>The protocol mapping in use for this service address.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> tcp</div>
<div><b>Choices:</b> tcp, http, http2</div>
</dd>
<dt><p>generate-tls-secrets</p></dt>
<dd>
<p>If specified, the service communication will be encrypted using TLS
</p>
<div><b>Type:</b> Boolean</div>
<div><b>Default:</b> n</div>
</dd>
<dt><p>tls-cert</p></dt>
<dd>
<p>The Kubernetes secret name with custom certificates to encrypt
the communication using TLS.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>ingress-enabled</p></dt>
<dd>
<p>Determines whether access to the Skupper service is enabled in
this site.

XXX I want a note here that says that some future iteration
might include a third state.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> Always</div>
<div><b>Choices:</b> Always, Never</div>
</dd>
<dt><p>event-channel</p></dt>
<dd>
<p>If specified, this service will be a channel for multicast events.
</p>
<div><b>Type:</b> Boolean</div>
<div><b>Default:</b> n</div>
</dd>
<dt><p>aggregate</p></dt>
<dd>
<p>The aggregation strategy to use. One of 'json' or
'multipart'. If specified requests to this service will be
sent to all registered implementations and the responses
aggregated.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> ?</div>
<div><b>Choices:</b> json, multipart</div>
</dd>
<dt><p>bridge-image</p></dt>
<dd>
<p>The image to use for a bridge running external to the skupper router
</p>
<div><b>Type:</b> String</div>
</dd>
</dl>
