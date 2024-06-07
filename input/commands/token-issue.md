---
body_class: command
links:
  - name: Grant concept
    url: /concepts/grant.html
  - name: Grant resource
    url: /resources/grant.html
  - name: Grant resource
    url: /resources/grant.html
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
Token file <file> created
The token expires after 1 use or after 15 minutes
~~~

</section>

<section>

## Arguments

- <h3 id="file">file <span class="argument-info">string</span></h3>

  The name of the token file.

- <h3 id="--expiration-period">--expiration-period <span class="argument-info">string (duration)</span></h3>

  The period of time in which a token for this grant can
  be redeemed.

  _Default:_ `15m`

- <h3 id="--redemptions-allowed">--redemptions-allowed <span class="argument-info">integer</span></h3>

  The number of times a token for this grant can be
  redeemed.

  _Default:_ 1

</section>
