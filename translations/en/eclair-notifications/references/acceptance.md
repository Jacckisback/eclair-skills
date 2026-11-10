# Validation plan — Community notifications

## Data model
Subscription, mention, notification, channel, preference, status.

## Expected implementation
Emit events after a validated write, filter by permissions at the time of reading and of sending, apply unsubscription.

## Tests to plan
1. Nominal: Test repeated notifications, unsubscription and permission withdrawal.
2. Refusal check: After access is revoked, no new notification contains a private excerpt.
3. Invariant: Never reveal content from private categories in an email, push or digest.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
