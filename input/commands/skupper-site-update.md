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

- **name** _string_

  This is optional!  We use the site associated with the
  current namespace if the name is not given.
  
  The name of the site resource.
  

- **--enable-link-access** _boolean_

  Allow access for incoming links from remote sites.
  

- **--link-access-type** _string_

  _Default:_ default

  Configure external access for links from remote sites.
  
  Select the means of opening external access.
  
  `default` equates to `route` if the environment is
  OpenShift, otherwise `loadbalancer`.
  

- **--service-account** _string_

## Errors

- **No site resource exists**

  There is no existing Skupper site resource to update.
  
