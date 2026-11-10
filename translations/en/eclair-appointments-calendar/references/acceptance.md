# Validation plan — Appointments and calendar

## Data model
Provider, service, duration, buffers, exceptions, events and time zones.

## Expected implementation
Normalise times to UTC, keep the display time zone, block unavailability slots, handle external resynchronisation.

## Tests to plan
1. Nominal: Test DST, appointment spanning midnight, deleted event.
2. Refusal check: A manually blocked slot is never offered after resynchronisation.
3. Invariant: An external integration requires OAuth/minimal scopes and must not expose private calendars.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
