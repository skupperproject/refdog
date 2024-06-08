---
body_class: command
links:
  - name: Site concept
    url: /concepts/site.html
  - name: Site resource
    url: /resources/site.html
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

- <h3 id="name">name <span class="argument-info">string, optional</span></h3>

  The name of the site resource.
  
  If not specified, the name is that of the site
  associated with the current namespace.

</section>

<section>

## Context options

- <h3 id="namespace">--namespace <span class="argument-info">string</span></h3>

  Select the current namespace.

- <h3 id="context">--context <span class="argument-info">string</span></h3>

  Select the current kubeconfig context.

- <h3 id="platform">--platform <span class="argument-info">string</span></h3>

  Select the current Skupper platform.

</section>

<section>

## Global options

- <h3 id="help">--help <span class="argument-info">None</span></h3>

  Display help and exit.

</section>

<section>

## Errors

- **No site resource exists**

  There is no existing Skupper site resource to delete.

</section>
