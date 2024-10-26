---
body_class: object resource
links:
  - name: AttachedConnector resource
    url: /resources/attachedconnector.html
---

# AttachedConnectorAnchor resource

<section>

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: AttachedConnectorAnchor
metadata:  # Metadata properties
spec:      # Spec properties
status:    # Status properties
~~~

</section>

<section>

## Metadata properties

</section>

<section>

## Spec properties

- <h3 id="connectornamespace">connectorNamespace <span class="attribute-info">string, required</span></h3>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="routingkey">routingKey <span class="attribute-info">string, required</span></h3>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="settings">settings <span class="attribute-info">object</span></h3>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

</section>

<section>

## Status properties

- <h3 id="matchinglistenercount">matchingListenerCount <span class="attribute-info">integer</span></h3>

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="status">status <span class="attribute-info">string</span></h3>

  The current state of the resource.

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="message">message <span class="attribute-info">None</span></h3>

  XXX

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

- <h3 id="conditions">conditions <span class="attribute-info">array</span></h3>

  XXX

  <table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Systemd</td></table>

</section>
