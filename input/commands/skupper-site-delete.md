---
body_class: command
---

# skupper site delete

Delete a site.

_See also:_ [Skupper sites]({{site_prefix}}/concepts.html#site)

## Usage

~~~ shell
$ skupper site delete [name]
Waiting for deletion to complete...
Site "<name>" is deleted
~~~

## Arguments

- <h3 id="name">name <span class="argument-info">string</span></h3>

  The name of the site resource.

## Errors

- **No site resource exists**

  There is no existing Skupper site resource to delete.
  
