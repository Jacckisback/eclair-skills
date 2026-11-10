# Validation plan — Landing pages

## Data model
Promise, proof, offer, call to action.

## Expected implementation
Write a page for a single intent, compose it in native blocks, link the action to a form or a payment link.

## Tests to plan
1. Nominal: Go through the page on mobile up to the action.
2. Refusal check: Proof not provided by the client does not appear.
3. Invariant: No invented testimonial, figure or guarantee.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
