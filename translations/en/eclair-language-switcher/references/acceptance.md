# Validation plan — Language switcher

## Data model
Current language, available versions, labels.

## Expected implementation
List the languages by their name in their own language, point to the equivalent version, with no forced automatic redirect.

## Tests to plan
1. Nominal: Switch language from a deep page and land on its equivalent.
2. Refusal check: With no equivalent, the link leads to the language's home page, not to an error.
3. Invariant: No redirect by IP address; the visitor's choice is respected.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
