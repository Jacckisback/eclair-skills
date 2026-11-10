# Validation plan — Subscriptions and memberships

## Data model
Plan, membership, renewal, period, cancellation, payment, permission.

## Expected implementation
Calculate permissions from the verified state, plan for plan changes and grace periods, handle billing events idempotently.

## Tests to plan
1. Nominal: Test failed direct debit, pro rata, refund and cancellation.
2. Refusal check: Two identical events do not extend the subscription twice.
3. Invariant: A browser receipt is never enough to renew paid access.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
