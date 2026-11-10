# Validation plan — Payment forms

## Data model
Service, amount, the provider's payment link.

## Expected implementation
Create the link with the payment provider, display it on a clear page with terms, store nothing on the site.

## Tests to plan
1. Nominal: Pay in test mode and check the receipt and return page.
2. Refusal check: An amount modified on the browser side has no effect on the amount collected.
3. Invariant: No banking data passes through or is stored on the site.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
