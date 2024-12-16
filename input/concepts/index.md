---
refdog_object_links:
  - title: Skupper resources
    url: /resources/index.html
  - title: Skupper commands
    url: /commands/index.html
---

# Skupper concepts

[Overview](overview.html)

#### Sites

<table class="objects">
<tr><th><a href="{{site_prefix}}/concepts/site.html">Site</a></th><td><p>A site is a place on the <a href="network.html">network</a> where application <a href="workload.html">workloads</a> are running</p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/workload.html">Workload</a></th><td><p>A workload is a set of processes running on a <a href="platform.html">platform</a></p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/platform.html">Platform</a></th><td><p>A platform is a system for running application <a href="workload.html">workloads</a></p>
</td></tr>
</table>

#### Site linking

<table class="objects">
<tr><th><a href="{{site_prefix}}/concepts/link.html">Link</a></th><td><p>A link is a channel for communication between <a href="site.html">sites</a></p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/network.html">Network</a></th><td><p>A network is a set of <a href="site.html">sites</a> joined by <a href="link.html">links</a></p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/access-token.html">Access token</a></th><td><p>An access token is a short-lived credential used to create a <a href="link.html">link</a></p>
</td></tr>
</table>

#### Service exposure

<table class="objects">
<tr><th><a href="{{site_prefix}}/concepts/listener.html">Listener</a></th><td><p>A listener binds a local connection endpoint to <a href="connector.html">connectors</a> in remote <a href="site.html">sites</a></p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/connector.html">Connector</a></th><td><p>A connector binds a local <a href="workload.html">workload</a> to <a href="listener.html">listeners</a> in remote <a href="site.html">sites</a></p>
</td></tr>
<tr><th><a href="{{site_prefix}}/concepts/routing-key.html">Routing key</a></th><td><p>A routing key is a string identifier for matching <a href="listener.html">listeners</a> and <a href="connector.html">connectors</a></p>
</td></tr>
</table>
