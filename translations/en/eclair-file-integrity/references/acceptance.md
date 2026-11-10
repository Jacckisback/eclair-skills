# Validation plan — File integrity

## Data model
File, expected hash, deviation.

## Expected implementation
Run the integrity check from the Security page, explain each deviation, restore the original files if needed.

## Tests to plan
1. Nominal: Modify a file on a test copy and observe the alert.
2. Refusal check: An altered core file is never declared compliant.
3. Invariant: An unexplained deviation is treated as an incident, not ignored.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
