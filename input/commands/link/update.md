---
body_class: object command
links:
  - name: Link concept
    url: /concepts/link.html
  - name: Link resource
    url: /resources/link.html
---

# Link update command

<section>

Change link settings.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>Waits for</th><td>Ready</td></table>

</section>

<section>

## Usage

~~~ shell
skupper link update <name> [options]
~~~

</section>

<section>

## Examples

~~~ console
# Change the link cost
$ skupper link update west-6bfn6 --cost 10
Waiting for status...
Link "west-6bfn6" is ready.
~~~

</section>

<section>

## Options

- <div class="attribute"><h3 id="option-name">&lt;name&gt;</h3><div>string, required</div></div>

  The name of the resource to be created.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names/">Kubernetes object names</a></td></table>

- <div class="attribute"><h3 id="option-wait">--wait</h3><div>&lt;string&gt;</div></div>

  Wait for the given status before exiting.

  <table class="fields"><tr><th>Default</th><td><p><code>ready</code></p>
  </td><tr><th>Choices</th><td><table class="choices"><tr><th><code>pending</code></th><td><p>Pending</p>
  </td></tr><tr><th><code>configured</code></th><td><p>Configured</p>
  </td></tr><tr><th><code>ready</code></th><td><p>Ready</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <div class="attribute"><h3 id="option-timeout">--timeout</h3><div>&lt;string&gt; (duration)</div></div>

  Raise an error if the operation does not complete in the given
  period of time.

  <table class="fields"><tr><th>Default</th><td><p><code>60s</code></p>
  </td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <div class="attribute"><h3 id="option-cost">--cost</h3><div>&lt;integer&gt;</div></div>

  The configured routing cost of sending traffic over
  the link.

  <table class="fields"><tr><th>Default</th><td>1</td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <div class="attribute"><h3 id="option-namespace">--namespace (-n)</h3><div>&lt;string&gt;</div></div>

  Set the namespace.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="/concepts/namespace.html">Namespace concept</a>, <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/">Kubernetes namespaces</a></td></table>

- <div class="attribute"><h3 id="option-context">--context</h3><div>&lt;string&gt;</div></div>

  Set the kubeconfig context.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/">Kubernetes kubeconfigs</a></td></table>

- <div class="attribute"><h3 id="option-kubeconfig">--kubeconfig</h3><div>&lt;string&gt;</div></div>

  Set the path to the kubeconfig file.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes</td><tr><th>See also</th><td><a href="https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/">Kubernetes kubeconfigs</a></td></table>

- <div class="attribute"><h3 id="option-platform">--platform</h3><div>&lt;string&gt;</div></div>

  Set the Skupper platform.

  <table class="fields"><tr><th>Default</th><td><p><code>kubernetes</code></p>
  </td><tr><th>Choices</th><td><table class="choices"><tr><th><code>kubernetes</code></th><td><p>Kubernetes</p>
  </td></tr><tr><th><code>docker</code></th><td><p>Docker</p>
  </td></tr><tr><th><code>podman</code></th><td><p>Podman</p>
  </td></tr><tr><th><code>systemd</code></th><td><p>Systemd</p>
  </td></tr></table></td><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td><tr><th>See also</th><td><a href="/concepts/platform.html">Platform concept</a></td></table>

- <div class="attribute"><h3 id="option-help">--help (-h)</h3><div>boolean</div></div>

  Display help and exit.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

</section>
