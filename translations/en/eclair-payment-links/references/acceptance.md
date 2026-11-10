# Validation plan — Payment links

## Data model
Product or variant, payment link, provider.

## Expected implementation
Create the link with the provider, paste it into the product page or the variant, test in test mode, check receipt and refund on the provider side.

## Tests to plan
1. Nominal: Buy in test mode and check amount and receipt.
2. Refusal check: A link to an unrecognised domain is rejected.
3. Invariant: No banking data on the site; a link leads only to the provider's domain.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
