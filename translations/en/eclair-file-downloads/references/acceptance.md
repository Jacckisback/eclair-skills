# Validation plan — Downloads

## Data model
File, title, version, size, host page.

## Expected implementation
Store the public files in the media library, display weight and format, version the replaced files.

## Tests to plan
1. Nominal: Download each file and check the stated type and size.
2. Refusal check: A replaced file does not leave the old version accessible by mistake.
3. Invariant: No private or paid file is placed at a guessable public address.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
