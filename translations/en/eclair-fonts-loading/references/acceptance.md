# Validation plan — Fonts

## Data model
Font, weights, self-hosted file, system fallback.

## Expected implementation
Use system fonts or the self-hosted heading font from the art directions, limit the weights.

## Tests to plan
1. Nominal: Check that there is no third-party request and no text jump.
2. Refusal check: An unavailable font leaves a readable fallback.
3. Invariant: No font is loaded from a third-party service.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
