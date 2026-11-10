# Public member HTTP routes — Éclair 2.0.0 experimental

The demonstrator's storage still uses the protected `Store` files and a global lock. It is capped at 1000 accounts; no promise of multi-file atomicity, of access at scale or of transactional fault tolerance. An SQL backend is a prerequisite before any business use.

The source patch is located in `core-patch/` of the full distribution, not included in a standalone copy of the skill. Never treat this patch as an official API before it has been merged upstream.
