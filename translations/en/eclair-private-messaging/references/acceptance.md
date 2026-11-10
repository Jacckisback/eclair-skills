# Validation plan — Private messaging

## Data model
Conversation, participants, message, report.

## Expected implementation
Define blocking, reporting, sending limits and retention; no conversation in a cached page.

## Tests to plan
1. Nominal: Simulate exchange, blocking and reporting.
2. Refusal check: A blocked member can no longer write to the member who blocked them.
3. Invariant: A message is readable only by its participants.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
