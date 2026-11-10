# Validation plan — API connectors

## Data model
OAuth/token, scopes, quotas, errors, pagination, version and logs.

## Expected implementation
Define the API schema, isolate secrets, validate incoming schemas, plan timeouts/circuit breaker and versioning.

## Tests to plan
1. Nominal: Test timeout, 429, 500, malformed response and revocation.
2. Refusal check: A 500 from the provider damages neither local data nor public rendering.
3. Invariant: Do not allow SSRF or arbitrary dynamic URLs; never log a token.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
