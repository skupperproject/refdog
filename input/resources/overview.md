# Skupper resource overview

- These are Kubernetes custom resources
- They are used for non-Kube platforms as well
- Some resource fields are "updatable" - you can change their values
  without recreating the resource.

## Site configuration resources

## Site linking resources

- You may want to use the CLI (or some other automation) to do the
  linking part

## Service exposure resources

## Hello World using YAML

Site West:

~~~
apiVersion: skupper.io/v2alpha1
kind: Site
metadata:
  name: west
  namespace: hello-world-west
spec:
  linkAccess: default
---
apiVersion: skupper.io/v2alpha1
kind: Listener
metadata:
  name: backend
  namespace: hello-world-west
spec:
  routingKey: backend
  port: 8080
  host: backend
~~~

~~~
skupper token issue ~/west-token.yaml
~~~

Site East:

~~~
apiVersion: skupper.io/v2alpha1
kind: Site
metadata:
  name: east
  namespace: hello-world-east
---
apiVersion: skupper.io/v2alpha1
kind: Connector
metadata:
  name: backend
  namespace: hello-world-east
spec:
  routingKey: backend
  port: 8080
  selector: app=backend
~~~

~~~
skupper token redeem ~/west-token.yaml
~~~
