# Validation plan — Maintenance mode

## Data model
Maintenance state, message, expected duration, team access.

## Expected implementation
Serve a static page with the correct temporary HTTP status at server level, keep access to the administration, plan the return online.

## Tests to plan
1. Nominal: Enable, check the 503 status and the retry header, disable.
2. Refusal check: Robots never receive the maintenance page with a 200 status.
3. Invariant: The maintenance page reveals neither version nor server path.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
