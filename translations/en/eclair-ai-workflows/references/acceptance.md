# Validation plan — AI workflows

## Data model
Draft, proposal, validation, model, cost, source and audit.

## Expected implementation
Use the core's MCP capabilities, keep a human in the loop, limit access and budget; evaluate quality and hallucinations.

## Tests to plan
1. Nominal: Test prompt injection, context change and rollback.
2. Refusal check: A hostile instruction in an imported article does not become an executed command.
3. Invariant: No AI publishes, deploys, deletes or modifies PHP directly through MCP without review.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
