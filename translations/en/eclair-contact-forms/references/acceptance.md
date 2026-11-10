# Validation plan — Contact form

## Data model
Message, name, e-mail, subject, date, read status.

## Expected implementation
Place the native contact block, set the recipient, test sending and receipt, display the information notice.

## Tests to plan
1. Nominal: Send a real message and find it in the admin and by e-mail.
2. Refusal check: Repeated submissions in bursts are rate-limited by the core.
3. Invariant: Messages are visible only to accounts with the Messages permission.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
