# Skupper commands

#### Contents

- [Global options](#global-options)
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

## Global options

- **--help**

  Display help and exit.
  

- **--context** _string_

  Select the kubeconfig context.
  

- **--namespace** _string_

  Select the Kubernetes namespace.
  

- **--platform** _string_

  Select the Skupper platform.
  

## Site configuration

### skupper site

Display help for site commands and exit.


### skupper site create

Create a site.


#### Usage

~~~ shell
$ skupper site create NAME [options]
Waiting for status...
Site "<name>" is ready
~~~

#### Examples

~~~
# Create a site
skupper site create west

# Create a site that can accept links from remote sites
skupper site create west --enable-link-access
~~~

#### Options

- **--enable-link-access** (default: false)

  Enable external access for links from remote sites.
  

- **--link-access-type** _string_ (default: _platform dependent_)

  Select the means of opening external access.
  
  The default is `route` on OpenShift and `loadbalancer`
  otherwise.
  

- **--service-account** _string_ (default: _I don't know_)

#### Errors

- **Site resource already exists**

  There is already a site resource defined for the namespace.
  

### skupper site update

Change site settings.


#### Usage

~~~ shell
$ skupper site update NAME [options]
Waiting for update to complete...
Site "<name>" is updated
~~~

#### Examples

~~~
# Update the site to accept links
skupper site update west --enable-link-access

# Update multiple settings
skupper site update west --enable-link-access --link-access-type loadbalancer
~~~

#### Options

- **--enable-link-access** (default: false)

  Enable external access for links from remote sites.
  

- **--link-access-type** _string_ (default: _platform dependent_)

  Select the means of opening external access.
  
  The default is `route` on OpenShift and `loadbalancer`
  otherwise.
  

- **--service-account** _string_ (default: _I don't know_)

#### Errors

- **No site resource exists**

  There is no existing Skupper site resource to update.
  

### skupper site delete

Delete a site.


#### Usage

~~~ shell
$ skupper site delete NAME
Waiting for deletion to complete...
Site "<name>" is deleted
~~~

#### Errors

- **No site resource exists**

  There is no existing Skupper site resource to delete.
  

### skupper site status

Show the current status of a site.


#### Usage

~~~ shell
$ skupper site status
NAME   STATUS   SITES-IN-NETWORK   SERVICES-IN-NETWORK
west   Ready    1                  0
~~~

#### _Notes_

_What is services-in-network?  Is that the total number of_ 
_unique routing keys defined by connectors?  Or listeners?_ 
_Or listeners plus connectors (not the orphans), grouped by_ 
_routing key?_ 

## Site linking

### skupper token

Display help for token commands and exit.  Currently there
is only one token command.


### skupper token create

Create a token.


#### Usage

~~~ shell
$ skupper token create FILE [options]
Token file created at <file>
The token expires after 1 use or after 15 minutes
~~~

#### Options

- **--expiry** _duration_ (default: 15m)

- **--uses** _integer_ (default: 1)

### skupper link

Display help for link commands and exit.


### skupper link create

Create a link.


#### Usage

~~~ shell
$ skupper link create FILE [options]
Waiting for status...
Link "<name>" is active
You can now safely delete <file>
~~~

#### Options

- **--cost** _integer_ (default: 1)

### skupper link delete


#### Usage

~~~ shell
$ skupper link delete NAME
~~~

### skupper link status


## Service exposure

### skupper connector

Display help for connector commands and exit.


### skupper connector create

Create a connector.


#### Usage

~~~ shell
$ skupper connector create NAME [options]
Waiting for status...
Connector "<name>" is ready
~~~

#### Examples

~~~
# Create a connector for a database
skupper connector create database --workload deployment/postgresql --port 5432
~~~

#### Options

- **--routing-key** _string_ (default: _value of NAME_)

- **--port** _integer_

- **--workload** _string_

- **--selector** _string_

- **--host** _string_

### skupper connector delete

Delete a connector.


#### Usage

~~~ shell
$ skupper connector delete NAME
Waiting for deletion to complete...
Connector "<name>" is deleted
~~~

### skupper connector status

Show the status of connectors in the current site.


#### Usage

~~~ shell
$ skupper connector status
NAME      ROUTING-KEY   SELECTOR         HOST   PORT   MATCHING-LISTENERS
backend   backend       app=backend      -      8080   1
database  database      app=postgresql   -      5342   1
~~~

### skupper listener

Display help for listener commands and exit.


### skupper listener create

Create a listener.


#### Usage

~~~ shell
$ skupper listener create NAME [options]
Waiting for status...
Listener "<name>" is ready
~~~

#### Examples

~~~
# Create a listener for a database
skupper listener create database --host database --port 5432
~~~

#### Options

- **--routing-key** _string_ (default: _value of NAME_)

- **--host** _string_

- **--port** _integer_

### skupper listener delete

Delete a listener.


#### Usage

~~~ shell
$ skupper listener delete NAME
Waiting for deletion to complete...
Listener "<name>" is deleted
~~~

### skupper listener status

Show the status of listeners in the current site.


#### Usage

~~~ shell
$ skupper listener status
NAME      ROUTING-KEY   HOST      PORT   MATCHING-CONNECTORS
backend   backend       backend   8080   1
database  database      database  5432   1
~~~

## Debug operations

### skupper debug

Display help for debug commands and exit.


### skupper debug dump

Generate a debug dump file.


#### Usage

~~~ shell
$ skupper debug dump [FILE]
Debug dump file generated at <file>
~~~

## Other operations

### skupper version


