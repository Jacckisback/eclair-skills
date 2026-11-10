# Validation plan — Groups

## Data model
Group, visibility, members, roles.

## Expected implementation
Define creation, joining, roles and visibility; apply permissions on every read.

## Tests to plan
1. Nominal: Simulate creation, request to join and exclusion.
2. Refusal check: A non-member reads no content of a private group.
3. Invariant: The content of a private group appears neither in search nor in the public cache.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
