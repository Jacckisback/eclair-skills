# Validation plan — Image galleries

## Data model
Gallery, images, captions, order.

## Expected implementation
Compose the gallery as a CSS grid from the images in the media library, with captions and alternative texts.

## Tests to plan
1. Nominal: Display a gallery of twenty images on mobile and measure its weight.
2. Refusal check: An image removed from the media library does not leave a broken thumbnail.
3. Invariant: No image is loaded from a third-party domain.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
