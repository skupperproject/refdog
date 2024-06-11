---
body_class: command
links:
  - name: Site resource
    url: /resources/site.html
  - name: site command
    url: /commands/site.html
---

# site create command

<section>

Create a site.

</section>

<section>

## Usage

~~~ shell
$ skupper site create <name> [options]
Waiting for status...
Site "<name>" is ready.
~~~

</section>

<section>

## Examples

~~~
# Create a site
skupper site create west

# Create a site that can accept links from remote sites
skupper site create west --enable-link-access
~~~

</section>

<section>

## Options

- <h4 id="name">name <span class="option-info">string, required</span></h4>

  A name of your choice for the Skupper site.  This name is
  displayed in the console and CLI output.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h4 id="enable-link-access">--enable-link-access <span class="option-info">boolean</span></h4>

  Allow access for incoming links from remote sites.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h4 id="link-access-type">--link-access-type <span class="option-info">string</span></h4>

  Configure external access for links from remote sites.

  | | |
  |-|-|
  | Default | `default` |
  | Choices | <table><tr><td><code>default</code></td><td>Use the default link access.  On OpenShift, the default is `route`.  For other Kubernetes flavors, the default is `loadbalancer`.</td></tr><tr><td><code>route</code></td><td>Use an OpenShift route.  _OpenShift only._</td></tr><tr><td><code>loadbalancer</code></td><td>Use a Kubernetes load balancer.  _Kubernetes only._</td></tr></table> |
  | Platforms | Kubernetes, Docker |
  
- <h4 id="service-account">--service-account <span class="option-info">string</span></h4>

  The Kubernetes service account under which to run the
  Skupper controller.

  | | |
  |-|-|
  | Default | `skupper:skupper-controller` |
  | Platforms | Kubernetes |
  | See also | [Kubernetes service accounts]({{site_prefix}}https://kubernetes.io/docs/concepts/security/service-accounts/) |
  
### Output options

- <h4 id="output">--output <span class="option-info">string</span></h4>

  Print resources to the console instead of submitting
  them to the Skupper controller.

  | | |
  |-|-|
  | Choices | <table><tr><td><code>json</code></td><td>Produce JSON output</td></tr><tr><td><code>yaml</code></td><td>Produce YAML output</td></tr></table> |
  | Platforms | Kubernetes, Docker |
  
### Context options

- <h4 id="namespace">--namespace <span class="option-info">string</span></h4>

  Select the current namespace.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h4 id="context">--context <span class="option-info">string</span></h4>

  Select the current kubeconfig context.

  | | |
  |-|-|
  | Platforms | Kubernetes |
  
- <h4 id="platform">--platform <span class="option-info">string</span></h4>

  Set the Skupper platform.

  | | |
  |-|-|
  | Choices | <table><tr><td><code>kubernetes</code></td><td>Kubernetes</td></tr><tr><td><code>docker</code></td><td>Docker or Podman</td></tr></table> |
  | Platforms | Kubernetes, Docker |
  
### Global options

- <h4 id="help">--help <span class="option-info"></span></h4>

  Display help and exit.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
</section>

<section>

## Errors

- **A site resource already exists**

  There is already a site resource defined for the namespace.

</section>
