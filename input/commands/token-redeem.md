---
body_class: command
links:
  - name: Token resource
    url: /resources/claim.html
  - name: Token command
    url: /commands/token.html
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

## Options

- <h4 id="file">file <span class="option-info">string, required</span></h4>

  The name of the token file.

  
### Context options

- <h4 id="namespace">--namespace <span class="option-info">string</span></h4>

  Select the current namespace.

  
- <h4 id="context">--context <span class="option-info">string</span></h4>

  Select the current kubeconfig context.

  
- <h4 id="platform">--platform <span class="option-info">string</span></h4>

  Select the current Skupper platform.

  
### Global options

- <h4 id="help">--help <span class="option-info">None</span></h4>

  Display help and exit.

  
</section>
