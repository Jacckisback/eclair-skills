---
name: eclair-architecture
description: Use for Éclair CMS v2 architecture decisions, reviewing system boundaries and choosing whether a feature belongs to native settings, a theme, an extension or an isolated core RFC.
---

# Éclair Architecture — preserving the v2 core

## Goal
Design the requested solution **without copying an extension system** and without overloading the cache route. Start with `references/core-map.md` and the code of the current checkout.

## Operating sequence
1. Record the commit, the `ECLAIR_VERSION` version, PHP and the capabilities available through `/admin/api/capabilities` if access is authorised.
2. Classify the goal: native content/setting, site theme, `eclair-extension/1` extension, external service, or a gap in the public contract requiring an RFC.
3. Look first for `Extensions`, `Themes`, `Packages`, `Migrations`, `Store`, `Cache`, `Site`, `Seo`, `Security`, `Mcp` and the docs `docs/ARCHITECTURE-2.md`/`docs/STATUS-2.md`.
4. Describe the boundaries: code under `site/extensions/` or `site/themes/`, data via `Store` and `$ctx['data']`, media under `media/`, no replacement of `app/`.
5. Strictly distinguish the native contract (`eclair-extension/1`) from the old v0.8 experiments (routes/permissions/SQL/outbox), which are incompatible with v2 without porting.
6. Produce an explicit architecture decision: alternatives, API limits, risks, rollback, compatibility test and performance indicators.
7. Have it reviewed, then validate with `php tests/run.php`, `php tools/measure.php --check` and the relevant tests in `tests/extensions.php`.

## Non-negotiables
Preserve SEO/GEO, canonical markup, CSRF/CSP protections, auth handling and the warm cache. An extension never activates itself. Do not claim to handle a transactional checkout, nor student accounts, as long as these contracts are not implemented and tested.

## Deliverables
ADR and before/after mapping, “native / extension / core RFC” decision, constraints, tests and rollback plan. The template `assets/architecture-decision.md` can serve as a starting point.

## V1.0 — Member extensions
The native extension `examples/extensions/member-directory` illustrates separate public accounts: no new role in `Eclair\Users`. A 2.0 core receives extensions via `site/extensions/<id>`; no write in `app/`.

## Éclair 2.0 — prototype v1.1 (experimental)
Éclair 2.0.0 now has an experimental public POST contract only if the v1.1 patch is applied on a development branch. The official core does **not** provide this contract. No direct modification of the core from a skill; prepare an RFC and tests beforehand.

## Éclair 2.0 — registration and recovery (experimental v1.2)

Read `references/member-email-v1.2.md` before any request to create customer/student accounts or to recover a password. The `member-directory` v0.3 module uses public POST routes **outside the official contract**; never promise a direct installation on unmodified Éclair 2.0, nor enable the email flows without a verified HTTPS URL and native tests. Prefer the v2 extension system to any modification of the old v0.x architecture. Keep public and administrator accounts separate, refuse any shared cache for member pages, and treat emails as undelivered as long as no confirmation exists.
