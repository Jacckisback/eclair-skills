# Validation plan — Pricing tables

## Data model
Plan, price, period, features, button.

## Expected implementation
Compose the plans as comparable cards, display prices including or excluding tax without ambiguity and link each button to the right action.

## Tests to plan
1. Nominal: Compare three plans on mobile and check every link.
2. Refusal check: A plan without a validated price is not displayed.
3. Invariant: No invented price, discount or legal notice.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
