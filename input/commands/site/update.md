---
body_class: object command
links:
  - name: Site concept
    url: /concepts/site.html
  - name: Site resource
    url: /resources/site.html
  - name: Site command
    url: /commands/site.html
---

# Site update command

<section>

Change site settings.

</section>

<section>

## Usage

~~~ shell
skupper site update [name] [options]
~~~

</section>

<section>

## Output

~~~ console
Waiting for update to complete...
Site "<name>" is updated.
~~~

</section>

<section>

## Examples

~~~
# Update the site to accept links
skupper site update --enable-link-access

# Update multiple settings
skupper site update --enable-link-access --service-account app1:alice
~~~

</section>

<section>

## Options

- <h3 id="name">name <span class="attribute-info">string, optional</span></h3>

  The name of the site resource.
  
  If not specified, the name is that of the site
  associated with the current namespace.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

- <h3 id="output">--output <span class="attribute-info">string</span></h3>

  Print the resource to the console in a structured output format
  instead of submitting it to the Skupper controller.

  <table class="fields"><tr><th>Choices</th><td><table class="choices"><tr><th><code>json</code></th><td><p>Produce JSON output</p>
  </td></tr><tr><th><code>yaml</code></th><td><p>Produce YAML output</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="timeout">--timeout <span class="attribute-info">string (duration)</span></h3>

  Raise an error if the operation does not complete in the given
  period of time.

  <table class="fields"><tr><th>Default</th><td><p><code>60s</code></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="enable-link-access">--enable-link-access <span class="attribute-info">boolean</span></h3>

  Allow access for incoming links from remote sites.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="/concepts/link-access.html">Link access concept</a></td></table>

- <h3 id="link-access-type">--link-access-type <span class="attribute-info">string</span></h3>

  Configure external access for links from remote sites.

  <table class="fields"><tr><th>Default</th><td><p><code>default</code></p>
  </td><tr><th>Choices</th><td><table class="choices"><tr><th><code>default</code></th><td><p>Use the default link access.  On OpenShift, the default is <code>route</code>.  For other Kubernetes flavors, the default is <code>loadbalancer</code>.</p>
  </td></tr><tr><th><code>route</code></th><td><p>Use an OpenShift route.  <em>OpenShift only.</em></p>
  </td></tr><tr><th><code>loadbalancer</code></th><td><p>Use a Kubernetes load balancer.  <em>Kubernetes only.</em></p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="/concepts/link-access.html">Link access concept</a>, <a href="https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer">Kubernetes load balancer services</a></td></table>

- <h3 id="service-account">--service-account <span class="attribute-info">string</span></h3>

  The Kubernetes service account under which to run the
  Skupper controller.

  <table class="fields"><tr><th>Default</th><td><p><code>skupper:skupper-controller</code></p>
  </td><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/security/service-accounts/">Kubernetes service accounts</a></td></table>

- <h3 id="namespace">--namespace <span class="attribute-info">string</span></h3>

  Set the namespace.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="/concepts/namespace.html">Namespace concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a></td></table>

- <h3 id="context">--context <span class="attribute-info">string</span></h3>

  Set the kubeconfig context.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/">Kubernetes kubeconfigs</a></td></table>

- <h3 id="kubeconfig">--kubeconfig <span class="attribute-info">string</span></h3>

  Set the path to the kubeconfig file.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/">Kubernetes kubeconfigs</a></td></table>

- <h3 id="platform">--platform <span class="attribute-info">string</span></h3>

  Set the Skupper platform.

  <table class="fields"><tr><th>Choices</th><td><table class="choices"><tr><th><code>kubernetes</code></th><td><p>Kubernetes</p>
  </td></tr><tr><th><code>docker</code></th><td><p>Docker or Podman</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="/concepts/platform.html">Platform concept</a></td></table>

- <h3 id="help">--help <span class="attribute-info"></span></h3>

  Display help and exit.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

</section>

<section>

## Errors

- **No site resource exists**

  There is no existing Skupper site resource to update.

</section>
