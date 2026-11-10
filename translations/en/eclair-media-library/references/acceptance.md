# Validation plan — Media library

## Data model
File, alternative text, dimensions, usages.

## Expected implementation
Import the media, fill in the alternative texts, identify unused files and duplicates.

## Tests to plan
1. Nominal: Upload several formats and check conversion, dimensions and alternative texts.
2. Refusal check: A file in a forbidden format or a booby-trapped file is rejected on upload.
3. Invariant: Only the formats accepted by the core are uploaded; no executable file.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
