# Validation plan — Technical SEO audit

## Data model
URLs, canonicals, sitemap, redirects, titles, HTTP statuses, structured data.

## Expected implementation
Crawl the authorised pages, record discrepancies, prioritise structural causes, check coverage and the correction plan.

## Tests to plan
1. Nominal: Test trailing slash, accents, paginations, 404, sitemap and robots.
2. Refusal check: No critical URL is orphaned or redirected in a chain after an update.
3. Invariant: Do not promise rankings; do not modify existing URLs without a redirect plan.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
