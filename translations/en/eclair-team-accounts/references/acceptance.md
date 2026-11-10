# Validation plan — Team accounts

## Data model
Account, permissions, two-factor authentication, last login.

## Expected implementation
List who does what, assign the minimal native permissions, enforce two-factor authentication, remove unnecessary accounts.

## Tests to plan
1. Nominal: Create an editor account and check what it can and cannot do.
2. Refusal check: An account without the Settings permission can neither enable a feature nor change the theme.
3. Invariant: No shared account; no Security permission given for convenience.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
