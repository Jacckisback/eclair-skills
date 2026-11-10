# Validation plan — Opening the lightweight shop

## Data model
Product, price, category, legal notices, terms of sale.

## Expected implementation
Publish the legal notices and terms of sale, open the shop, create the first product pages, check the catalogue and structured data.

## Tests to plan
1. Nominal: Open the shop on a copy and go through the catalogue and a product page.
2. Refusal check: The shop does not open without published legal pages.
3. Invariant: No price, lead time or term of sale invented by the agent.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
