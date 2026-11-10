---
name: eclair-storage
description: Use when choosing Éclair CMS v2 extension persistence, migrations, backups or SQL requirements for commerce, forums or course progress.
---

# Éclair Storage — choosing the right persistence

## Storage decision
1. For Éclair content and settings, use `Eclair\Store` and the `data/ext/<id>/` prefix obtained via `$ctx['data']`.
2. Check `Store::locked`, atomic writes and the volumes actually handled; do not invent any transactional multi-file guarantee.
3. For orders/payments/stock and concurrent LMS progress: specify SQLite or MySQL **as an optional dependency of the module** with its migrations, constraints, transactions, backup and recovery. The native v2 contract does not provide a generic PDO for extensions.
4. Declare personal data, retention, deletion and export; do not keep keys or tokens in backups.
5. Native extension migrations via the `migrations[]` manifest entry and the `migrate` method: additive, versioned, idempotent. An SQL schema migration must have a separate plan, not be triggered on a GET page.
6. Plan for a consistent backup, a cold restore and a rollback test. If SQL is unavailable on shared hosting, announce the feature as unavailable rather than falling back on unreliable persistence.
7. Test collisions, restarts, concurrency, duplicates, corruption, chmod/symlink, backup and reconciliation.

## Rules
Native storage without a database must remain possible for a simple site. The v0.5/v0.8 SQL prototypes are neither installed nor recognised by v2. Do not promise exactly-once for external effects.

## Deliverables
Schema, invariant matrix, migration/restore protocol, hosting requirements, transaction and integrity tests.

## V1.0 — Lightweight accounts model
The `member-directory` prototype respects `data/ext/<id>/`, atomic writes and a global lock. Storage across several files **is not an SQL transaction**. The quota of 1,000 accounts is a lab limit: any commercial project with many members must first have the transactional SQL contract.

## Éclair 2.0 — prototype v1.1 (experimental)
The demonstrator's storage still uses the protected `Store` files and a global lock. It is capped at 1000 accounts; no promise of multi-file atomicity, of access at scale or of transactional fault tolerance. An SQL backend is a prerequisite before any business use.

## Éclair 2.0 — registration and recovery (experimental v1.2)

Read `references/member-email-v1.2.md` before any request to create customer/student accounts or to recover a password. The `member-directory` v0.3 module uses public POST routes **outside the official contract**; never promise a direct installation on unmodified Éclair 2.0, nor enable the email flows without a verified HTTPS URL and native tests. Prefer the v2 extension system to any modification of the old v0.x architecture. Keep public and administrator accounts separate, refuse any shared cache for member pages, and treat emails as undelivered as long as no confirmation exists.
