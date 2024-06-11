---
body_class: command
links:
  - name: AccessToken resource
    url: /resources/claim.html
  - name: access-token command
    url: /commands/access-token.html
  - name: Token issue command
    url: /commands/access-token-issue.html
---

# access-token redeem command

<section>

Redeem a token in order to obtain a link to a remote site.

</section>

<section>

## Usage

~~~ shell
$ skupper access-token redeem <file> [options]
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

  Set the Skupper platform.

  | | |
  |-|-|
  | Choices | `kubernetes`, `docker`, `systemd` |
  
### Global options

- <h4 id="help">--help <span class="option-info"></span></h4>

  Display help and exit.

  
</section>
