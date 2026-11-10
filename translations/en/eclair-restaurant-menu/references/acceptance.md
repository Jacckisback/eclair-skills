# Validation plan — Restaurant menu

## Data model
Dish, price, allergens, category, availability.

## Expected implementation
Enter the menu supplied by the restaurateur, display prices and allergens, keep a readable HTML version rather than a PDF alone.

## Tests to plan
1. Nominal: Proofread the published menu with the restaurateur, on mobile.
2. Refusal check: A dish without validated allergen information is flagged, not filled in.
3. Invariant: No price or allergen invented or inferred.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
