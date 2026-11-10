# Validation plan — Custom content types

## Data model
Business record, fields, list, address, status.

## Expected implementation
Choose between pages with dedicated blocks and an extension with its own storage and GET routes, fix the addresses, plan for list and record.

## Tests to plan
1. Nominal: Create a record type through an extension, with list and detail in GET, then validate the package.
2. Refusal check: An unpublished record is served neither in the list nor at its direct address.
3. Invariant: Never write to the core's content files from an extension.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
