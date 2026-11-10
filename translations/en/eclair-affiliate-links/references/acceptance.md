# Validation plan — Affiliate links

## Data model
Link, programme, notice, host content.

## Expected implementation
Enable the bundled affiliate feature, declare the programmes, let the core add the notice and the sponsored attribute.

## Tests to plan
1. Nominal: Publish a comparison and check the notice and the link attributes.
2. Refusal check: An affiliate link is never presented as an independent review.
3. Invariant: No affiliate link without a visible advertising notice.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
