# Skupper command overview

`skupper` is the command-line interface (CLI) for creating and
operating Skupper networks.

The Skupper CLI is a light layer on top of the standard Skupper
resources.  Its primary job is to generate resources, submit them to
the platform, and wait for the desired result.

#### Key capabilities

- **Resource configuration** - Create, update, and delete Skupper
  sites, links, listeners, and connectors.
- **Resource status** - Inspect the current state of Skupper
  resources.
- **Site linking** - Use tokens to set up site-to-site links.
- **System operation** - Install and operate Skupper runtime
  components.
- **Troubleshooting** - Use debugging tools to identify and fix
  problems.

#### Usage

~~~
skupper [command] [subcommand] [options]
~~~

XXX

#### Context

Most commands operate in the context of a selected platform and
current namespace.  You can use the `--platform` and `--namespace`
options and the `SKUPPER_PLATFORM` and `SKUPPER_NAMESPACE` environment
variables to set them.

XXX And kubeconfig and context!

#### Blocking

In general, the operations block until the user's desired outcome is
achieved.  You can change the wait condition using the `--wait`
option.

XXX Timeouts!

#### Errors

XXX

## Resource commands

These are the core CLI operations.

- **Site command**
- **Link command**
- **Listener command**
- **Connector command**

- On Kubernetes: Generally, they submit the resource to the controller
  and wait for ready state (Listener and Connector wait for configured
  state).

- On other platforms: They don't wait for anything.  Instead they put
  the resources in the input location.  The user must then trigger a
  config reload.

Resource options for setting resource properties are set using one or
more `--some-key some-value` command line options.  YAML resource
options in camel case (`someKey`) are exposed as hyphenated names
(`some-key`) when used as command line options.

XXX The resource `create` and `update` operations in particular are meant
to provide a convenient and CLI-conventional interface, as an
alternative to writing YAML by hand. XXX

#### `skupper <resource-type> [options]`

Without specifying a subcommand, these print help text for the
operations of this resource type.

#### `skupper <resource-type> create <resource-name> [options]`

Create a resource.

- Create operations take a name option, which is the name of the
  resource created (.metadata.name).

- XXX Create and update in general block until the resource is ready.
  Delete waits for deletion to complete.

#### `skupper <resource-type> update <resource-name> [options]`

- Update operations shift the resource status from ready to pending
  while the change is taking place.  It waits for ready status.

- It has the same options as create.

- XXX Create and update in general block until the resource is ready.
  Delete waits for deletion to complete.

#### `skupper <resource-type> delete <resource-name> [options]`

- Waits until deletion is complete.

#### `skupper <resource-type> status [resource-name] [options]`

- The status command gets the status info from the resource status
  fields.

- If no name is given, it gets an aggregate output across all
  resources of this type (in a table!).

- `status` without a qualifying resource name argument enumerates the
  status of all the resources of this type.

- `status` with a resource name and `--output yaml` gives you...

#### `skupper <resource-type> generate <resource-name> [options]`

- These commands generate Skupper resources in YAML or JSON format.

- They generate output that represents Skupper resources.

- You might want to direct the output to a file, cut and paste it, or
  pipe it to kubectl.

- These are good for learning about the resources.

- Link generate is a little different from the other generate
  commands.  In general, the generate commands are helping you produce
  resources for your current site.  By contrast, link generates a link
  resource (and a secret to go with it) for use in a *remote* site,
  *to* the current site.

- The generate commands usually don't need to wait for a status.  Link
  generate is the exception - it needs the site to be ready.

## Token commands

- The token commands are for creating links!

## System commands

- These commands are for non-Kube sites.

- They are about installing and operating the Skupper runtime
  components.

## Debug commands

- These commands are for debugging and troubleshooting.

## Version command

- The version command!

## Hello World using the CLI

~~~ console
# Get the CLI

$ curl https://skupper.io/install.sh | sh

# West

$ export KUBECONFIG=~/.kube/config-west
$ kubectl apply -f https://skupper.io/install.yaml
$ kubectl create deployment frontend --image quay.io/skupper/hello-world-frontend

$ skupper site create --enable-link-access
$ skupper listener create backend 8080
$ skupper token issue ~/token.yaml

# East

$ export KUBECONFIG=~/.kube/config-east
$ kubectl apply -f https://skupper.io/install.yaml
$ kubectl create deployment backend --image quay.io/skupper/hello-world-backend --replicas 3

$ skupper site create
$ skupper connector create backend 8080
$ skupper token redeem ~/token.yaml
~~~
