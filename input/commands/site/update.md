---
body_class: object command
links:
  - name: Site concept
    url: /concepts/site.html
  - name: Site resource
    url: /resources/site.html
---

# Site update command

<section>

Change site settings.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>Waits for</th><td>Ready</td></table>

</section>

<section>

## Usage

~~~ shell
skupper site update [name] [options]
~~~

</section>

<section>

## Examples

~~~ console
# Update the current site to accept links
$ skupper site update --enable-link-access
Waiting for status...
Site "west" is ready.

# Update multiple settings
$ skupper site update --enable-link-access --service-account alice
~~~

</section>

<section class="attributes">

## Options

<div class="attribute">

<div class="attribute-heading"><h3 id="option-name">[name]</h3><div>string, optional</div></div>

The name of the site resource.

If not specified, the name is that of the site
associated with the current namespace.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

</div>

<div class="attribute">

<div class="attribute-heading"><h3 id="option-wait">--wait</h3><div>&lt;string&gt;</div></div>

Wait for the given status before exiting.

<table class="fields"><tr><th>Default</th><td><p><code>ready</code></p>
</td><tr><th>Choices</th><td><table class="choices"><tr><th><code>pending</code></th><td><p>Pending</p>
</td></tr><tr><th><code>configured</code></th><td><p>Configured</p>
</td></tr><tr><th><code>ready</code></th><td><p>Ready</p>
</td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>

<div class="attribute">

<div class="attribute-heading"><h3 id="option-timeout">--timeout</h3><div>&lt;string&gt; (duration)</div></div>

Raise an error if the operation does not complete in the given
period of time.

<table class="fields"><tr><th>Default</th><td><p><code>60s</code></p>
</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>

<div class="attribute">

<div class="attribute-heading"><h3 id="option-enable-link-access">--enable-link-access</h3><div>boolean</div></div>

Allow access for incoming links from remote sites.

<!-- XXX reference link access type -->

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/link-access.html">Link access concept</a></td></table>

</div>

<div class="attribute">

<div class="attribute-heading"><h3 id="option-link-access-type">--link-access-type</h3><div>&lt;string&gt;</div></div>

Configure external access for links from remote sites.

<table class="fields"><tr><th>Default</th><td><p><code>default</code></p>
</td><tr><th>Choices</th><td><table class="choices"><tr><th><code>default</code></th><td><p>Use the default link access.  On OpenShift, the default is <code>route</code>.  For other Kubernetes flavors, the default is <code>loadbalancer</code>.</p>
</td></tr><tr><th><code>route</code></th><td><p>Use an OpenShift route.  <em>OpenShift only.</em></p>
</td></tr><tr><th><code>loadbalancer</code></th><td><p>Use a Kubernetes load balancer.  <em>Kubernetes only.</em></p>
</td></tr></table></td><tr><th>Platforms</th><td>Kubernetes</td></table>

</div>

<div class="attribute">

<div class="attribute-heading"><h3 id="option-service-account">--service-account</h3><div>&lt;string&gt;</div></div>

The Kubernetes service account under which to run the
Skupper controller.

<table class="fields"><tr><th>Default</th><td><p><code>skupper-router</code></p>
</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>

<div class="attribute">

<div class="attribute-heading"><h3 id="option-namespace">--namespace</h3><div>(-n) &lt;string&gt;</div></div>

Set the namespace.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/namespace.html">Namespace concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a></td></table>

</div>

<div class="attribute">

<div class="attribute-heading"><h3 id="option-context">--context</h3><div>&lt;string&gt;</div></div>

Set the kubeconfig context.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/">Kubernetes kubeconfigs</a></td></table>

</div>

<div class="attribute">

<div class="attribute-heading"><h3 id="option-kubeconfig">--kubeconfig</h3><div>&lt;string&gt;</div></div>

Set the path to the kubeconfig file.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/">Kubernetes kubeconfigs</a></td></table>

</div>

<div class="attribute">

<div class="attribute-heading"><h3 id="option-platform">--platform</h3><div>&lt;string&gt;</div></div>

Set the Skupper platform.

<table class="fields"><tr><th>Default</th><td><p><code>kubernetes</code></p>
</td><tr><th>Choices</th><td><table class="choices"><tr><th><code>kubernetes</code></th><td><p>Kubernetes</p>
</td></tr><tr><th><code>docker</code></th><td><p>Docker</p>
</td></tr><tr><th><code>podman</code></th><td><p>Podman</p>
</td></tr><tr><th><code>linux</code></th><td><p>Linux</p>
</td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td><tr><th>See also</th><td><a href="/concepts/platform.html">Platform concept</a></td></table>

</div>

<div class="attribute">

<div class="attribute-heading"><h3 id="option-help">--help</h3><div>(-h) boolean</div></div>

Display help and exit.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</div>

</section>

<section>

## Errors

- **No site resource exists**

  There is no existing Skupper site resource to update.

</section>
