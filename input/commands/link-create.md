---
body_class: command
links:
  - name: Link concept
    url: /concepts/link.html
  - name: Link resource
    url: /resources/link.html
  - name: Link command
    url: /commands/link.html
---

# Link create command

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

  
- <h4 id="tls-secret">tls-secret <span class="option-info">string, required</span></h4>

  The name of a Kubernetes secret containing TLS
  credentials. The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.

  
### Context options

- <h4 id="namespace">--namespace <span class="option-info">string</span></h4>

  Select the current namespace.

  
- <h4 id="context">--context <span class="option-info">string</span></h4>

  Select the current kubeconfig context.

  
- <h4 id="platform">--platform <span class="option-info">string</span></h4>

  Set the Skupper platform.

  | | |
  |-|-|
  | Choices | `kubernetes`, `docker`, `systemd` |
  
### Global options

- <h4 id="help">--help <span class="option-info"></span></h4>

  Display help and exit.

  
</section>
