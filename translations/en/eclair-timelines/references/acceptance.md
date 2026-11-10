# Validation plan — Timelines

## Data model
Step, date, title, text.

## Expected implementation
Render the timeline as an ordered list styled in CSS, readable as a column on mobile.

## Tests to plan
1. Nominal: Check the reading order and the mobile display.
2. Refusal check: A step without a date remains readable and in order.
3. Invariant: The dates and facts displayed are provided by the client.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
