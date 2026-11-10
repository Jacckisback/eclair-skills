# Validation plan — Data tables

## Data model
Table, headers, rows, caption.

## Expected implementation
Use the native table block, add a caption and headers, plan for controlled horizontal scrolling.

## Tests to plan
1. Nominal: Read the table on mobile and with a screen reader.
2. Refusal check: A wide table does not cause the whole page to scroll horizontally.
3. Invariant: No personal data in a public table without consent.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
