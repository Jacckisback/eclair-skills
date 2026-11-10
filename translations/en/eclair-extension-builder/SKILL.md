---
name: eclair-extension-builder
description: Use when creating or adapting an Éclair CMS 2.0 optional server extension that uses extension.json, extension.php and the native eclair-extension/1 contract.
---

# Éclair Extension Builder — building an extension that is genuinely installable in v2

## Goal
Create an **`eclair-extension/1` package that conforms to the v2 core**. Do not use the `manifest.json` manifest or the `events.php` / `services.php` files of the old prototypes as if they were supported.

## Process
1. Read `references/core-map.md`, `docs/EXTENSION-CONTRACT.md`, `docs/schemas/extension.schema.json` and `examples/extensions/bonjour` from the checkout.
2. Check `ECLAIR_VERSION` and the `eclair-extension/1` contract through the code and, if accessible, the capabilities API.
3. Define `id`, `version`, `requires`, `depends`, `provides`, `entry`, routes, blocks, fields, assets, `tasks`, migrations; use only the fields of the schema.
4. Deliver into `site/extensions/<id>/` **without writing in `app/`**; the PHP entry must return an object and must output nothing when it is loaded.
5. Control the output with `e()`; read the settings from `$ctx['settings']`; store via `Eclair\Store` under `$ctx['data']`. For secrets: a private location and a documented no-backup policy.
6. Public GET routes only. On a public page that displays session or individual data: stop and request a new identity/cache contract; no fake workaround.
7. Compute the SHA-256 hashes of the files and declare them in `files`, except `extension.json`. Generate a ZIP package whose root contains the manifest.
8. `php tools/validate.php chemin/extension --json`; fix all errors before proposing the import, then test `php tests/run.php` and `php tools/measure.php --check`.
9. An authorised person imports, previews/checks, activates; document deactivation, removal of the code and retention of the data.

## Deliverables
`extension.json`, `extension.php` entry, references, tests, proof of official validation and installation manual. Original example in `examples/extensions/skill-sample/`; verify on the exact core before deployment.

## V1.0 — Advanced template delivered
Consult `examples/extensions/member-directory`: it proves native admin GET/POST routes and a PHP library loaded only by the extension. Do not turn its admin GET into a public login, nor add a POST to `routes.public` (incompatible with the v2 contract).

## Éclair 2.0 — prototype v1.1 (experimental)
A public POST route prototype is included in `examples/extensions/member-directory/`. It is rejected by the official 2.0 core. Use the manifest only with the experimental patch and the explicit agreement of a maintainer, never in production. POST requires `cache:false`, TLS, CSRF, relative redirect.

## Éclair 2.0 — registration and recovery (experimental v1.2)

Read `references/member-email-v1.2.md` before any request to create customer/student accounts or to recover a password. The `member-directory` v0.3 module uses public POST routes **outside the official contract**; never promise a direct installation on unmodified Éclair 2.0, nor enable the email flows without a verified HTTPS URL and native tests. Prefer the v2 extension system to any modification of the old v0.x architecture. Keep public and administrator accounts separate, refuse any shared cache for member pages, and treat emails as undelivered as long as no confirmation exists.
