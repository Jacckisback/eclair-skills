# Validation plan — Badges and points

## Data model
Rule, points, badge, leaderboard.

## Expected implementation
Set simple rules that are verifiable server-side, plan for withdrawal in case of abuse and an option not to appear on the leaderboard.

## Tests to plan
1. Nominal: Simulate earning, withdrawal and leaderboard display.
2. Refusal check: An artificially repeated action does not earn points twice.
3. Invariant: No point is awarded on the strength of information sent by the browser.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
