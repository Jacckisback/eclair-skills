# Validation plan — Data requests

## Data model
Request, person, data concerned, time limit, response.

## Expected implementation
Map where the data is (messages, accounts, logs, backups), write the access and erasure procedure, keep a register.

## Tests to plan
1. Nominal: Walk through an access request and then an erasure request on a test data set.
2. Refusal check: A request without identity verification results in no disclosure.
3. Invariant: The requester's identity is verified before any data is disclosed.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
