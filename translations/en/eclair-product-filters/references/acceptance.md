# Validation plan — Catalogue filters and sorting

## Data model
Criterion, value, combination, filtered address.

## Expected implementation
Rely on the native category filters; add browser-side filters on public data, with controlled canonical addresses.

## Tests to plan
1. Nominal: Filter and sort a test catalogue on mobile.
2. Refusal check: A combination with no results displays a message, not an indexable empty page.
3. Invariant: Filter combinations do not create an infinite number of indexable pages.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
