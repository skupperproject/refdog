---
links:
  - name: Skupper resources
    url: /resources/index.html
  - name: Skupper commands
    url: /commands/index.html
---

# Skupper concepts

[Overview](overview.html)

#### Sites and networks

<table class="objects">
<tr><th><a href="{{site_prefix}}/concepts/site.html">Site</a></th><td><p>A <em>site</em> is a place on the network where workloads are running</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/network.html">Network</a></th><td><p>A <em>network</em> is a set of linked sites</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/platform.html">Platform</a></th><td><p>A <em>platform</em> is a system for running workloads</p>
</td></tr>
</table>

#### Site linking

<table class="objects">
<tr><th><a href="{{site_prefix}}/concepts/link.html">Link</a></th><td><p>A <em>link</em> is a channel for communication between sites</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/access-token.html">Access token</a></th><td><p>An <em>access token</em> is a short-lived credential used to create a link</p>
</td></tr>
</table>

#### Service exposure

<table class="objects">
<tr><th><a href="{{site_prefix}}/concepts/listener.html">Listener</a></th><td><p>A <em>listener</em> binds a local connection endpoint to connectors in remote sites</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/connector.html">Connector</a></th><td><p>A <em>connector</em> binds a local workload to listeners in remote sites</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/routing-key.html">Routing key</a></th><td><p>A <em>routing key</em> is an identifier for matching listeners and connectors</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/attached-connector.html">Attached connector</a></th><td><p>An <em>attached connector</em> is a connector in a peer namespace</p>
</td></tr>
</table>
