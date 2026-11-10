# Validation plan — Conditional forms

## Data model
Field, condition, branch, validation.

## Expected implementation
Describe the rules as data, apply them on the server side and on the browser side, test each branch.

## Tests to plan
1. Nominal: Go through each branch up to submission.
2. Refusal check: A required field of an active branch cannot be bypassed.
3. Invariant: Server validation never trusts fields hidden on the browser side.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
