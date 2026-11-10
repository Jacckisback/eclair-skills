# Validation plan — Maps and directions

## Data model
Address, coordinates, map image, directions link.

## Expected implementation
Prefer a static map image with a link to the directions; a third-party interactive map depends on the native content policy.

## Tests to plan
1. Nominal: Check image, alternative text and directions link on mobile.
2. Refusal check: No request to a map service when the page loads.
3. Invariant: No third-party map loaded before an action by the visitor.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
