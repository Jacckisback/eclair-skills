# Validation plan — Deals and promo codes

## Data model
Offer, merchant, code, end date, link.

## Expected implementation
Display conditions and end date, automatically remove expired offers, mark affiliate links.

## Tests to plan
1. Nominal: Publish a dated offer and observe its removal on expiry.
2. Refusal check: A paid link never appears without a disclosure.
3. Invariant: No expired or unverifiable offer presented as valid.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
