# Validation plan — Structured data

## Data model
WebPage, Article, Product, relevant FAQ, Organization, BreadcrumbList.

## Expected implementation
Inspect the native JSON-LD before adding a type; avoid duplication; align each field with the visible data and the search engines' guidelines.

## Tests to plan
1. Nominal: Test valid JSON, canonical, identifiers and displayed content.
2. Refusal check: No price/review/product that is invented or absent from the page appears in JSON-LD.
3. Invariant: Éclair v2 does not yet expose all JSON-LD contributions to extensions; propose an RFC rather than opaque injection.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
