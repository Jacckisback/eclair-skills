# Validation plan — Diagnostics and logs

## Data model
Symptom, server log, site log, hypothesis, fix.

## Expected implementation
Reproduce, read the server and site logs, isolate the feature at fault by disabling it, fix then verify.

## Tests to plan
1. Nominal: Trigger an error in a test extension and locate it.
2. Refusal check: No technical trace appears in a public page.
3. Invariant: Error display is never enabled on the public site.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
