# Validation plan — Simulators and calculators

## Data model
Parameters, formula, result.

## Expected implementation
Calculate in the browser with a formula validated by the client, display assumptions and limits, then offer a contact option.

## Tests to plan
1. Nominal: Compare the results with a set of cases calculated by hand.
2. Refusal check: An absurd or negative value displays a message, not a wrong result.
3. Invariant: The result is indicative and stated as such; no input is sent to the server.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
