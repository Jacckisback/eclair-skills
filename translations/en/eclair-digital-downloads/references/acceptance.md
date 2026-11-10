# Validation plan — Digital products

## Data model
Digital product, purchase, temporary delivery link.

## Expected implementation
Have the file delivered by the provider or through a signed, time-limited link; never place the file at a public address.

## Tests to plan
1. Nominal: Simulate purchase, delivery and link expiry.
2. Refusal check: An expired or shared link no longer gives access to the file.
3. Invariant: No paid file is accessible without a verified purchase.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
