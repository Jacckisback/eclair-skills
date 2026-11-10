# Validation plan — Éclair art direction

## Data model
Positioning, identity, typography, colours, components, photographs and real content.

## Expected implementation
Define a visual world drawn from the business, compose sections, adjust CSS and test themes with real content; favour site/themes and the existing blocks.

## Tests to plan
1. Nominal: Test contrast, multi-page consistency and mobile versions.
2. Refusal check: The new appearance remains readable without JavaScript and respects the existing links.
3. Invariant: Never modify app/theme/ or break the SEO, the CSP or the fast path.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
