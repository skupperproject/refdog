---
body_class: resource
---

# Site

<section>

## Overview

A [site][site] is a place where components of your application are
running.  Sites are linked to form application
[networks][network].

There can be only one site definition per namespace.

[site]: concepts.html#site
[network]: concepts.html#network


</section>

<section>

## Examples

A minimal site

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Site
metadata:
  name: east
  namespace: hello-world-east
~~~
A site configured to accept links

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Site
metadata:
  name: west
  namespace: hello-world-west
spec:
  linkAccess: default
~~~
</section>

<section>

## Spec properties

- **linkAccess** _string_

  _Default:_ none

  Configure external access for links from remote sites.
  
  Select the means of opening external access.
  
  `default` equates to `route` if the environment is
  OpenShift, otherwise `loadbalancer`.
  

- **serviceAccount** _string_

- **settings** _array_

</section>
