# Validation plan — Commerce Pro architecture

## Data model
Catalogue, cart, prices frozen per line, order, payment, refund, stock, invoice and status log.

## Expected implementation
Design an order/payment state machine, separate public reads from private writes, choose transactional storage, formalise the PSP connector; identify the points not provided by Éclair v2.

## Tests to plan
1. Nominal: Simulate purchase, webhook confirmation, retry, refund, stock and cancellation.
2. Refusal check: Same payment notification delivered twice => a single order transition.
3. Invariant: No payment is declared successful from the browser redirect alone; the server validates an authenticated PSP event.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
