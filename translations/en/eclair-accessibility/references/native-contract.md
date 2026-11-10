# Applying the native contract to the skill eclair-accessibility

This skill uses exclusively what Éclair CMS 2.0.x ships: the core features, the theme contract and the `eclair-extension/1` contract. Official reference: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Position of this skill

Éclair v2 exposes themes under site/themes and declarative extension blocks. Do not modify app/, index.php, the CSP or cache generation; validate themes with tools/validate.php.

## Practical safeguard

On a real checkout, re-read `eclair/index.php`, run `php tools/validate.php` on every package produced and `php tests/run.php`. If the request goes beyond the native features, public GET routes, protected administration pages, blocks, settings and `Store`, produce a separate change request; **never simulate its availability**.
