# Validation plan — MCP connector

## Data model
Authorised client, token, available tools, drafts created.

## Expected implementation
Have the owner enable the connector, authorise the client, work in drafts and proposals, know how to cut off access.

## Tests to plan
1. Nominal: Create a draft through the connector, then revoke access.
2. Refusal check: After revocation, every request from the client is refused.
3. Invariant: The connector neither publishes nor deletes; access is revocable at any time.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
