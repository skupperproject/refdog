---
body_class: resource
---

# Claim

<section>

A verifiable assertion of permission to link to a remote
site.  A claim contains the URL and secret of a previous
grant.


</section>

<section>

## Spec properties

- **url** _string_, _required_

- **secret** _string_, _required_

- **ca** _string_, _required_

</section>

<section>

## Status properties

- **claimed** _boolean_

  _Default:_ false

  _Suggest accepted._

- **status** _string_

</section>
