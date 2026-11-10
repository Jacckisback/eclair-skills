# Public member HTTP routes — Éclair 2.0.0 experimental

Public POST routes are **not** present in official Éclair 2.0. The proposed v1.1 patch makes a controlled exception: explicit POST method, `cache:false`, HTTPS, `Security::checkFormToken()`, `private,no-store` response, relative 303 redirect. Always run HTTP trials with the full CMS before merging.

The source patch is located in `core-patch/` of the full distribution, not included in a standalone copy of the skill. Never treat this patch as an official API before it has been merged upstream.
