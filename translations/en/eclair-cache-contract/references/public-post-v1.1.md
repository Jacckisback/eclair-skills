# Public member HTTP routes — Éclair 2.0.0 experimental

Public GET forms use `Security::formField()` and must be declared `cache:false`. Their responses must not reach the core's fast path. POST is excluded from the fast path and forced to no-store. Test the purge on activation of the module and verify the absence of cookies/identities in the shared-cache HTML.

The source patch is located in `core-patch/` of the full distribution, not included in a standalone copy of the skill. Never treat this patch as an official API before it has been merged upstream.
