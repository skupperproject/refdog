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

# Site delete command

<section>

Delete a site.

</section>

<section>

## Usage

~~~ shell
$ skupper site delete [name]
Waiting for deletion to complete...
Site "<name>" is deleted.
~~~

</section>

<section>

## Options

- <h3 id="name">name <span class="attribute-info">string, optional</span></h3>

  The name of the site resource.
  
  If not specified, the name is that of the site
  associated with the current namespace.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td></table>

- <h3 id="namespace">--namespace <span class="attribute-info">string</span></h3>

  Set the namespace.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker</td><tr><th>See also</th><td><a href="/concepts/namespace.html">Namespace concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a></td></table>

- <h3 id="context">--context <span class="attribute-info">string</span></h3>

  Set the kubeconfig context.

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

  There is no existing Skupper site resource to delete.

</section>
