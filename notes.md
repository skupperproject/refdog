## Notes

### Goals

- A unified declarative language ("Skupper site YAML") for creating sites,
  linking sites, and exposing services.
- A language that operates uniformly for Kubernetes, Podman, and
  generated bundles, while still allowing for some platform specific
  variations.
- A simple translation from Skupper site YAML to Kubernetes custom
  resources.
- As an alternative to CRDs, allow use of Skupper site YAML as the
  content of a Kubernetes ConfigMap.

### Clarifications

- A token is special in that it is not yet "fulfilled" - and therefore
  usable for linking - until it has an associated token file or
  secret.

### Questions

- What *are* address and host on ProvidedService?  Router tcpConnector
  stuff?

### Resources

- [Skupper syncer demo](https://github.com/grs/skupper-syncer-demo)
- [Kubernetes Service API](https://kubernetes.io/docs/reference/kubernetes-api/service-resources/service-v1/)
-
