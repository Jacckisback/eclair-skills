# Public member HTTP routes — Éclair 2.0.0 experimental

A public POST route prototype is included in `examples/extensions/member-directory/`. It is rejected by the official 2.0 core. Use the manifest only with the experimental patch and the explicit agreement of a maintainer, never in production. POST requires `cache:false`, TLS, CSRF, relative redirect.

The source patch is located in `core-patch/` of the full distribution, not included in a standalone copy of the skill. Never treat this patch as an official API before it has been merged upstream.
