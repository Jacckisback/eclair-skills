# Public member HTTP routes — Éclair 2.0.0 experimental

The v1.1 prototype has `RateLimit::attempt` limiting before hashing, a strict members/admin separation and 256-bit session tokens. Assess the security of `Origin` handling, of TLS behind a reverse proxy, CSRF, IDOR, account enumeration, information leaks and concurrency. Do not confuse isolated tests with a production audit.

The source patch is located in `core-patch/` of the full distribution, not included in a standalone copy of the skill. Never treat this patch as an official API before it has been merged upstream.
