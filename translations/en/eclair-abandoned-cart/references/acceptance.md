# Validation plan — Abandoned cart reminders

## Data model
Cart, contact, consent, reminder.

## Expected implementation
Check the legal basis, limit the number of reminders, rely on the payment provider's tools where they exist.

## Tests to plan
1. Nominal: Simulate abandonment, reminder and unsubscription.
2. Refusal check: An unsubscribed contact receives no reminder.
3. Invariant: No reminder without consent or a legal basis; immediate unsubscription.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
