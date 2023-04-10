## Notes

### Goals

*Regularize* and *document* Skupper configuration.

- A declarative language ("Skupper YAML") for creating sites, linking
  sites, and exposing services.
- A configuration model that operates uniformly across Kubernetes,
  Podman, and bundle generation, while still allowing for platform
  specific variations.
- A simple translation from Skupper YAML to Kubernetes custom
  resources.
- As an alternative to custom resources, the option to use Skupper
  YAML as the content of a Kubernetes ConfigMap that you feed to the
  site controller.
- A central configuration reference for Skupper.

In addition, I'd like to use this exercise to work out what the [CLI
experience][services-cli] should be for provided and required
services.

[services-cli]: services-cli.txt

A related project is mocking up the [GUI equivalent][skuppernetes] in
the context of a Kubernetes console.

[skuppernetes]: https://www.ssorj.net/skuppernetes/

<!-- ### Clarifications -->

<!-- - A token is special in that it is not yet "fulfilled" - and therefore -->
<!--   usable for linking - until it has an associated token file or -->
<!--   secret. -->

<!-- ### Questions -->

<!-- - What *are* address and host on ProvidedService?  Router tcpConnector -->
<!--   stuff? -->

### Resources

- [Hello World expressed in Skupper YAML](hello-world.yaml)
- [Hello World expressed as Kubernetes custom resources](hello-world-custom-resources.yaml)
- [Hello World as Skupper YAML embedded in ConfigMaps](hello-world-config-map.yaml)
- [Hello World scripted using the proposed CLI commands](hello-world-cli-script.txt)
- [Skupper syncer demo](https://github.com/grs/skupper-syncer-demo)
- [Kubernetes Service API](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/)
- [Skuppernetes, the GUI equivalent of the operations here](https://www.ssorj.net/skuppernetes/)
