# Validation plan — Wishlists

## Data model
List, product, owner.

## Expected implementation
Start with storage in the browser, without an account; design the account-based version for later.

## Tests to plan
1. Nominal: Add, remove and retrieve favourites.
2. Refusal check: A deleted product disappears cleanly from the lists.
3. Invariant: No list is shared with or visible to a third party without action by its owner.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
