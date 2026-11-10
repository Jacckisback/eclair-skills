# Validation plan — Automation platforms

## Data model
Scenario, trigger, transmitted data.

## Expected implementation
Expose read-only what the platform can query (feeds, public JSON); design the reception of events for later.

## Tests to plan
1. Nominal: Have the platform read a public feed and trigger a scenario.
2. Refusal check: An unauthenticated incoming call modifies nothing on the site.
3. Invariant: No personal data is exposed in a public endpoint to make an automation easier.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
