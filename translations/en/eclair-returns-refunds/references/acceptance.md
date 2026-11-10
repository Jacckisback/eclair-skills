# Validation plan — Returns and refunds

## Data model
Return request, reason, state, refund.

## Expected implementation
Publish the native returns policy on product pages, handle requests through the contact form, refund at the provider; design the structured tracking.

## Tests to plan
1. Nominal: Walk through a return request from receipt to refund.
2. Refusal check: A request outside the time limit receives a reasoned reply, not an automatic refund.
3. Invariant: A refund is triggered only by an authorised person, at the provider.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
