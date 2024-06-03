---
body_class: command
---

# skupper site update

Change site settings.

The name argument is optional for update.

## Usage

~~~ shell
$ skupper site update [name] [options]
Waiting for update to complete...
Site "<name>" is updated
~~~

## Examples

~~~
# Update the site to accept links
skupper site update --enable-link-access

# Update multiple settings
skupper site update --enable-link-access --service-account app1:alice
~~~

## Arguments

- <h3 id="name">name <span class="argument-info">string</span></h3>

  This is optional!  We use the site associated with the
  current namespace if the name is not given.
  
  The name of the site resource.

- <h3 id="--enable-link-access">--enable-link-access <span class="argument-info">boolean</span></h3>

  Allow access for incoming links from remote sites.

- <h3 id="--link-access-type">--link-access-type <span class="argument-info">string</span></h3>

  Configure external access for links from remote sites.

  _Default:_ default

- <h3 id="--service-account">--service-account <span class="argument-info">string</span></h3>

  The Kubernetes service account under which to run the
  Skupper controller.

  _Default:_ `skupper:skupper-controller`

## Errors

- **No site resource exists**

  There is no existing Skupper site resource to update.
  
