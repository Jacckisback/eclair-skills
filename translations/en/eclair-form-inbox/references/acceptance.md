# Validation plan — Received messages

## Data model
Message, status, reply, retention period.

## Expected implementation
Define who reads and replies, within what time, how long the messages are kept, how they are deleted.

## Tests to plan
1. Nominal: Handle a message from receipt to archiving.
2. Refusal check: An account without the Messages permission has access to no message.
3. Invariant: Limited retention period and restricted access permission.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
