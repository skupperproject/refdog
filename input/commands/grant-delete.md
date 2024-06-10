---
body_class: command
links:
  - name: Grant concept
    url: /concepts/grant.html
  - name: Grant resource
    url: /resources/grant.html
  - name: Grant command
    url: /commands/grant.html
---

# Grant delete command

<section>

Delate a grant.

</section>

<section>

## Usage

~~~ shell
$ skupper grant delete <name>
Waiting for deletion to complete...
Grant "<name>" is deleted.
~~~

</section>

<section>

## Options

- <h4 id="name">name <span class="option-info">string, required</span></h4>

  The name of the grant.

  
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
