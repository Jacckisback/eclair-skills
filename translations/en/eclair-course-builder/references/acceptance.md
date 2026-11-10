# Validation plan — Course building

## Data model
Course, module, lesson, order, draft, published version and author.

## Expected implementation
Establish a hierarchical schema; preview before publication; preserve identifiers when reordering; document archiving.

## Tests to plan
1. Nominal: Test lesson swapping, unpublishing and concurrent editing.
2. Refusal check: Changing the order does not reset students' progress.
3. Invariant: Instructor drafts must not be indexed or publicly exposed.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
