# Validation plan — Dark mode

## Data model
Light and dark colour schemes, visitor preference.

## Expected implementation
Define the theme's colour variables for prefers-color-scheme, check contrasts, images and logos.

## Tests to plan
1. Nominal: Check the contrasts of both modes on the typical pages.
2. Refusal check: A dark logo does not become invisible in dark mode.
3. Invariant: No cookie is needed to respect the system preference.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
