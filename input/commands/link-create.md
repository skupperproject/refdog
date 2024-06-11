---
body_class: command
links:
  - name: Link resource
    url: /resources/link.html
  - name: link command
    url: /commands/link.html
---

# link create command

<section>

Create a link.

</section>

<section>

## Usage

~~~ shell
$ skupper link create <name> <tls-secret>
Waiting for status...
Link "<name>" is ready.
~~~

</section>

<section>

## Options

- <h4 id="name">name <span class="option-info">string, required</span></h4>

  The name of the link.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
- <h4 id="tls-secret">tls-secret <span class="option-info">string, required</span></h4>

  The name of a Kubernetes secret containing TLS
  credentials. The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.

  | | |
  |-|-|
  | Platforms | Kubernetes, Docker |
  
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
