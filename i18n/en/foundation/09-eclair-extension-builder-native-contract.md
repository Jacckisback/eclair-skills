# Applying the native contract to the skill eclair-extension-builder

This skill uses exclusively the `eclair-extension/1` contract shipped in Éclair CMS 2.0.0 and not the APIs of the old prototypes. Official reference: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Practical safeguard

On a real checkout, re-read `eclair/index.php`, run `php tools/validate.php` on every package produced and `php tests/run.php`. If the requested contract goes beyond public GET routes, admin permissions, fields/blocks and `Store`, produce a separate RFC; **never simulate its availability**.
