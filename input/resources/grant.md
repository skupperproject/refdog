---
body_class: resource
---

# Grant

<section>

## Overview

An offer to accept links to the local site.  A remote site
can use a claim containing the grant URL and secret to
obtain a certificate signed by the grant's certificate
authority (CA), within a certain expiration period and for a
limited number of claims.


</section>

<section>

## Spec properties

- **claims** _integer_

  _Consider maxClaims, claimsAllowed, and maxClaimsAllowed_

- **validFor** _string (duration)_

  _Look for what would be conventional for this._
  _"validFor" doesn't necessarily make it clear that it's_
  _about time: "valid for 3 uses"._

- **secret** _string_

</section>
