# Validation plan — Paid subscriptions

## Data model
Plan, period, subscriber, due date, status.

## Expected implementation
Let the provider manage direct debits and the customer area; design the synchronisation of permissions through signed events.

## Tests to plan
1. Nominal: Simulate subscription, renewal, failure and cancellation.
2. Refusal check: A failed payment extends no access.
3. Invariant: An access right is opened only on an authenticated payment event.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
