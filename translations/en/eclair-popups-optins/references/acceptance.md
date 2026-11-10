# Validation plan — Pop-ups and opt-in boxes

## Data model
Message, trigger, frequency, action.

## Expected implementation
Prefer a box within the page; otherwise a native dialog triggered by a visitor action, closable with the keyboard, never on arrival.

## Tests to plan
1. Nominal: Open and close with the keyboard and on mobile.
2. Refusal check: A dismissed box does not reappear during the visit.
3. Invariant: No window blocks the content or traps focus.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
