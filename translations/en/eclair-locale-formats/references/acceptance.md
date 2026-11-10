# Validation plan — Regional formats

## Data model
Language, country, currency, time zone.

## Expected implementation
Centralise formatting on the server side, never hard-code a format in the templates.

## Tests to plan
1. Nominal: Compare a date and a price in French, English and German.
2. Refusal check: An unknown currency is not displayed with a misleading default symbol.
3. Invariant: A displayed price always corresponds to the currency actually charged.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
