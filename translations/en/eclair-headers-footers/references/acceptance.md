# Validation plan — Headers and footers

## Data model
Logo, menu, contact details, legal links.

## Expected implementation
Go through a theme package in site/themes, respect the variables of the theme contract, keep the skip link and the legal links.

## Tests to plan
1. Nominal: Validate the theme and check the header and footer on all the typical pages.
2. Refusal check: A theme rejected by the validator is not delivered.
3. Invariant: Never generate SEO tags or headers already provided by the core yourself.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
