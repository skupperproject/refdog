---
refdog_object_links:
- title: Skupper concepts
  url: /concepts/index.html
- title: Skupper commands
  url: /commands/index.html
---

# Skupper resources

[Overview](overview.html)

#### Primary resources

<table class="objects">
<tr><th><a href="{{site_prefix}}/resources/site.html">Site</a></th><td><p>A place on the network where application workloads are running</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/resources/link.html">Link</a></th><td><p>A channel for communication between sites</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/resources/listener.html">Listener</a></th><td><p>A binding from a local connection endpoint to connectors in remote sites</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/resources/connector.html">Connector</a></th><td><p>A binding from a local workload to listeners in remotes sites</p>
</td></tr>
</table>

#### Site linking

<table class="objects">
<tr><th><a href="{{site_prefix}}/resources/link.html">Link</a></th><td><p>A channel for communication between sites</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/resources/access-grant.html">AccessGrant</a></th><td><p>Permission to redeem access tokens for links to the local site</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/resources/access-token.html">AccessToken</a></th><td><p>A short-lived credential used to create a link</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/resources/router-access.html">RouterAccess</a></th><td><p>Configuration for secure access to the site router</p>
</td></tr>
</table>

#### Service exposure

<table class="objects">
<tr><th><a href="{{site_prefix}}/resources/listener.html">Listener</a></th><td><p>A binding from a local connection endpoint to connectors in remote sites</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/resources/connector.html">Connector</a></th><td><p>A binding from a local workload to listeners in remotes sites</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/resources/attached-connector.html">AttachedConnector</a></th><td><p>A connector in a peer namespace</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/resources/attached-connector-anchor.html">AttachedConnectorBinding</a></th><td><p>A binding to an attached connector in a peer namespace</p>
</td></tr>
</table>
