# Validation plan — Responsive UX

## Data model
Breakpoints, density, text width, menu, forms and media.

## Expected implementation
Design mobile-first; keep the information hierarchy; test small screens, target sizes and orientations.

## Tests to plan
1. Nominal: Test 320px, 375px, tablet and mobile keyboard.
2. Refusal check: A primary action remains visible and usable on a narrow screen without horizontal scrolling.
3. Invariant: No essential content hidden on mobile or dependent on animation.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
