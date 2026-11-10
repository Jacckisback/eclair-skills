# Validation plan — Email marketing services

## Data model
List, hosted form, API key, synchronisation.

## Expected implementation
Use the service's hosted form; store any API key in the extension's secrets; synchronise by task if necessary.

## Tests to plan
1. Nominal: Subscribe a test address and find it in the service.
2. Refusal check: A revoked key produces a logged error, not a leak.
3. Invariant: No API key in the code, the repository or a public page.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
