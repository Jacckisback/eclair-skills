# Validation plan — Content delivery network (CDN)

## Data model
DNS zone, cache rules, purge.

## Expected implementation
Set up DNS and HTTPS end to end, exclude the administration from the CDN cache, define purging on publication.

## Tests to plan
1. Nominal: Check the cache headers of the public pages and of the administration.
2. Refusal check: After a modification, the old version is no longer served once the purge has run.
3. Invariant: The administration and any private response are never cached by the CDN.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
