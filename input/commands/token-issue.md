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

- <h4 id="file">file <span class="argument-info">string, required</span></h3>

  The name of the token file.

- <h4 id="expiration-period">--expiration-period <span class="argument-info">string (duration)</span></h3>

  The period of time in which a token for this grant can
  be redeemed.

  _Default:_ `15m`

- <h4 id="redemptions-allowed">--redemptions-allowed <span class="argument-info">integer</span></h3>

  The number of times a token for this grant can be
  redeemed.

  _Default:_ 1

### Context options

- <h4 id="namespace">--namespace <span class="argument-info">string</span></h3>

  Select the current namespace.

- <h4 id="context">--context <span class="argument-info">string</span></h3>

  Select the current kubeconfig context.

- <h4 id="platform">--platform <span class="argument-info">string</span></h3>

  Select the current Skupper platform.

### Global options

- <h4 id="help">--help <span class="argument-info">None</span></h3>

  Display help and exit.

</section>

<section>

## Errors

- **Link access is not enabled**

  Link access at this site is not currently enabled.  You
  can use "skupper site update --enable-link-access" to
  enable it.

</section>
