# Validation plan — Backups and restoration

## Data model
Backup archive, date, destination, restoration test.

## Expected implementation
Enable the downloadable backup or the backup to the remote storage provided for by the core, set the frequency, restore on a copy to check.

## Tests to plan
1. Nominal: Restore the latest backup on a test installation and compare.
2. Refusal check: A modified or booby-trapped archive is refused on restoration.
3. Invariant: A backup contains personal data: it is stored encrypted or in a safe place, never in a public folder.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
