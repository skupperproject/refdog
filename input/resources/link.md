---
body_class: resource
---

# Link

<section>

A [link][link] is a site-to-site communication channel. Links
serve as a transport for application connections and requests.

[link]: concepts.html#link


</section>

<section>

## Examples

A typical link definition

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: Link
metadata:
  name: link-to-west
  namespace: hello-world-east
spec:
  [...]
~~~
</section>

<section>

## Spec properties

- **tlsSecret** _string_

  The name of a Kubernetes secret containing TLS
  credentials. The secret contains the trusted server
  certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  

- **cost** _integer_

- **interRouter** _object_, _required_

- **edge** _object_, _required_

- **noClientAuth** _boolean_

  _Default:_ false

</section>

<section>

## Status properties

- **configured** _boolean_

  _Default:_ false

- **active** _boolean_

  _Default:_ false

- **status** _string_

- **url** _string_

- **site** _string_

</section>
