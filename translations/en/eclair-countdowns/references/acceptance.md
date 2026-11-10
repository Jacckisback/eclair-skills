# Validation plan — Countdowns

## Data model
Target date, time zone, end message.

## Expected implementation
Write the date in the HTML, animate as a progressive enhancement, plan for the state after the deadline and for cache invalidation.

## Tests to plan
1. Nominal: Test before, during and after the deadline and in two time zones.
2. Refusal check: After the deadline, the cached page no longer displays an expired offer.
3. Invariant: No false urgency: the date corresponds to a real event.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
