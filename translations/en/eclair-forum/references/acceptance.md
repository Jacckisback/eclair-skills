# Validation plan — Forum architecture

## Data model
Space, category, topic, message, author, role, report, locking.

## Expected implementation
Separate indexable and private topics; plan stable pagination, object permissions, quotas and moderation; prepare a bounded search engine.

## Tests to plan
1. Nominal: Test visitor, member, moderator and suspended account.
2. Refusal check: Private topic non-existent for an unauthorised member, including through search.
3. Invariant: No anonymous writing without anti-spam, CSRF and rate limiting; never arbitrary HTML executed.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
