# Validation plan — Customer accounts

## Data model
Customer, credentials, orders, addresses.

## Expected implementation
Define registration, login, account recovery and account deletion; strictly separate customer accounts from administration accounts.

## Tests to plan
1. Nominal: Simulate registration, login, viewing and deletion of the account.
2. Refusal check: A customer cannot read another customer's order by changing an identifier.
3. Invariant: A customer sees only their own data; never a shared cache on the customer area.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
