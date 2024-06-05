---
body_class: command
links:
  - name: Grant resource
    url: /resources/grant.html
---

# skupper token create

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

- <h3 id="--valid-for">--valid-for <span class="argument-info">string (duration)</span></h3>

  _Default:_ `15m`

- <h3 id="--claims">--claims <span class="argument-info">integer</span></h3>

  _Default:_ 1

</section>
