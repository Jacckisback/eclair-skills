# Validation plan — Theme creation

## Data model
theme.json, styles, assets, declared templates, licence and provenance.

## Expected implementation
Start from the official example theme, use supported variables and templates, test the preview then the ZIP, check version compatibility.

## Tests to plan
1. Nominal: Test the theme validator, activation, preview and rollback.
2. Refusal check: A faulty template does not make the site inaccessible, thanks to the planned fallback.
3. Invariant: Never redo the SEO head and canonical or touch the core files.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
