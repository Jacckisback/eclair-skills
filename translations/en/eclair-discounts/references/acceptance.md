# Validation plan — Promotions and coupons

## Data model
Code, budget, dates, quota, cart conditions, usages and exclusions.

## Expected implementation
Define calculation order and rounding; check the coupon before the order; count usages atomically; trace cancellation and return.

## Tests to plan
1. Nominal: Test expired and exhausted coupons, threshold and exclusions.
2. Refusal check: Two simultaneous orders cannot consume the last single coupon.
3. Invariant: The eligibility decision comes from server data and not from the discount entered in HTML.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
