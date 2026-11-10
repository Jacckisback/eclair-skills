# Validation plan — Command-line tools

## Data model
Command, input, output, exit code.

## Expected implementation
On a checkout of the core, run the validator, the test suite and the budget measurement; integrate these commands into the project's CI.

## Tests to plan
1. Nominal: Validate a package and read the JSON report.
2. Refusal check: An invalid package makes the command and the CI fail.
3. Invariant: No command is run on production without a backup.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
