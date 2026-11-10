# Validation plan — Editorial workflow

## Data model
Draft, author, reviewer, planned date, status, schedule entry.

## Expected implementation
Decide who writes and who publishes according to the native permissions, use the editorial schedule and drafts, keep a human review before anything goes live.

## Tests to plan
1. Nominal: Take a piece of content from idea to draft and then to publication by an authorised person.
2. Refusal check: An account limited to content can neither change the settings nor publish in place of another role.
3. Invariant: An agent or a writer without publishing permission puts nothing live.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
