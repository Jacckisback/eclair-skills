---
name: eclair-cache-contract
description: Use when deciding Éclair CMS v2 static/uncached extension route behavior, invalidation, privacy and performance budgets.
---

# Éclair Cache Contract — keeping the cache safe

## Decision
1. Read `eclair/index.php`, `Cache.php`, `Extensions::route()` and `docs/EXTENSION-CONTRACT.md` of the targeted v2 core.
2. For extension pages whose public content is identical for everyone, `routes.public[].cache` may be `true` after the rendering dependencies have been checked.
3. For private content, user states, baskets, tokens or personalised prices: **no shared cache** (`Cache-Control: private, no-store`), `noindex` where relevant and a server authentication contract. Never claim that a `cache:false` implements authentication on its own.
4. Measure GET/HEAD and query strings, first generation then cache HIT, data editing, activation/deactivation and migrations. Check the CMS routes and the `data/ext-public.php` index.
5. Never add a lookup or a registry read to the `index.php` fast path without a measured budget and a security justification.
6. Test `php tools/measure.php --check` and the budgets in `tools/budgets.json`, then compare with a clean baseline using the same PHP version and data.
7. Check the purge after activation and that unaffected public pages remain cacheable; test cookies and headers under concurrency.

## Deliverables
URL × method × identity × cache matrix, measurements and isolation tests.

## V1.0 — Identity and cache
Never serve a personalised page from a shared cache. The existing administrator routes are already `private, no-store`; future public member pages require a private-route contract before any opening. Never assume that `cache:false` automatically implements complete session/CSRF guarantees.

## Éclair 2.0 — prototype v1.1 (experimental)
Public GET forms use `Security::formField()` and must be declared `cache:false`. Their responses must not reach the core's fast path. POST is excluded from the fast path and forced to no-store. Test the purge on activation of the module and verify the absence of cookies/identities in the shared-cache HTML.

## Éclair 2.0 — registration and recovery (experimental v1.2)

Read `references/member-email-v1.2.md` before any request to create customer/student accounts or to recover a password. The `member-directory` v0.3 module uses public POST routes **outside the official contract**; never promise a direct installation on unmodified Éclair 2.0, nor enable the email flows without a verified HTTPS URL and native tests. Prefer the v2 extension system to any modification of the old v0.x architecture. Keep public and administrator accounts separate, refuse any shared cache for member pages, and treat emails as undelivered as long as no confirmation exists.
