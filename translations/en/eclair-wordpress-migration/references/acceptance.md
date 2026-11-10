# Validation plan — WordPress migration

## Data model
WordPress export, old IDs, slugs, media, categories, authors, redirects and ?p= queries.

## Expected implementation
Use the native WordPress feature; inventory historical URLs, simulate the import, compare slug/canonical, keep exact links and media, provide a rollback plan.

## Tests to plan
1. Nominal: Test URLs with trailing slash, query alias, accents, images and deleted pages.
2. Refusal check: For each old indexed URL, obtain an exact 200 or a targeted 301 redirect.
3. Invariant: Avoid 404s and URL deletions; never a DNS switchover without tests and backups.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
