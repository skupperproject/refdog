<!-- * [Skupper components](#skupper-components) -->
<!--   * [CLI (command line interface)](#cli-command-line-interface) -->
<!--   * [Collector](#collector) -->
<!--   * [Console](#console) -->
<!--   * [Controller](#controller) -->
<!--   * [Router](#router) -->

<!-- ## Skupper components -->

<!-- The software components that implement Skupper's features. -->

<!-- ~~~ -->
<!--              +-------------------------+   +------------------------+ -->
<!--              |       Site "west"       |   |       Site "east"      | -->
<!--              |                         |   |                        | -->
<!--              | +---------------------+ |   | +--------------------+ | -->
<!--              | | Workload "frontend" | |   | | Workload "backend" | | -->
<!--              | +---------------------+ |   | +--------------------+ | -->
<!--              |       +--------+        |   |       +--------+       | -->
<!--              |       | Router |--------------------| Router |       | -->
<!--              |       +--------+        |   |       +--------+       | -->
<!--   +-----+    |     +------------+      |   |     +------------+     |    +-----+ -->
<!--   | CLI |----------| Controller |      |   |     | Controller |----------| CLI | -->
<!--   +-----+    |     +------------+      |   |     +------------+     |    +-----+ -->
<!--              |     +-----------+       |   |                        | -->
<!--              |     | Collector |       |   |                        | -->
<!--              |     +-----------+       |   |                        | -->
<!-- +---------+  |      +---------+        |   |                        | -->
<!-- | Browser |---------| Console |        |   |                        | -->
<!-- +---------+  |      +---------+        |   |                        | -->
<!--              +-------------------------+   +------------------------+ -->
<!-- ~~~ -->

<!-- ### CLI (command line interface) -->

<!-- ### Collector -->

<!-- The collector stores data about network configuration and application -->
<!-- traffic. -->

<!-- ### Console -->

<!-- The console displays the application traffic on your network. -->
<!-- The console is scoped to one Skupper network. -->
<!-- The console is read only. -->
<!-- The console depends on the flow collector. -->

<!-- ### Controller -->

<!-- The site controller and service controller. -->
<!-- This is the Skupper control plane. -->

<!-- ### Router -->

<!-- Routers transfer application traffic. -->
<!-- Routers listen for client connections. -->
<!-- Routers connect to servers. -->

<!-- Each site has at least one router. -->
<!-- Routers link to eachother to form a router network. -->

<!-- The routers in a network are responsible for transporting application traffic. -->
<!-- The routers in a network constitute the Skupper data plane. -->

<!-- Routers implement application-layer addressing based on names. -->
<!-- Routers know where the target processes are for each named address. -->

<!-- Routers have two modes, interior and edge. -->
