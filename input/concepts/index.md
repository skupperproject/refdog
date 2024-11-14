---
links:
  - name: Skupper resources
    url: /resources/index.html
  - name: Skupper commands
    url: /commands/index.html
---

# Skupper concepts

[Overview](overview.html)

#### Networks and sites

<table class="objects">
<tr><th><a href="{{site_prefix}}/concepts/network.html">Network</a></th><td><p>A <em>network</em> is a set of linked sites that host a distributed application</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/site.html">Site</a></th><td><p>A place where components of your application are running</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/platform.html">Platform</a></th><td><p>A system for running workloads</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/namespace.html">Namespace</a></th><td><p>A named area for a related set of resources and components</p>
</td></tr>
</table>

#### Site linking

<table class="objects">
<tr><th><a href="{{site_prefix}}/concepts/link.html">Link</a></th><td><p>A site-to-site communication channel</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/link-access.html">Link access</a></th><td><p>An external access point for receiving links</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/access-grant.html">Access grant</a></th><td><p>Permission to redeem access tokens for links to the local site</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/access-token.html">Access token</a></th><td><p>A transferrable token redeemable for a link to a remote site</p>
</td></tr>
</table>

#### Service exposure

<table class="objects">
<tr><th><a href="{{site_prefix}}/concepts/service.html">Service</a></th><td><p>An application component exposed on the network</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/listener.html">Listener</a></th><td><p>A binding from a local connection endpoint to connectors in remote sites</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/connector.html">Connector</a></th><td><p>A binding from a local workload to listeners in remote sites</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/routing-key.html">Routing key</a></th><td><p>An identifier for matching listeners to connectors</p>
</td></tr>
</table>
