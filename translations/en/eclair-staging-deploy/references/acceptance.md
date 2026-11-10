# Validation plan — Staging and go-live

## Data model
Test copy, differences, go-live checklist.

## Expected implementation
Restore a backup on a protected, non-indexable subdomain, validate theme and features there, then reproduce in production.

## Tests to plan
1. Nominal: Walk through a theme change from the copy to production.
2. Refusal check: The test copy is neither indexed nor accessible without authentication.
3. Invariant: The test copy is password-protected and blocked to robots.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
