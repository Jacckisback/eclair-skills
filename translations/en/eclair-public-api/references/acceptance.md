# Validation plan — Read-only public API

## Data model
Resource, public fields, pagination, version.

## Expected implementation
Declare cacheable GET routes that return bounded, versioned JSON; document that writing is not open.

## Tests to plan
1. Nominal: Read list and detail, pagination and empty case.
2. Refusal check: Unpublished content is returned by no route.
3. Invariant: Only content that is already public is exposed; no sensitive internal identifier.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
