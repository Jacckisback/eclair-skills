# Validation plan — Multilingual SEO

## Data model
Language, translation URL, reciprocal hreflang, title and sitemap.

## Expected implementation
Inventory published languages, define the translation mapping, test canonical per language, hreflang/x-default and the absence of intrusive redirects.

## Tests to plan
1. Nominal: Test FR/ES/EN pairs, missing pages and language switching.
2. Refusal check: Each hreflang link points to an indexable, reciprocal 200 URL.
3. Invariant: Do not use an unverified machine translation as a final page.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
