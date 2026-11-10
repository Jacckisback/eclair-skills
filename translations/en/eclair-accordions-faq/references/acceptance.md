# Validation plan — FAQ and accordions

## Data model
Question, answer, order.

## Expected implementation
Write real customer questions, use the native FAQ block, which also produces the markup, limit the number per page.

## Tests to plan
1. Nominal: Check keyboard opening and the markup produced.
2. Refusal check: An empty FAQ emits no markup.
3. Invariant: No invented answer or unverified promise.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
