# skupper token create

Create a token.


## Usage

~~~ shell
$ skupper token create <file> [options]
Token file <file> created
The token expires after 1 use or after 15 minutes
~~~

## Arguments

- **file** _string_

  The name of the token file.
  

- **--expiry** _string (duration)_

  _Default:_ 15m

  _Look for what would be conventional for this._
  _"validFor" doesn't necessarily make it clear that it's_
  _about time: "valid for 3 uses"._

- **--uses** _integer_

  _Default:_ 1

  _Consider maxClaims, claimsAllowed, and maxClaimsAllowed_
