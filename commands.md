# Skupper commands

#### Contents
- [Site configuration](#site-configuration)
  - [skupper site](#skupper-site)
  - [skupper site create](#skupper-site-create)
  - [skupper site update](#skupper-site-update)
  - [skupper site delete](#skupper-site-delete)
  - [skupper site status](#skupper-site-status)
- [Site linking](#site-linking)
  - [skupper token](#skupper-token)
  - [skupper token create](#skupper-token-create)
  - [skupper link](#skupper-link)
  - [skupper link create](#skupper-link-create)
  - [skupper link delete](#skupper-link-delete)
  - [skupper link status](#skupper-link-status)
- [Service exposure](#service-exposure)
  - [skupper connector](#skupper-connector)
  - [skupper connector create](#skupper-connector-create)
  - [skupper connector delete](#skupper-connector-delete)
  - [skupper connector status](#skupper-connector-status)
  - [skupper listener](#skupper-listener)
  - [skupper listener create](#skupper-listener-create)
  - [skupper listener delete](#skupper-listener-delete)
  - [skupper listener status](#skupper-listener-status)
- [Debug operations](#debug-operations)
  - [skupper debug](#skupper-debug)
  - [skupper debug dump](#skupper-debug-dump)
- [Other operations](#other-operations)
  - [skupper version](#skupper-version)

## Site configuration

### skupper site

Print help for site commands.


### skupper site create

Create a site.


#### Examples

~~~
# Create a site
skupper site create

# Create a site that can accept links from remote sites
skupper site create --create-default-link-access
~~~

#### Usage

~~~
skupper site create [OPTIONS]
~~~

#### Output

~~~
Waiting for status...
Site "<name>" is ready
~~~
#### Options

- **--name** (default [generated])

  Set the site name.  The default is the site namespace
  name.
  

- **--create-default-link-access** (default False)

  Enable external access for links from remote sites.
  

  ##### _Notes_

  _I've come to think we should name this_
  _--enable-link-access._

- **--link-access-type** (default [platform-dependent])

  Select the means of opening external access.
  
  The default is `route` on OpenShift and `loadbalancer`
  otherwise.
  

#### Errors

- **Site resource already exists**

  There is already a site resource defined for the namespace.
  

#### _Notes_

_I think it may make sense for the site CR to always have the_ 
_name "site", since it is a singleton, and have the name_ 
_option be a distinct "name override" field._ 

### skupper site update

Change site settings.

`skupper site update` has the same options as `skupper site
create`, except for those options that cannot be changed
after site creation.


#### Examples

~~~
# Change the site name
skupper site update --name headquarters

# Update multiple settings
skupper site update --name warehouse --create-default-link-access
~~~

#### Usage

~~~
skupper site update [OPTIONS]
~~~

#### Output

~~~
Waiting for update to complete...
Site "<name>" is updated
~~~
#### Errors

- **No site resource exists**

  There is no existing Skupper site resource to update.
  

### skupper site delete

Delete a site.


#### Usage

~~~
skupper site delete
~~~

#### Output

~~~
Waiting for deletion to complete...
Site "<name>" is deleted
~~~
#### Errors

- **No site resource exists**

  There is no existing Skupper site resource to delete.
  

### skupper site status

Show the current status of a site.


#### Usage

~~~
skupper site status
~~~

#### Output

~~~
Status:        Active
Name:          west
Linked sites:  1
~~~
## Site linking

### skupper token

Print help for token commands.  Currently there is just one.


### skupper token create

Create a token.


#### Usage

~~~
skupper token create TOKEN-FILE
~~~

#### Output

~~~
Token file created at <file>
The token expires after 1 use or after 15 minutes
~~~
### skupper link

Print help for link commands.


### skupper link create

Create a link.


#### Usage

~~~
skupper link create TOKEN-FILE
~~~

### skupper link delete


#### Usage

~~~
skupper link delete LINK-NAME
~~~

### skupper link status


#### Output

~~~
NAME   STATUS
link1  Active

Links from remote sites:
east
~~~
## Service exposure

### skupper connector

Print help for connector commands.


### skupper connector create

Create a connector.


#### Usage

~~~
skupper connector create CONNECTOR-NAME [OPTIONS]
~~~

#### Output

~~~
Waiting for status...
Connector "<name>" is ready
~~~
### skupper connector delete

Delete a connector.


#### Usage

~~~
skupper connector delete CONNECTOR-NAME
~~~

#### Output

~~~
Waiting for deletion to complete...
Connector "<name>" is deleted
~~~
### skupper connector status

Show the status of connectors in the current site.


#### Usage

~~~
skupper connector status
~~~

#### Output

~~~
NAME      ROUTING-KEY   SELECTOR      PORT   LISTENERS
backend   backend       app=backend   8080   1
~~~
### skupper listener

Print help for listener commands.


### skupper listener create

Create a listener.


#### Usage

~~~
skupper listener create LISTENER-NAME [OPTIONS]
~~~

#### Output

~~~
Waiting for status...
Connector "<name>" is ready
~~~
### skupper listener delete

Delete a listener.


#### Usage

~~~
skupper listener delete LISTENER-NAME
~~~

#### Output

~~~
Waiting for deletion to complete...
Listener "<name>" is deleted
~~~
### skupper listener status

Show the status of listeners in the current site.


#### Usage

~~~
skupper listener status
~~~

#### Output

~~~
NAME      ROUTING-KEY   HOST      PORT   CONNECTORS
backend   backend       backend   8080   1
~~~
## Debug operations

### skupper debug

Print help for debug commands.


### skupper debug dump

Generate a debug dump file.


#### Usage

~~~
skupper debug dump [FILE-NAME]
~~~

#### Output

~~~
Debug dump file generated at <file>
~~~
## Other operations

### skupper version


