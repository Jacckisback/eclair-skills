# Validation plan — Donations and non-profits

## Data model
Cause, project, amount, donation link, receipt.

## Expected implementation
Present the mission and the use of funds, connect the donation buttons to the provider's links, leave receipt management to the provider or to the organisation.

## Tests to plan
1. Nominal: Make a donation in test mode and follow the complete journey.
2. Refusal check: An amount modified in the page does not change the amount collected.
3. Invariant: No promise of a tax benefit without confirmation from the organisation.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
