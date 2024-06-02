---
body_class: resource
---

# LinkAccess

<section>

## Overview

A point of external access for links from remote sites.  A
LinkAccess configures the router to accept inter-router
links and creates the Kubernetes resources for external
access.


</section>

<section>

## Examples

A typical link access definition

~~~ yaml
apiVersion: skupper.io/v1alpha1
kind: LinkAccess
metadata:
  name: skupper-router
spec:
  roles:
  - role: inter-router
    port: 55671
  - role: edge
    port: 45671
  tlsCredentials: skupper-site-server
~~~
</section>

<section>

## Spec properties

- **roles** _array_

- **tlsCredentials** _string_

  The name of a Kubernetes secret containing the trusted
  server certificate (typically a CA).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  

- **ca** _string_

  The name of a Kubernetes secret containing a CA for
  generating TLS credentials.  If the `tlsCredentials`
  property is not set, the controller uses `ca` to
  generate them.
  

  _Consider tlsCA.  And "ca" often means "this is what I trust".  This thing has a different meaning._

- **bindHost** _string_

  _Just host?  What does "bind" do here to clarify?  I have a related attribute on site: linkAccessHost._

- **subjectAlternativeNames** _array_

- **options** _object_

- **accessType** _string_

</section>
