---
body_class: command
---

# skupper site create

Create a site.

A [site][site] is a place where components of your application are
running.  Sites are linked to form application
[networks][network].

There can be only one site definition per namespace.

[site]: concepts.html#site
[network]: concepts.html#network



## Usage

~~~ shell
$ skupper site create <name> [options]
Waiting for status...
Site "<name>" is ready
~~~

## Examples

~~~
# Create a site
skupper site create west

# Create a site that can accept links from remote sites
skupper site create west --link-access default
~~~

## Arguments

- **name** _string_

  A name of your choice for the Skupper site.  This name is
  displayed in the console and CLI output.
  

- **--enable-link-access** _boolean_

  Allow access for incoming links from remote sites.
  

- **--link-access-type** _string_

  _Default:_ default

  Configure external access for links from remote sites.
  
  Select the means of opening external access.
  
  `default` equates to `route` if the environment is
  OpenShift, otherwise `loadbalancer`.
  

- **--service-account** _string_

## Errors

- **A site resource already exists**

  There is already a site resource defined for the namespace.
  
