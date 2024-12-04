---
refdog_object_links:
  - title: Skupper resources
    url: /resources/index.html
  - title: Skupper commands
    url: /commands/index.html
---

# Skupper concepts

[Overview](overview.html)

#### Primary concepts

<table class="objects">
<tr><th><a href="{{site_prefix}}/concepts/network.html">Network</a></th><td><p>A <strong>network</strong> is a set of <strong><a href="site.html">sites</a></strong> joined by <strong><a href="link.html">links</a></strong></p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/site.html">Site</a></th><td><p>A <strong>site</strong> is a place on the IP network where application workloads are running</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/link.html">Link</a></th><td><p>A <strong>link</strong> is a channel for communication between <strong><a href="site.html">sites</a></strong></p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/listener.html">Listener</a></th><td><p>A <strong>listener</strong> binds a local connection endpoint to <strong><a href="connector.html">connectors</a></strong> in remote <strong><a href="site.html">sites</a></strong></p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/connector.html">Connector</a></th><td><p>A <strong>connector</strong> binds a local workload to <strong><a href="listener.html">listeners</a></strong> in remote <strong><a href="site.html">sites</a></strong></p>
</td></tr>
</table>

#### Sites

<table class="objects">
<tr><th><a href="{{site_prefix}}/concepts/site.html">Site</a></th><td><p>A <strong>site</strong> is a place on the IP network where application workloads are running</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/platform.html">Platform</a></th><td><p>A <strong>platform</strong> is a system for running application workloads</p>
</td></tr>
</table>

#### Site linking

<table class="objects">
<tr><th><a href="{{site_prefix}}/concepts/link.html">Link</a></th><td><p>A <strong>link</strong> is a channel for communication between <strong><a href="site.html">sites</a></strong></p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/network.html">Network</a></th><td><p>A <strong>network</strong> is a set of <strong><a href="site.html">sites</a></strong> joined by <strong><a href="link.html">links</a></strong></p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/access-token.html">Access token</a></th><td><p>An <strong>access token</strong> is a short-lived credential used to create a <strong><a href="link.html">link</a></strong></p>
</td></tr>
</table>

#### Service exposure

<table class="objects">
<tr><th><a href="{{site_prefix}}/concepts/listener.html">Listener</a></th><td><p>A <strong>listener</strong> binds a local connection endpoint to <strong><a href="connector.html">connectors</a></strong> in remote <strong><a href="site.html">sites</a></strong></p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/connector.html">Connector</a></th><td><p>A <strong>connector</strong> binds a local workload to <strong><a href="listener.html">listeners</a></strong> in remote <strong><a href="site.html">sites</a></strong></p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/routing-key.html">Routing key</a></th><td><p>A <strong>routing key</strong> is an identifier for matching <strong><a href="listener.html">listeners</a></strong> and <strong><a href="connector.html">connectors</a></strong></p>
</td></tr>
</table>
