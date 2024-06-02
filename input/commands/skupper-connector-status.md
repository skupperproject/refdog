# skupper connector status

Show the status of connectors in the current site.


## Usage

~~~ shell
$ skupper connector status
NAME       ROUTING-KEY   SELECTOR         HOST   PORT   MATCHING-LISTENERS
backend    backend       app=backend      -      8080   1
database   database      app=postgresql   -      5342   1
~~~
