# Validation plan — Calls to action

## Data model
Title, text, button, destination.

## Expected implementation
Define one main action per page, repeat it in the right places, check contrast and an explicit label.

## Tests to plan
1. Nominal: Follow each button to its destination on mobile.
2. Refusal check: A button without a valid destination is not published.
3. Invariant: No misleading link and no open redirect.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
