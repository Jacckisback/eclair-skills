# Validation plan — Page cache

## Data model
Cached page, invalidation, forbidden variants.

## Expected implementation
Measure the cached response, identify what prevents an extension route from being cached, check invalidation on modification.

## Tests to plan
1. Nominal: Measure the response time before and after a modification.
2. Refusal check: An extension route declared non-cacheable is never served from the cache.
3. Invariant: No page containing session or personal data enters the shared cache.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
