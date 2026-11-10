# Validation plan — Breadcrumb trail

## Data model
Levels, labels, addresses.

## Expected implementation
Check the consistency between the tree structure, the displayed breadcrumb trail and the core's structured data.

## Tests to plan
1. Nominal: Compare the displayed trail and the markup over three levels of depth.
2. Refusal check: An orphan page does not display an inconsistent trail.
3. Invariant: The breadcrumb trail reveals no unpublished page.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
