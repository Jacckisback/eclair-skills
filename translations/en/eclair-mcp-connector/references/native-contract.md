# Applying the native contract to the skill eclair-mcp-connector

This skill uses exclusively what Éclair CMS 2.0.x ships: the core features, the theme contract and the `eclair-extension/1` contract. Official reference: https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md

## Position of this skill

The feature exists in the core: configure it through the administration or, as a draft, through the MCP connector. Do not duplicate it in an extension and never modify the core to adapt it; if a need goes beyond what the core offers, report it as a gap.

## Practical safeguard

On a real checkout, re-read `eclair/index.php`, run `php tools/validate.php` on every package produced and `php tests/run.php`. If the request goes beyond the native features, public GET routes, protected administration pages, blocks, settings and `Store`, produce a separate change request; **never simulate its availability**.
