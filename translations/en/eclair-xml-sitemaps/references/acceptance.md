# Validation plan — XML sitemap

## Data model
Sitemap entries, dates, images, languages.

## Expected implementation
Check the sitemap produced by the core, declare it in the search engines' tools, monitor coverage errors.

## Tests to plan
1. Nominal: Validate the sitemap and compare it with the number of published pages.
2. Refusal check: A draft or redirected page does not appear in it.
3. Invariant: The sitemap lists only published and indexable pages.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
