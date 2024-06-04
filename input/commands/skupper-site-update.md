---
body_class: command
links:
  - name: Site resource
    url: /resources/site.html
---

# skupper site update

<section>

Change site settings.

The name argument is optional for update.

</section>

<section>

## Usage

~~~ shell
$ skupper site update [name] [options]
Waiting for update to complete...
Site "<name>" is updated
~~~

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

## Arguments

- <h3 id="name">name <span class="argument-info">string</span></h3>

  This is optional!  We use the site associated with the
  current namespace if the name is not given.
  
  The name of the site resource.

- <h3 id="--enable-link-access">--enable-link-access <span class="argument-info">boolean</span></h3>

  Allow access for incoming links from remote sites.

- <h3 id="--link-access-type">--link-access-type <span class="argument-info">string</span></h3>

  Configure external access for links from remote sites.

  _Default:_ default

  _Choices:_

    - `none` - No link access.
    - `default` - Use the default link access.  On OpenShift, `route`
is the default.  For other Kubernetes flavors,
`loadbalancer` is the default.
    - `route` - Use an OpenShift route.
    - `loadbalancer` - Use a Kubernetes load balancer.

- <h3 id="--service-account">--service-account <span class="argument-info">string</span></h3>

  The Kubernetes service account under which to run the
  Skupper controller.

  _Default:_ skupper:skupper-controller

  _Choices:_


</section>

<section>

## Errors

- **No site resource exists**

  There is no existing Skupper site resource to update.

</section>
