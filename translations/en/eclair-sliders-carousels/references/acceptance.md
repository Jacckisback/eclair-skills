# Validation plan — Slideshows and carousels

## Data model
Slide, image, text, link, order.

## Expected implementation
Prefer a single strong image; otherwise CSS scrolling with keyboard controls, pause and no imposed autoplay.

## Tests to plan
1. Nominal: Navigate with the keyboard and a screen reader, measure the layout shift.
2. Refusal check: Without JavaScript, all the slide content remains readable.
3. Invariant: No heavy third-party library; prefers-reduced-motion respected.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
