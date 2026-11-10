# Validation plan — Hero sections

## Data model
Title, subtitle, image, button.

## Expected implementation
Write a precise promise, choose a lightweight image, keep a single main heading and one button.

## Tests to plan
1. Nominal: Measure the rendering of the largest element on mobile.
2. Refusal check: Without an image, the section remains readable and well contrasted.
3. Invariant: The main image has explicit dimensions and does not delay rendering.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
