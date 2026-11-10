# Validation plan — Image optimisation

## Data model
Source image, responsive variants, dimensions, weight.

## Expected implementation
Provide sources of the right size, let the core produce the variants, check the actual weight served on mobile.

## Tests to plan
1. Nominal: Measure the weight and dimensions served on mobile and desktop.
2. Refusal check: No image is served without explicit dimensions.
3. Invariant: Sensitive metadata (geolocation) is not published.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
