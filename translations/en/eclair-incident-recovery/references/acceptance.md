# Validation plan — Incident response

## Data model
Incident, timeline, affected accounts, clean backup.

## Expected implementation
Isolate, preserve the evidence, change the secrets, check integrity, restore a clean backup, inform the people concerned if necessary.

## Tests to plan
1. Nominal: Run the exercise on a copy: detection, restoration, check.
2. Refusal check: A restored site is not put back online before all the secrets have been changed.
3. Invariant: Never delete the traces before having copied them.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
