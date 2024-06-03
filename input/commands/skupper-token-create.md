---
body_class: command
---

# skupper token create

Create a token.

## Usage

~~~ shell
$ skupper token create <file> [options]
Token file <file> created
The token expires after 1 use or after 15 minutes
~~~

## Arguments

- <h3 id="file">file <span class="argument-info">string</span></h3>

  The name of the token file.

- <h3 id="--expiry">--expiry <span class="argument-info">string (duration)</span></h3>

  _Default:_ 15m

  _Suggest **expirationPeriod**._

- <h3 id="--uses">--uses <span class="argument-info">integer</span></h3>

  _Default:_ 1

  _Suggest **claimsAllowed**._
