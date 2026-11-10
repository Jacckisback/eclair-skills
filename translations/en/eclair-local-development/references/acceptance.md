# Validation plan — Local development

## Data model
PHP version, web server, copy of the site, test data.

## Expected implementation
Install the same PHP version and the same server rules, restore an anonymised backup, run the tests.

## Tests to plan
1. Nominal: Start the local site and get the test suite to pass.
2. Refusal check: A local copy sends no real email.
3. Invariant: Real customer data is not copied locally without anonymisation.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
