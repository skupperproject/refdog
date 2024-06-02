# skupper site status

Show the current status of a site.


## Usage

~~~ shell
$ skupper site status
NAME   STATUS   SITES-IN-NETWORK   SERVICES-IN-NETWORK
west   Ready    1                  0
~~~

_Notes: What is services-in-network?  Is that the total number of_ 
_Notes: unique routing keys defined by connectors?  Or listeners?_ 
_Notes: Or listeners plus connectors (not the orphans), grouped by_ 
_Notes: routing key?_ 
