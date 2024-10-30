---
body_class: object resource
links:
  - name: AttachedConnector resource
    url: /resources/attachedconnector.html
---

# AttachedConnectorAnchor resource

<section>

~~~ yaml
apiVersion: skupper.io/v2alpha1
kind: AttachedConnectorAnchor
~~~

</section>

<section>

## Metadata properties

</section>

<section>

## Spec properties

- <div class="attribute"><h3 id="spec-connectornamespace">connectorNamespace</h3><div>string, required</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="spec-routingkey">routingKey</h3><div>string, required</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="spec-settings">settings</h3><div>object</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</section>

<section>

## Status properties

- <div class="attribute"><h3 id="status-matchinglistenercount">matchingListenerCount</h3><div>integer</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="status-status">status</h3><div>string</div></div>

  The current state of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="status-message">message</h3><div>None</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

- <div class="attribute"><h3 id="status-conditions">conditions</h3><div>array</div></div>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</section>
