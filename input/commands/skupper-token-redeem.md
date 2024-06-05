---
body_class: command
links:
  - name: Claim resource
    url: /resources/claim.html
---

# skupper token redeem

<section>

Redeem a token for a link.

XXX A verifiable assertion of permission to link to a remote
site.  A claim contains the URL and secret of an existing
grant.

A claim is redeemed for a link and a secret.

</section>

<section>

## Usage

~~~ shell
$ skupper token redeem <file> [options]
Waiting for status...
Link "<name>" is active
You can now safely delete <file>
~~~

</section>

<section>

## Arguments

- <h3 id="file">file <span class="argument-info">None</span></h3>

  The name of the token file.

</section>
