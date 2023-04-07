## Notes

### Goals

- A unified declarative language ("Skupper YAML") for creating sites,
  linking sites, and exposing services.
- A configuration model that operates uniformly across Kubernetes,
  Podman, and bundle generation, while still allowing for platform
  specific variations.
- A simple translation from Skupper YAML to Kubernetes custom
  resources.
- As an alternative to custom resources, the option to use Skupper
  YAML as the content of a Kubernetes ConfigMap that you feed to the
  site controller.
- A central configuration reference for Skupper.

In addition, I'd like to use this exercise to work out what the CLI
experience should be for provided and required services.

### Clarifications

- A token is special in that it is not yet "fulfilled" - and therefore
  usable for linking - until it has an associated token file or
  secret.

### Questions

- What *are* address and host on ProvidedService?  Router tcpConnector
  stuff?

### Resources

- [Skupper's Hello World expressed in Skupper YAML](hello-world.yaml)
- [Skupper syncer demo](https://github.com/grs/skupper-syncer-demo)
- [Kubernetes Service API](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/)
