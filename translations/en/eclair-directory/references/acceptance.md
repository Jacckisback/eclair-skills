# Validation plan — Business directory

## Data model
Listing, category, location, public contact, verification status.

## Expected implementation
Separate public and private business data; create category pages, canonical, moderation and bounded filters.

## Tests to plan
1. Nominal: Test fake listings, duplicates, deletion and empty search.
2. Refusal check: A pending listing appears neither in the sitemap nor in the structured data.
3. Invariant: Do not publish a personal address, telephone number or sensitive contact details without authorisation.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
