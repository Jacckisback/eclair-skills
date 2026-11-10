# Validation plan — Product catalogue

## Data model
Product, SKU, slug, title, description, display price, media, availability and category.

## Expected implementation
First prototype a cacheable public GET page; produce a product schema and its index; keep source titles and descriptions; define pagination and canonical; preserve slugs across edits.

## Tests to plan
1. Nominal: Test categories, empty lists, canonical URL, search and soft deletion.
2. Refusal check: A deleted or private product must not remain in the catalogue or in an old cache.
3. Invariant: The displayed price is never taken as the authoritative source for a future order.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
