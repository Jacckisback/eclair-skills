# Validation plan — Stock and reservations

## Data model
SKU, warehouse, physical stock, reserved, available, immutable movements.

## Expected implementation
Design the inbound/outbound movements; lock the reservation; handle expiry and compensation; trace all manual corrections.

## Tests to plan
1. Nominal: Test simultaneous purchases of the last item and release after expiry.
2. Refusal check: Two buyers cannot reserve the same last unit of stock.
3. Invariant: The cacheable availability read is informational; every sale re-reads the stock within a transaction.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
