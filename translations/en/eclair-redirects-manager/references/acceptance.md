# Validation plan — Redirects

## Data model
Old address, new address, type, date.

## Expected implementation
Import the old addresses, create one direct redirect per address, remove chains and loops.

## Tests to plan
1. Nominal: Test a batch of old addresses and record status and destination.
2. Refusal check: No chain of more than one hop and no loop.
3. Invariant: No open redirect to an unintended domain.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
