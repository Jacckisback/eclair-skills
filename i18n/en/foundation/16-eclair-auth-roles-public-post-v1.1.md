# Public member HTTP routes — Éclair 2.0.0 experimental

The v1.1 prototype has public handlers: GET form + POST login/logout + GET private area. They are valid only after the approved addition of the POST contract. Member sessions distinct from admin sessions, opaque token, double-submit CSRF and session CSRF on logout; no admin/editor role granted.

The source patch is located in `core-patch/` of the full distribution, not included in a standalone copy of the skill. Never treat this patch as an official API before it has been merged upstream.
