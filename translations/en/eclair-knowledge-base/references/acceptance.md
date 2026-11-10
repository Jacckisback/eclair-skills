# Validation plan — Knowledge base

## Data model
Help article, section, version, update date.

## Expected implementation
Organise by users' problems, one answer per page, navigation by sections and internal search.

## Tests to plan
1. Nominal: Solve three typical problems using the documentation alone.
2. Refusal check: An obsolete article is dated and flagged, not left as valid.
3. Invariant: No untested procedure is published.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
