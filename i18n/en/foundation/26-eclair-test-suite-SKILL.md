---
name: eclair-test-suite
description: Use when creating CI, regression, security and performance tests for Éclair CMS 2.0 themes, native extensions and advanced module integrations.
---

# Éclair Test Suite — proof before publication

## Verification order
1. Record the commit and the `ECLAIR_VERSION`; require the official v2 contract. Without a full checkout, limit any claim to the tests that can actually be run.
2. `php -l` on each PHP file produced, then `php tools/validate.php site/extensions/<id> --json` with the corresponding core.
3. `php tests/run.php --unit`, then `php tests/run.php` (HTTP, auth, routes, cache, backups, extensions, themes, WordPress migration).
4. `php tools/measure.php --check`; compare the warm cache and the memory/time budget with the unmodified core.
5. Test inactive installation, activation, idempotent migration, update, route conflict, deactivation, data retention, code removal and any manual purge.
6. If member accounts/SQL: require real PHP/PDO tests, multi-process, per-object authorisations, signed webhooks and restore from backup. `pdo_sqlite` absent = test blocked, not passed.
7. Recommended CI: PHP 8.1 to 8.5 matrix, official `tests.yml`, built archive and Apache/Nginx servers; add jobs specific to the feature.
8. Produce a table of tests run / failed / blocked. Never report “production compatible” from an isolated fixture.

## Deliverables
Scripts and fixtures, execution report, coverage of adversarial cases, budgets and rollback strategy.

## V1.0 — Additional checks
Run `php tests/member-directory.php`, `python3 -m unittest discover -s tests -v`, and `python3 scripts/verify_sample.py`. On a full Éclair 2.0 checkout, it is **imperative** to run `php tools/validate.php examples/extensions/member-directory --json`, then the PHP/HTTP tests of the full CMS and the `tools/measure.php --check` budget before any merge proposal.

## Éclair 2.0 — prototype v1.1 (experimental)
Test `php tests/member-directory.php` + `php tests/member-public.php` and the Python tests. On a real Éclair 2.0.0 clone, apply the patch to a clean feature branch, run `php tools/validate.php`, `php tests/run.php`, `php tools/measure.php --check`, and HTTP/TLS trials. No merge without these criteria.

## Éclair 2.0 — registration and recovery (experimental v1.2)

Read `references/member-email-v1.2.md` before any request to create customer/student accounts or to recover a password. The `member-directory` v0.3 module uses public POST routes **outside the official contract**; never promise a direct installation on unmodified Éclair 2.0, nor enable the email flows without a verified HTTPS URL and native tests. Prefer the v2 extension system to any modification of the old v0.x architecture. Keep public and administrator accounts separate, refuse any shared cache for member pages, and treat emails as undelivered as long as no confirmation exists.
