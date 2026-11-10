# Validation plan — Porting WordPress plugins

## Data model
Original plugin, features actually used, native equivalent, gap.

## Expected implementation
List what the plugin really does on the site, look first for the native feature, otherwise the skill from the catalogue, otherwise a custom extension; never copy WordPress PHP code.

## Tests to plan
1. Nominal: Draw up the mapping table for a real site and have it validated.
2. Refusal check: A feature with no equivalent is announced as missing, not simulated.
3. Invariant: No code under an incompatible licence or dependent on the WordPress API is reused.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
