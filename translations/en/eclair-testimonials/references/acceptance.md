# Validation plan — Testimonials and reviews

## Data model
Testimonial, author, date, authorisation.

## Expected implementation
Collect real testimonials with written authorisation, present them as quotations, state the source.

## Tests to plan
1. Nominal: Check that every published testimonial has a recorded authorisation.
2. Refusal check: A review without a verifiable source is not published.
3. Invariant: No review that is invented, modified or selected in a misleading way.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
