# Refdog

- [Resource _site_](#user-content-resource-site)
    - [Site options](#user-content-site-options)
    - [Ingress options](#user-content-ingress-options)
    - [Console options](#user-content-console-options)
    - [Service sync options](#user-content-service-sync-options)
    - [Config sync options](#user-content-config-sync-options)
    - [Controller options](#user-content-controller-options)
    - [Flow collector options](#user-content-flow-collector-options)
    - [Router options](#user-content-router-options)
- [Resource _token_](#user-content-resource-token)
- [Resource _link_](#user-content-resource-link)
- [Resource _required-service_](#user-content-resource-required-service)
- [Resource _provided-service_](#user-content-resource-provided-service)

## Resource _site_

<dl>
</dl>

### Site options

<dl>
<dt><p>name</p></dt>
<dd>
<p>A name of your choice for this Skupper site.
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
<dt><p>enable-console</p></dt>
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
<dt><p>enable-service-sync</p></dt>
<dd>
<p>Participate in cross-site service synchronization (default true)
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
- name: controller-service-annotation
  default:
      type: strings
  description: |
    Annotations to add to skupper controller service
</p>
<div><b>Type:</b> String</div>
</dd>
</dl>

### Flow collector options

<dl>
<dt><p>enable-flow-collector</p></dt>
<dd>
<p>Enable cross-site flow collection for the application network
</p>
<div><b>Type:</b> Boolean</div>
</dd>
<dt><p>flow-collector-record-ttl</p></dt>
<dd>
<p>Time after which terminated flow records are deleted, i.e. those flow records that have an end time set. Default is 30 minutes.
</p>
<div><b>Type:</b> Duration</div>
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

## Resource _token_

<dl>
<dt><p>expiry</p></dt>
<dd>
<p>Expiration time for claim (only valid if --token-type=claim) (default 15m0s)
</p>
<div><b>Type:</b> Duration</div>
</dd>
<dt><p>name</p></dt>
<dd>
<p>Provide a specific identity as which connecting skupper installation will be authenticated (default "skupper")
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>uses</p></dt>
<dd>
<p>Number of uses for which claim will be valid (only valid if --token-type=claim) (default 1)
</p>
<div><b>Type:</b> Integer</div>
</dd>
</dl>

## Resource _link_

<dl>
<dt><p>cost</p></dt>
<dd>
<p>Specify a cost for this link.
</p>
<div><b>Type:</b> Integer</div>
<div><b>Default:</b> 1</div>
</dd>
<dt><p>name</p></dt>
<dd>
<p>Provide a specific name for the link (used when deleting it)
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> [Generated]</div>
</dd>
</dl>

## Resource _required-service_

<dl>
<dt><p>aggregate</p></dt>
<dd>
<p>The aggregation strategy to use. One of 'json' or 'multipart'. If specified requests to this service will be sent to all registered implementations and the responses aggregated.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>bridge-image</p></dt>
<dd>
<p>The image to use for a bridge running external to the skupper router
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>enable-ingress</p></dt>
<dd>
<p>Determines whether access to the Skupper service is enabled in this site. Valid values are Always (default) or Never.
</p>
<div><b>Type:</b> String</div>
</dd>
<dt><p>event-channel</p></dt>
<dd>
<p>If specified, this service will be a channel for multicast events.
</p>
<div><b>Type:</b> Boolean</div>
</dd>
<dt><p>generate-tls-secrets</p></dt>
<dd>
<p>If specified, the service communication will be encrypted using TLS
</p>
<div><b>Type:</b> Boolean</div>
</dd>
<dt><p>protocol</p></dt>
<dd>
<p>The protocol mapping in use for this service address.
</p>
<div><b>Type:</b> String</div>
<div><b>Default:</b> tcp</div>
<div><b>Choices:</b> tcp, http, http2</div>
</dd>
<dt><p>tls-cert</p></dt>
<dd>
<p>The Kubernetes secret name with custom certificates to encrypt
the communication using TLS.
</p>
<div><b>Type:</b> String</div>
</dd>
</dl>

## Resource _provided-service_

<dl>
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
