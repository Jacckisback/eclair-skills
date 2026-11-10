# Validation plan — Login protection

## Data model
Attempts, limits per network and per account, administration address.

## Expected implementation
Check the native attempt limits, the administration address, the active sessions and the temporary passwords.

## Tests to plan
1. Nominal: Simulate repeated failures and observe the lockout.
2. Refusal check: The owner's usual device is not locked out by a third party's attempts.
3. Invariant: No native limit is relaxed.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
