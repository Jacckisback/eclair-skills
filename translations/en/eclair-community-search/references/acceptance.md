# Validation plan — Forum search

## Data model
Term, bounded index, language, category, page, status and permissions.

## Expected implementation
Normalise text, index authorised posts, paginate and limit cost, remove deleted objects from the results.

## Tests to plan
1. Nominal: Test empty phrase, injection, mass search, private topics.
2. Refusal check: A visitor must not see the excerpt of a private discussion in a suggestion.
3. Invariant: Permission filtering takes place on every search, not only at indexing time.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
