# Validation plan — Activity log

## Data model
Event, account, date, action.

## Expected implementation
Consult the log on the Security page, spot sensitive logins and changes, set a checking routine.

## Tests to plan
1. Nominal: Trigger a sensitive action and find it in the log.
2. Refusal check: An account without the Security permission does not access the log.
3. Invariant: The log is readable only by accounts with the Security permission.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
