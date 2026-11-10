# Validation plan — Product feed

## Data model
Product, price, availability, image, identifiers.

## Expected implementation
Complete the product pages, check the feed produced by the core, declare it in the merchant tool, fix the rejections.

## Tests to plan
1. Nominal: Validate the feed and compare three products with their product pages.
2. Refusal check: An unavailable product is not advertised as in stock.
3. Invariant: Price and availability in the feed are those of the public product page.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
