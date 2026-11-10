# Validation plan — A/B tests

## Data model
Variant, split, objective, result.

## Expected implementation
Test over successive periods or with separate addresses rather than with variants in the cache; set hypothesis, duration and measurement in advance.

## Tests to plan
1. Nominal: Run a test on two separate landing pages.
2. Refusal check: A result without sufficient volume is not presented as conclusive.
3. Invariant: No variant is stored in the shared cache per visitor.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
