---
body_class: object concept
refdog_object_links:
- title: Link concept
  url: /concepts/link.html
- title: AccessGrant resource
  url: /resources/access-grant.html
- title: AccessToken resource
  url: /resources/access-token.html
- title: Token command
  url: /commands/token/index.html
---

# Access token concept

<section>

An **access token** is a short-lived credential used to create a
link.  An access token contains the URL and secret code of a
corresponding **access grant**.

Access tokens have limited redemptions and limited lifespans.
By default, they can be redeemed only once, and they expire 15
minutes after being issued.  You can set custom limits by
configuring the access grant.

A site wishing to accept a link (the accepting site) creates an
access grant.  It uses the access grant to create a
corresponding access token and transfers it to a remote site (it
_issues_ a token).  The remote site submits the access token to
the accepting site (it _redeems_ the token).  If the token is
valid, the accepting site sends the remote site the TLS
credentials and connection endpoints required to create a link
to the accepting site.

<figure>
  <img src="images/access-token-1.svg"/>
  <figcaption>An access grant and corresponding access token</figcaption>
</figure>

<figure>
  <img src="images/access-token-2.svg"/>
  <figcaption>The sequence for issuing and redeeming access tokens</figcaption>
</figure>

</section>
