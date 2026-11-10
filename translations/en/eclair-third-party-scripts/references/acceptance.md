# Validation plan — Third-party scripts

## Data model
Script, purpose, weight, domain, consent required.

## Expected implementation
Inventory every script request, look for a script-free alternative, document the blocking by the native content policy where it exists.

## Tests to plan
1. Nominal: Measure weight and requests before and after each accepted addition.
2. Refusal check: A script from an unauthorised domain does not run.
3. Invariant: No script is injected by bypassing the Content-Security-Policy.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
