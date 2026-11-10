# Validation plan — Two-factor authentication

## Data model
Account, TOTP secret, backup codes.

## Expected implementation
Have each person enable two-factor authentication, store the backup codes safely, plan for the loss of a device.

## Tests to plan
1. Nominal: Enable, log out, log back in with the second factor.
2. Refusal check: A correct password without the second factor does not give access.
3. Invariant: Secrets and backup codes are never copied into a chat, an email or a repository.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
