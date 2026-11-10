# Validation plan — Lazy loading

## Data model
Image, priority, dimensions.

## Expected implementation
Check that the main image is loaded with priority and the others lazily, with explicit dimensions.

## Tests to plan
1. Nominal: Measure the largest element's display and the layout shift.
2. Refusal check: The main image is never lazy-loaded.
3. Invariant: No third-party script is added to defer loading.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
