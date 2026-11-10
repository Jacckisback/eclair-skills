# Validation plan — Product reviews

## Data model
Review, rating, author, verified purchase, status.

## Expected implementation
Define proof of purchase, moderation, right of reply and aggregated display; until then, offer manually collected testimonials.

## Tests to plan
1. Nominal: Simulate submission, moderation and publication of a review.
2. Refusal check: A review without a verified purchase is not marked as verified.
3. Invariant: No review published without moderation; no aggregated rating without real reviews.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
