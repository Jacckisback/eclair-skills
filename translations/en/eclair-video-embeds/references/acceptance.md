# Validation plan — Videos

## Data model
Video, source, preview image, subtitles.

## Expected implementation
Use the native video block, prefer a clickable facade for third-party platforms, provide subtitles or a transcript.

## Tests to plan
1. Nominal: Check that no third-party request is sent before the click.
2. Refusal check: A video address from an unauthorised domain is rejected.
3. Invariant: No third-party player is loaded before the visitor clicks.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
