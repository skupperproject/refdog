---
body_class: command
links:
  - name: Site resource
    url: /resources/site.html
  - name: Site command
    url: /commands/site.html
---

# Site update command

<section>

Change site settings.

</section>

<section>

## Usage

~~~ shell
$ skupper site update [name] [options]
Waiting for update to complete...
Site "<name>" is updated.
~~~

</section>

<section>

## Subcommands

</section>

<section>

## Examples

~~~
# Update the site to accept links
skupper site update --enable-link-access

# Update multiple settings
skupper site update --enable-link-access --service-account app1:alice
~~~

</section>

<section>

## Options

- <h4 id="name">name <span class="option-info">string, optional</span></h4>

  The name of the site resource.
  
  If not specified, the name is that of the site
  associated with the current namespace.

- <h4 id="enable-link-access">--enable-link-access <span class="option-info">boolean</span></h4>

  Allow access for incoming links from remote sites.

- <h4 id="link-access-type">--link-access-type <span class="option-info">string</span></h4>

  Configure external access for links from remote sites.

  _Default:_ `default`

  _Choices:_
  
   - `none` - No linking to this site is permitted.
   - `default` - Use the default link access.  On OpenShift, `route`
  is the default.  For other Kubernetes flavors,
  `loadbalancer` is the default.
   - `route` - Use an OpenShift route.
   - `loadbalancer` - Use a Kubernetes load balancer.

- <h4 id="service-account">--service-account <span class="option-info">string</span></h4>

  The Kubernetes service account under which to run the
  Skupper controller.

  _Default:_ `skupper:skupper-controller`

  _See also:_ [Kubernetes service accounts]({{site_prefix}}https://kubernetes.io/docs/concepts/security/service-accounts/)

### Output options

- <h4 id="output">--output <span class="option-info">string</span></h4>

  Print resources to the console instead of submitting
  them to the Skupper controller.

  _Choices:_
  
   - `json` - Produce JSON output
   - `yaml` - Produce YAML output

### Context options

- <h4 id="namespace">--namespace <span class="option-info">string</span></h4>

  Select the current namespace.

- <h4 id="context">--context <span class="option-info">string</span></h4>

  Select the current kubeconfig context.

- <h4 id="platform">--platform <span class="option-info">string</span></h4>

  Select the current Skupper platform.

### Global options

- <h4 id="help">--help <span class="option-info">None</span></h4>

  Display help and exit.

</section>

<section>

## Errors

- **No site resource exists**

  There is no existing Skupper site resource to update.

</section>
