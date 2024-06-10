---
body_class: command
links:
  - name: Site concept
    url: /concepts/site.html
  - name: Site resource
    url: /resources/site.html
  - name: Site command
    url: /commands/site.html
---

# Site create command

<section>

Create a site.

</section>

<section>

## Usage

~~~ shell
$ skupper site create <name> [options]
Waiting for status...
Site "<name>" is ready.
~~~

</section>

<section>

## Examples

~~~
# Create a site
skupper site create west

# Create a site that can accept links from remote sites
skupper site create west --enable-link-access
~~~

</section>

<section>

## Options

- <h4 id="name">name <span class="option-info">string, required</span></h4>

  A name of your choice for the Skupper site.  This name is
  displayed in the console and CLI output.

  
- <h4 id="enable-link-access">--enable-link-access <span class="option-info">boolean</span></h4>

  Allow access for incoming links from remote sites.

  
- <h4 id="link-access-type">--link-access-type <span class="option-info">string</span></h4>

  Configure external access for links from remote sites.

  | | |
  |-|-|
  | Default | `default` |
  | Choices | `none`, `default`, `route`, `loadbalancer` |
  
- <h4 id="service-account">--service-account <span class="option-info">string</span></h4>

  The Kubernetes service account under which to run the
  Skupper controller.

  | | |
  |-|-|
  | Default | `skupper:skupper-controller` |
  | See also | [Kubernetes service accounts]({{site_prefix}}https://kubernetes.io/docs/concepts/security/service-accounts/) |
  
### Output options

- <h4 id="output">--output <span class="option-info">string</span></h4>

  Print resources to the console instead of submitting
  them to the Skupper controller.

  | | |
  |-|-|
  | Choices | `json`, `yaml` |
  
### Context options

- <h4 id="namespace">--namespace <span class="option-info">string</span></h4>

  Select the current namespace.

  
- <h4 id="context">--context <span class="option-info">string</span></h4>

  Select the current kubeconfig context.

  
- <h4 id="platform">--platform <span class="option-info">string</span></h4>

  Select the current Skupper platform.

  | | |
  |-|-|
  | Choices | `kubernetes`, `docker`, `systemd` |
  
### Global options

- <h4 id="help">--help <span class="option-info">None</span></h4>

  Display help and exit.

  
</section>

<section>

## Errors

- **A site resource already exists**

  There is already a site resource defined for the namespace.

</section>
