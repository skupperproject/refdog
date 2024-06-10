---
body_class: command
links:
  - name: Site concept
    url: /concepts/site.html
  - name: Site resource
    url: /resources/site.html
  - name: Site command
    url: /commands/site.html
---

# Site delete command

<section>

Delete a site.

</section>

<section>

## Usage

~~~ shell
$ skupper site delete [name]
Waiting for deletion to complete...
Site "<name>" is deleted.
~~~

</section>

<section>

## Options

- <h4 id="name">name <span class="option-info">string, optional</span></h4>

  The name of the site resource.
  
  If not specified, the name is that of the site
  associated with the current namespace.

  
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

<section>

## Errors

- **No site resource exists**

  There is no existing Skupper site resource to delete.

</section>
