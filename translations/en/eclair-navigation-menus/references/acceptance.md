# Validation plan — Navigation menus

## Data model
Menu, entry, order, target, location.

## Expected implementation
Limit the main menu to the essential journeys, put the rest in the footer, test with keyboard and on mobile.

## Tests to plan
1. Nominal: Compose the menus and go through them with the keyboard and on mobile.
2. Refusal check: An unpublished page disappears from the menu or is flagged, never served as a 404 from the navigation.
3. Invariant: No menu link points to a draft or to an unintended external address.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
