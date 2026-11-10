# Validation plan — Forms and mini-CRM

## Data model
Form, field, consent, contact, source, ticket and status.

## Expected implementation
Define purpose and retention period per form; validate data on the server; protect against spam; compartmentalise files and read permission.

## Tests to plan
1. Nominal: Test spam, attachment, duplicate and GDPR deletion.
2. Refusal check: A user without permission cannot export the contact database.
3. Invariant: A public form must not allow email injection nor let the data appear in the cache.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
