---
body_class: command
links:
  - name: Site concept
    url: /concepts/site.html
  - name: Site resource
    url: /resources/site.html
---

# skupper site create

<section>

Create a site.

A site is a place where components of your application are
running.  Sites are linked to form application networks.

There can be only one site resource per namespace.

</section>

<section>

## Usage

~~~ shell
$ skupper site create <name> [options]
Waiting for status...
Site "<name>" is ready
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

## Arguments

- <h3 id="name">name <span class="argument-info">string, required</span></h3>

  A name of your choice for the Skupper site.  This name is
  displayed in the console and CLI output.

- <h3 id="--enable-link-access">--enable-link-access <span class="argument-info">boolean</span></h3>

  Allow access for incoming links from remote sites.

- <h3 id="--link-access-type">--link-access-type <span class="argument-info">string</span></h3>

  Configure external access for links from remote sites.

  _Default:_ `default`

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

  _Default:_ `skupper:skupper-controller`

</section>

<section>

## Errors

- **A site resource already exists**

  There is already a site resource defined for the namespace.

</section>
