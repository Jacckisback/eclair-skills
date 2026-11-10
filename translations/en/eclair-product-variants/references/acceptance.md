# Validation plan — Variants and attributes

## Data model
Parent product, variants with a unique SKU, attribute combinations, own prices/stock, media and status.

## Expected implementation
Define the maximum number of combinations; ensure SKU uniqueness; project variants into the GET rendering; prepare server-validated selection at checkout.

## Tests to plan
1. Nominal: Test missing, out-of-stock and deactivated variants.
2. Refusal check: Two combinations create the same SKU => explicit rejection before publication.
3. Invariant: Never accept prices, weights or stock sent by the browser as reliable data.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
