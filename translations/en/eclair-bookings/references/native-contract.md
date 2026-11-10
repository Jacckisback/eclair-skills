# Applying the native contract to the skill eclair-bookings

This skill uses exclusively what Éclair CMS 2.0.x ships: the core features, the theme contract and the `eclair-extension/1` contract. Official reference: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Position of this skill

Public showcase pages are possible with GET; bookings, payments, applications, CRM and personal data require secure POST, suitable storage and permissions verified server-side.

## Practical safeguard

On a real checkout, re-read `eclair/index.php`, run `php tools/validate.php` on every package produced and `php tests/run.php`. If the request goes beyond the native features, public GET routes, protected administration pages, blocks, settings and `Store`, produce a separate change request; **never simulate its availability**.
