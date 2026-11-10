# Validation plan — Client and partner logos

## Data model
Logo, name, optional link.

## Expected implementation
Display the logos in a static grid, consistent sizes, names as alternative text.

## Tests to plan
1. Nominal: Check legibility in light and dark mode.
2. Refusal check: A logo without a recorded authorisation is not included.
3. Invariant: Only logos whose use is authorised are published.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
