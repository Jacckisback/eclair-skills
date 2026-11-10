# Validation plan — Pagination and lists

## Data model
List, current page, page size, previous and next links.

## Expected implementation
Set a reasonable page size, stable addresses per page and accessible links.

## Tests to plan
1. Nominal: Go through the first page, a middle page and the last page.
2. Refusal check: An out-of-range page number responds with a clean error, not with an indexable empty list.
3. Invariant: The page parameters are bounded and validated.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
