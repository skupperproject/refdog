---
body_class: command
links:
  - name: Grant concept
    url: /concepts/grant.html
  - name: Grant resource
    url: /resources/grant.html
  - name: Token redeem command
    url: /commands/token-redeem.html
---

# Token issue command

<section>

Create a grant and then use it to create a token file that
can be redeemed for a link to the local site.

</section>

<section>

## Usage

~~~ shell
$ skupper token issue <file> [options]
Waiting for status...
Grant "<name>" is ready.
Token file <file> created.

Transfer this file to a remote site. At the remote site,
create a link to this site using the 'skupper token redeem'
command:

   $ skupper token redeem <file>

The token expires after 1 use or after 15 minutes.
~~~

</section>

<section>

## Examples

~~~
# Issue a token
skupper token issue ~/token.yaml

# Issue a token with non-default limits
skupper token issue ~/token.yaml --expiration-period 24h --redemptions-allowed 3
~~~

</section>

<section>

## Options

</section>

<section>

## Errors

- **Link access is not enabled**

  Link access at this site is not currently enabled.  You
  can use "skupper site update --enable-link-access" to
  enable it.

</section>
