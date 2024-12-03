# Debug dumps

- The purpose of a debug dump is to package up details of a site so
  another party can identify and fix a problem.
- A dump is a tarball containing various files with the site details.
- Key elements include site resources and status; component versions,
  config files, and logs; and info about the environment where Skupper
  is running.

~~~
versions.yaml  # Same as the output of 'skupper version --output yaml'
platform.yaml  # Info about the platform and namespace hosting the site
network.yaml   # ??
components/
  controller/
    <config file>
    controller.log
  router/
    <config file>
    router.log
    kube-adaptor.log
  network-observer/
    <config file>
    network-observer.log
resources/
  <kind>-<name>.yaml for each Skupper resource
~~~
