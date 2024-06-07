---
body_class: command
links:
  - name: Token resource
    url: /resources/claim.html
---

# Token redeem command

<section>

Redeem a token for a link to a remote site.

A transferrable authentication token redeemable for a link
to a remote site.  A token contains the URL and secret of a
corresponding grant.

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
