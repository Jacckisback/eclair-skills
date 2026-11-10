# Validation plan — Calendar feeds

## Data model
Event, date, time zone, venue, iCalendar feed.

## Expected implementation
Generate a public iCalendar feed via GET from the published events, with explicit time zones.

## Tests to plan
1. Nominal: Subscribe to the feed from two calendar applications.
2. Refusal check: A cancelled event is marked as cancelled in the feed.
3. Invariant: The feed contains only public events, without participants.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
