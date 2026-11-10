# Applying the native contract to the skill eclair-social-sharing

This skill uses exclusively what Éclair CMS 2.0.x ships: the core features, the theme contract and the `eclair-extension/1` contract. Official reference: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Position of this skill

Achievable with `eclair-extension/1` and the theme contract: cacheable public GET routes, protected administration pages, declarative blocks and settings, scheduled tasks, assets. First check that a native block or setting is not enough.

## Practical safeguard

On a real checkout, re-read `eclair/index.php`, run `php tools/validate.php` on every package produced and `php tests/run.php`. If the request goes beyond the native features, public GET routes, protected administration pages, blocks, settings and `Store`, produce a separate change request; **never simulate its availability**.
