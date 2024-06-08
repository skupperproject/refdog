# Refdog

## Reference guides

- [Concepts](concepts/index.html)
- [Resources](resources/index.html)
- [Commands](commands/index.html)

## Hello World using YAML

Site West:

~~~
apiVersion: skupper.io/v1alpha1
kind: Site
metadata:
  name: west
  namespace: hello-world-west
spec:
  linkAccess: default
---
apiVersion: skupper.io/v1alpha1
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
apiVersion: skupper.io/v1alpha1
kind: Site
metadata:
  name: east
  namespace: hello-world-east
---
apiVersion: skupper.io/v1alpha1
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

## Hello World using the CLI

Site West:

~~~
skupper site create west --enable-link-access
skupper listener create backend 8080
skupper token issue ~/west-token.yaml
~~~

Site East:

~~~
skupper site create east
skupper connector create backend 8080
skupper token redeem ~/west-token.yaml
~~~
