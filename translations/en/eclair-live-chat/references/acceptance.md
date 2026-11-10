# Validation plan — Live chat

## Data model
Channel, opening hours, conversation link.

## Expected implementation
Prefer a link to a messaging channel (WhatsApp, email, telephone) with opening hours; a third-party widget depends on the native content policy.

## Tests to plan
1. Nominal: Open the channel from mobile and desktop.
2. Refusal check: Outside opening hours, the site says so instead of promising an immediate reply.
3. Invariant: No widget loads a tracker before an action by the visitor.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
