# Validation plan — Teaching dashboard

## Data model
Enrolments, progress, aggregated results, course events.

## Expected implementation
Define metrics useful to instructors, filter by course and authorisation; minimise collection; plan retention and export.

## Tests to plan
1. Nominal: Test instructor visibility on course A vs B.
2. Refusal check: An aggregated statistics query must not expose the identity of a third-party student.
3. Invariant: A student's statistics are visible only to authorised parties.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
