# Validation plan — Events and tickets

## Data model
Event, session, place type, booking, ticket, scan, refund.

## Expected implementation
Separate quotas per session; issue unique tickets after confirmed payment; handle atomic entry control and transfer.

## Tests to plan
1. Nominal: Test double scan, cancellation and simultaneous last ticket.
2. Refusal check: Same ticket presented at two doors => a single admission accepted.
3. Invariant: QR code does not contain personal data in clear text and does not allow several entries.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
