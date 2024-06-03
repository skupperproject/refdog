---
body_class: resource
---

# Site

<section>

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

  _Default:_ `none`

  Configure external access for links from remote sites.
  
  Select the means of opening external access.
  
  `default` equates to `route` if the environment is
  OpenShift, otherwise `loadbalancer`.
  

- **serviceAccount** _string_

  _Default:_ `skupper:skupper-controller`

  The Kubernetes service account under which to run the
  Skupper controller.
  

- **options** _array_

</section>

<section>

## Status properties

- **active** _boolean_

  _Default:_ false

- **status** _string_

- **endpoints** _array_

- **sitesInNetwork** _integer_

- **servicesInNetwork** _integer_

- **network** _array_

</section>
