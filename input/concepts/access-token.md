---
body_class: object concept
refdog_object_links:
- title: Token issue command
  url: /commands/token-issue.html
- title: Token redeem command
  url: /commands/token-redeem.html
- title: Link concept
  url: /concepts/link.html
---

# Access token concept

<section>

An _access token_ is a short-lived credential used to create a
link.  An access token contains the URL and secret code of a
corresponding access grant.

A site wishing to accept a link (the origin site) creates an
access grant.  It uses the access grant to create a
corresponding access token (it _issues_ a token) and transfers
it to a remote site.  The remote site submits the access token
to the origin site (it _redeems_ the token).  If the token is
valid, the origin site sends the remote site the TLS credentials
and connection endpoints required to create a link to the origin
site.

Access tokens are limited to a maximum number of uses, and they
expire shortly after they are issued.  By default, they are
restricted to a single use, and they expire after 15 minutes.
You can configure the limits on the access grant.

<figure>
  <img src="images/access-token-1.svg"/>
  <figcaption>An access grant and corresponding access token</figcaption>
</figure>

<figure>
  <img src="images/access-token-2.svg"/>
  <figcaption>The sequence for issuing and redeeming access tokens</figcaption>
</figure>

</section>
