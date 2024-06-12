---
body_class: concept
links:
  - name: AccessGrant resource
    url: /resources/grant.html
  - name: Access token concept
    url: /concepts/claim.html
  - name: Token issue command
    url: /commands/token-issue.html
---

# Access grant concept

<section>

Permission to redeem access tokens for links to the local
site.  A remote site can use a token containing the grant
URL and secret code to obtain a certificate signed by the
grant's certificate authority (CA), within a certain
expiration window and for a limited number of redemptions.

</section>
