# Validation plan — Orders and payments

## Data model
Order, payment attempt, provider identifier, webhook proof, idempotency key, refund.

## Expected implementation
Detail the allowed transitions; store the proof of the notification and its timestamp; process webhooks durably; plan for reconciliation and partial refund.

## Tests to plan
1. Nominal: Test reversed, out-of-order and re-sent webhooks and declined payment.
2. Refusal check: A webhook without a valid signature modifies neither the order nor LMS access.
3. Invariant: Never store raw bank card data; checkout hosted by the provider and webhook signatures verified.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
