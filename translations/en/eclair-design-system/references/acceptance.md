# Validation plan — Design system

## Data model
Tokens, grid, spacing, colours, typography, components and states.

## Expected implementation
Declare the token scale, reuse components, document states and variants; Éclair theme compatibility.

## Tests to plan
1. Nominal: Test contrast, consistency and theme switching.
2. Refusal check: Changing the main colour makes no links or errors illegible.
3. Invariant: Do not introduce a heavy CSS stylesheet or a JS library without proof of need.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
