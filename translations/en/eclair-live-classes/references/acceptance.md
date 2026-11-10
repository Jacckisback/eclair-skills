# Validation plan — Live classes

## Data model
Session, date, time zone, joining link, enrolled participants.

## Expected implementation
Publish the session calendar via GET, send the joining link through the video conferencing service or by email, not on a public page.

## Tests to plan
1. Nominal: Check the display of dates in two time zones.
2. Refusal check: A past session is no longer offered for enrolment.
3. Invariant: The link to a paid or private session is never published.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
