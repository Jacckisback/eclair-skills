# Validation plan — Recipes

## Data model
Recipe, ingredients, steps, times, servings.

## Expected implementation
Structure each recipe into ingredients and steps, add times and servings, provide a printable version.

## Tests to plan
1. Nominal: Follow a published recipe on mobile and print it.
2. Refusal check: A recipe without quantities is not published.
3. Invariant: No unsubstantiated health claim.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
