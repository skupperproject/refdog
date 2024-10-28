---
body_class: object command
---

# Version command

<section>

Display versions of Skupper components.

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

</section>

<section>

## Usage

~~~ shell
skupper version [options]
~~~

</section>

<section>

## Examples

~~~ console
$ skupper version
COMPONENT    VERSION   IMAGE                                   // ID?
cli          2.0.0     -
controller   2.0.0     quay.io/skupper/controller:2.0.0
router       3.0.0     quay.io/skupper/router:3.0.0            // Was skupper-router
~~~

</section>

<section>

## Options

- <div class="attribute"><h3 id="option-namespace">--namespace</h3><div>&lt;string&gt;</div></div>

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

- <div class="attribute"><h3 id="option-help">--help</h3><div>boolean</div></div>

  Display help and exit.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

</section>
