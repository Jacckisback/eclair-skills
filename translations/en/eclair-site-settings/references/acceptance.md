# Validation plan — Site settings

## Data model
Name, description, logo, contact details, language, theme, art direction.

## Expected implementation
Read the site's capabilities, fill in the settings through the administration, preview before saving.

## Tests to plan
1. Nominal: Set up a new site and check the public rendering.
2. Refusal check: An account without the Settings permission modifies no setting.
3. Invariant: No native protection is disabled to save time.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
