# Validation plan — Image viewer

## Data model
Image, enlarged version, caption.

## Expected implementation
Use the native dialog or a link to the image, handle focus, the Escape key and back, with no dependency.

## Tests to plan
1. Nominal: Open, navigate and close with the keyboard.
2. Refusal check: Without JavaScript, the click simply opens the image.
3. Invariant: Focus is trapped then correctly returned; no external content.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
