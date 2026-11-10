# Validation plan — Cart and checkout flow

## Data model
Temporary cart, member or guest session, lines, promotions, fees, taxes, order state.

## Expected implementation
Separate display from state change; revalidate each line on the server; calculate amounts in whole monetary units; reserve stock transactionally at the right moment.

## Tests to plan
1. Nominal: Test simultaneous cart modification, expiry and price change.
2. Refusal check: Double or concurrent submission does not create two payable orders for the same key.
3. Invariant: No public write operation before a qualified POST route, CSRF, quotas and verified permissions.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
