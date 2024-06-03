---
body_class: resource
---

# SecuredAccess

<section>

A generic resource for exposing a workload by creating the
necessary service and ingress resources and optionally
generating TLS credentials.


</section>

<section>

## Spec properties

- **ports** _array_, _required_

- **selector** _object_, _required_

- **ca** _string_

- **certificate** _string_

- **accessType** _string_

- **options** _object_

</section>

<section>

## Status properties

- **active** _boolean_

  _Default:_ false

- **status** _string_

- **urls** _array_

- **ca** _string_

</section>
