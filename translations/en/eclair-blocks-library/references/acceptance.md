# Validation plan — Block library

## Data model
Namespaced type, field declaration, limits, rendering and preserved data.

## Expected implementation
Favour native blocks; declare the allowed fields; generate escaped rendering, default values and preservation after deactivation.

## Tests to plan
1. Nominal: Test invalid fields, removal of the extension and reinstallation.
2. Refusal check: The deactivated block is kept but neither executed nor rendered.
3. Invariant: Refuse to execute HTML/JS coming from fields; no data loss when the block is missing.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
