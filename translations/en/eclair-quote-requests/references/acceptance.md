# Validation plan — Quote requests

## Data model
Request, service, budget, timeframe, contact details.

## Expected implementation
Start with the native contact form and guided questions in the page; design the structured form for later.

## Tests to plan
1. Nominal: Send a typical request and check that it is received in full.
2. Refusal check: A request without valid contact details is rejected with a clear message.
3. Invariant: Only the data needed for the quote is requested.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
