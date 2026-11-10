# Validation plan — Gift cards

## Data model
Card, code, balance, validity.

## Expected implementation
Generate unpredictable codes, track the balance server-side, handle expiry according to the applicable law.

## Tests to plan
1. Nominal: Simulate purchase, partial use and remaining balance.
2. Refusal check: A used-up or expired code is refused.
3. Invariant: A code is never guessable, nor reusable beyond its balance.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
