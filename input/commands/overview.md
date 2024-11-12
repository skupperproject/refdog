# Skupper command overview

## Resource configuration and status commands

- Create, update, delete, and status.

- Site, Link, Listener, and Connector.

- Generally, they submit the resource to the controller and wait for
  ready state (Listener and Connector wait for configured state).

- Create operations take a name option, which is the name of the
  resource created (.metadata.name).

- Update operations shift the resource status from ready to pending
  while the change is taking place.  It waits for ready status.

- The status command gets the status info from the resource status
  fields.

## Resource output generation commands

- These commands generate structured output, YAML or JSON.

- They generate output that represents Skupper resources.

- You might want to direct the output to a file, cut and paste it, or
  pipe it to kubectl.

- These are good for learning about the resources.

- Link generate is a little different from the other generate
  commands.  In general, the generate commands are helping you produce
  resources for your current site.  By contrast, link generates a link
  resource (and a secret to go with it) for use in a *remote* site,
  *to* the current site.

- The token commands are for creating links!

## Site configuration commands

## Site linking commands

## Service exposure commands

## Site operation commands

- These commands are for non-Kube sites.

- They are about installing and operating the Skupper runtime
  components.

## Debug commands

- These commands are for debugging and troubleshooting.

## Other stuff

- The version command!

## Hello World using the CLI

Site West:

~~~
skupper site create west --enable-link-access
skupper listener create backend 8080
skupper token issue ~/west-token.yaml
~~~

Site East:

~~~
skupper site create east
skupper connector create backend 8080
skupper token redeem ~/west-token.yaml
~~~
