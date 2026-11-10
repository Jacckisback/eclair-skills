# Validation plan — Business bookings

## Data model
Resource, time range, capacity, time zone, state and booking.

## Expected implementation
Define availability and cancellation rules, lock slots transactionally, distinguish provisional hold and firm booking.

## Tests to plan
1. Nominal: Test simultaneous customers, clock changes and cancellation.
2. Refusal check: Last place booked simultaneously => a single confirmation.
3. Invariant: No cached GET calendar replaces the transactional validation of availability.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
