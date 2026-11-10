# Validation plan — Spam protection

## Data model
Message, form token, rate limit.

## Expected implementation
Rely on the token and the limits of the native form, add a honeypot field if needed, monitor the inbox.

## Tests to plan
1. Nominal: Send a legitimate message, then an automated burst.
2. Refusal check: A submission without a valid token is rejected.
3. Invariant: No third-party service receives visitors' messages without prior notice.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
