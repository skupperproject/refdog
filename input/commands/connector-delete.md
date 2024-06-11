---
body_class: command
links:
  - name: Connector resource
    url: /resources/connector.html
  - name: connector command
    url: /commands/connector.html
  - name: listener delete command
    url: /commands/listener-delete.html
---

# connector delete command

<section>

Delete a connector.

</section>

<section>

## Usage

~~~ shell
$ skupper connector delete <name>
Waiting for deletion to complete...
Connector "<name>" is deleted.
~~~

</section>

<section>

## Options

- <h4 id="name">name <span class="option-info">string, required</span></h4>

  The name of the connector resource.

  | | |
  |-|-|
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
