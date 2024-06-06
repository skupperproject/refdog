---
body_class: command
links:
  - name: AccessGrant resource
    url: /resources/grant.html
---

# Token create command

<section>

Create a token.

</section>

<section>

## Usage

~~~ shell
$ skupper token create <file> [options]
Token file <file> created
The token expires after 1 use or after 15 minutes
~~~

</section>

<section>

## Arguments

- <h3 id="file">file <span class="argument-info">string</span></h3>

  The name of the token file.

- <h3 id="--expiration-period">--expiration-period <span class="argument-info">string (duration)</span></h3>

  The period of time in which an access token for this
  grant can be redeemed.

  _Default:_ `15m`

- <h3 id="--redemptions-allowed">--redemptions-allowed <span class="argument-info">integer</span></h3>

  The number of times an access token for this grant can
  be redeemed.

  _Default:_ 1

</section>
