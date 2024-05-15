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

A [site][site] is a place where components of your application are
running.  Sites are linked to form application
[networks][network].

There can be only one site definition per namespace.

[site]: concepts.html#site
[network]: concepts.html#network



#### Usage

~~~ shell
$ skupper site create <name> [options]
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

#### Arguments

- **name** _string_

  A name of your choice for the Skupper site.  This name is
  displayed in the console and CLI output.
  

- **--enable-link-access** _boolean_

  _Default:_ false

  Enable external access for links from remote sites.
  

- **--link-access-type** _string_

  _Default:_ `route` if the environment is OpenShift, otherwise
`loadbalancer`


  Select the means of opening external access.
  

- **--link-access-host** _string_

  The host or IP address at which to expose link access.
  

- **--service-account** _string_

#### Errors

- **Site resource already exists**

  There is already a site resource defined for the namespace.
  

### skupper site update

Change site settings.


#### Usage

~~~ shell
$ skupper site update <name> [options]
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

#### Arguments

- **name** _string_

  The name of the site resource.
  

- **--enable-link-access** _boolean_

  _Default:_ false

  Enable external access for links from remote sites.
  

- **--link-access-type** _string_

  _Default:_ `route` if the environment is OpenShift, otherwise
`loadbalancer`


  Select the means of opening external access.
  

- **--link-access-host** _string_

  The host or IP address at which to expose link access.
  

- **--service-account** _string_

#### Errors

- **No site resource exists**

  There is no existing Skupper site resource to update.
  

### skupper site delete

Delete a site.


#### Usage

~~~ shell
$ skupper site delete <name>
Waiting for deletion to complete...
Site "<name>" is deleted
~~~

#### Arguments

- **name** _string_

  The name of the site resource.
  

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

_Notes: What is services-in-network?  Is that the total number of_ 
_Notes: unique routing keys defined by connectors?  Or listeners?_ 
_Notes: Or listeners plus connectors (not the orphans), grouped by_ 
_Notes: routing key?_ 

## Site linking

### skupper token

Display help for token commands and exit.  Currently there
is only one token command.


### skupper token create

Create a token.


#### Usage

~~~ shell
$ skupper token create <file> [options]
Token file <file> created
The token expires after 1 use or after 15 minutes
~~~

#### Arguments

- **file** _string_

  The name of the token file.
  

- **--expiry** _duration_

  _Default:_ 15m

- **--uses** _int_

  _Default:_ 1

### skupper link

Display help for link commands and exit.


### skupper link create

Create a link.

A [link][link] is a site-to-site communication channel. Links
serve as a transport for application connections and requests.

[link]: concepts.html#link



#### Usage

~~~ shell
$ skupper link create <file> [options]
Waiting for status...
Link "<name>" is active
You can now safely delete <file>
~~~

#### Arguments

- **file**

  The name of the token file.
  

- **--cost** _integer_

### skupper link delete


#### Usage

~~~ shell
$ skupper link delete <name>
~~~

### skupper link status


## Service exposure

### skupper connector

Display help for connector commands and exit.


### skupper connector create

Create a connector.

A [connector][connector] binds local servers to listeners in
remote sites.

Each namespace can contain multiple connector definitions.

[connector]: concepts.html#connector



#### Usage

~~~ shell
$ skupper connector create <name> [options]
Waiting for status...
Connector "<name>" is ready
~~~

#### Examples

~~~
# Create a connector for a database
skupper connector create database --workload deployment/postgresql --port 5432
~~~

#### Arguments

- **name** _string_

  The name of the connector resource.
  

- **--routing-key** _string_

  _Default:_ _value of name_

  The identifier used to route traffic from listeners to
  connectors.  To connect to a service at a remote site, the
  listener and connector must have matching routing keys.
  

- **--workload** _string_

- **--port** _integer_

  The port number of the server listener.
  

- **--selector** _string_

  A Kubernetes [label selector][selector] for targeting server
  pods.
  
  [selector]: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors
  

- **--host** _string_

  The hostname or IP address of the server.  This is an
  alternative to `selector` for specifying the target
  server.
  

- **--enable-t-l-s** _boolean_

  _Default:_ false

  Use TLS to encrypt communication between the router and servers.
  
  By default, the TLS credentials are generated and stored in
  a secret at XXX.
  

- **--tls-credentials** _string_

  The name of a Kubernetes secret containing TLS
  credentials.  The secret contains the trusted server
  certificate (typically a CA certificate).
  
  It can optionally include a client certificate and key for
  mutual TLS.
  

- **--type** _string_

  _Notes: What is this again?  I think we need a qualifier on "type"._

- **--include-not-ready** _boolean_

  _Default:_ false

### skupper connector delete

Delete a connector.


#### Usage

~~~ shell
$ skupper connector delete <name>
Waiting for deletion to complete...
Connector "<name>" is deleted
~~~

#### Arguments

- **name** _string_

  The name of the connector resource.
  

### skupper connector status

Show the status of connectors in the current site.


#### Usage

~~~ shell
$ skupper connector status
NAME       ROUTING-KEY   SELECTOR         HOST   PORT   MATCHING-LISTENERS
backend    backend       app=backend      -      8080   1
database   database      app=postgresql   -      5342   1
~~~

### skupper listener

Display help for listener commands and exit.


### skupper listener create

Create a listener.

A [listener][listener] is a local connection endpoint bound to
servers in remote sites.

Each namespace can contain multiple listener definitions.

[listener]: concepts.html#listener



#### Usage

~~~ shell
$ skupper listener create <name> [options]
Waiting for status...
Listener "<name>" is ready
~~~

#### Examples

~~~
# Create a listener for a database
skupper listener create database --host database --port 5432
~~~

#### Arguments

- **name** _string_

  The name of the listener resource.
  

- **--routing-key** _string_

  _Default:_ _value of name_

  The identifier used to route traffic from listeners to
  connectors.  To connect to a service at a remote site, the
  listener and connector must have matching routing keys.
  

- **--host** _string_

  The hostname or IP address of the local listener.  Clients
  at this site use the listener host and port to
  establish connections to the remote service.
  

- **--port** _integer_

  The port of the local listener.  Clients at this site use
  the listener host and port to establish connections to
  the remote service.
  

- **--enable-t-l-s** _boolean_

  _Default:_ false

  Use TLS to encrypt communication between clients and the router.
  
  By default, the TLS credentials are generated and stored in
  a secret at XXX.
  

- **--tls-credentials** _string_

  The name of a Kubernetes secret containing TLS
  credentials.  The secret contains the server certificate
  and key.
  
  It can optionally include a client certificate for mutual
  TLS.
  

- **--type** _string_

  _Notes: What is this again?  I think we need a qualifier on "type"._

### skupper listener delete

Delete a listener.


#### Usage

~~~ shell
$ skupper listener delete <name>
Waiting for deletion to complete...
Listener "<name>" is deleted
~~~

#### Arguments

- **name** _string_

  The name of the listener resource.
  

### skupper listener status

Show the status of listeners in the current site.


#### Usage

~~~ shell
$ skupper listener status
NAME       ROUTING-KEY   HOST       PORT   MATCHING-CONNECTORS
backend    backend       backend    8080   1
database   database      database   5432   1
~~~

## Debug operations

### skupper debug

Display help for debug commands and exit.


### skupper debug dump

Generate a debug dump file.


#### Usage

~~~ shell
$ skupper debug dump [file]
Debug dump file generated at <file>
~~~

## Other operations

### skupper version


