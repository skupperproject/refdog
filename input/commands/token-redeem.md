---
body_class: command
links:
  - name: Token concept
    url: /concepts/claim.html
  - name: Token resource
    url: /resources/claim.html
  - name: Token issue command
    url: /commands/token-issue.html
---

# Token redeem command

<section>

Redeem a token for a link to a remote site.

</section>

<section>

## Usage

~~~ shell
$ skupper token redeem <file> [options]
Waiting for status...
Link "<name>" is active.
You can now safely delete <file>.
~~~

</section>

<section>

## Arguments

- <h3 id="file">file <span class="argument-info">string, required</span></h3>

  The name of the token file.

</section>
