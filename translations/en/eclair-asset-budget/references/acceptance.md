# Validation plan — Weight budget

## Data model
Budget per resource type, measurement, deviation.

## Expected implementation
Set budgets per page type, measure with the core's tool, refuse any addition that exceeds them without justification.

## Tests to plan
1. Nominal: Run the budget measurement on the site and on the package produced.
2. Refusal check: A package that exceeds the budget is not delivered as is.
3. Invariant: No third-party dependency loaded for a decorative function.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
