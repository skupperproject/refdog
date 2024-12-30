---
body_class: object command
refdog_links:
- title: Site linking
  url: /topics/site-linking.html
- title: Access token concept
  url: /concepts/access-token.html
- title: AccessGrant resource
  url: /resources/access-grant.html
- title: AccessToken resource
  url: /resources/access-token.html
refdog_object_has_attributes: true
refdog_toc:
- id: ''
  title: Overview
- id: subcommands
  title: Subcommands
- id: primary-options
  title: Primary options
- id: global-options
  title: Global options
---

# Token command

<section>

~~~ shell
skupper token [subcommand] [options]
~~~

<table class="fields"><tr><th>Platforms</th><td>Kubernetes, Docker, Podman, Linux</td></table>

</section>

<section>

## Subcommands

<table class="objects">
<tr><th><a href="issue.html">Token issue</a></th><td>Issue a token file redeemable for a link to the current site</td></tr>
<tr><th><a href="redeem.html">Token redeem</a></th><td>Redeem a token file in order to create a link to a remote site</td></tr>
</table>

</section>
