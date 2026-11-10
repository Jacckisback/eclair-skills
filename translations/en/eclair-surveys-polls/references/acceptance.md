# Validation plan — Polls and surveys

## Data model
Question, choices, response, anonymous participant, aggregated results.

## Expected implementation
Define anonymity, limitation of multiple votes, display of aggregated results and duration of the poll.

## Tests to plan
1. Nominal: Vote, view the results and close the poll.
2. Refusal check: A second vote from the same participant is ignored.
3. Invariant: No individual response is published; aggregated results only.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
