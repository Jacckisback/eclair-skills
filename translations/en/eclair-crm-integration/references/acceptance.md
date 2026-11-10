# Validation plan — CRM synchronisation

## Data model
Contact, company, consent, mapping, external key, provenance.

## Expected implementation
Map strict fields, differentiate directional updates and merging, provide reconciliation and export/deletion.

## Tests to plan
1. Nominal: Test merge, changed email, conflict, deletion and retry.
2. Refusal check: The same contact resynchronised does not create several duplicates in the CRM.
3. Invariant: Do not export contacts without a legal basis or minimal scopes.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
