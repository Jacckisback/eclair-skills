# Validation plan — Support and tickets

## Data model
Ticket, requester, status, exchanges, priority.

## Expected implementation
Start with a contact form and an inbox; design statuses, response times and a tracking area for later.

## Tests to plan
1. Nominal: Walk through a request from opening to closure.
2. Refusal check: A ticket cannot be read by guessing its number.
3. Invariant: A requester sees only their own tickets.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
