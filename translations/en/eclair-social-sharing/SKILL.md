---
name: eclair-social-sharing
description: "Add share links without third-party scripts. Use on Éclair CMS 2.x when the user wants to: add sharing links without a third-party script. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Share buttons — Éclair CMS 2.x

## Trigger and expected outcome
Use this skill to **add sharing links without a third-party script**. This feature is **achievable today** with the native contract (theme, blocks, GET routes, administration pages, tasks). This skill is an **agent workflow**, not a working PHP extension nor a guarantee of compliance.

**WordPress equivalent:** AddToAny, Social Warfare. Family: Marketing & audience.

## Mandatory diagnosis before any change
1. Read `references/core-map.md` (what the core already does) and `references/native-contract.md`; check the actual CMS version and the capabilities in `GET /<admin>/api/capabilities` (if access is authorised).
2. Read `references/family-contract.md` and `references/acceptance.md`. Never copy the old v0.x pack system or WordPress PHP code into Éclair 2.
3. Identify the data model: **Network, sharing address, label**. Document what is public, what is private and where each piece of data comes from.

## Specific procedure
4. **Flow:** Use simple sharing links and the browser's share API as a progressive enhancement. Describe the states and the errors before writing any code.
5. **Locations:** site-specific code in `site/extensions/<id>/`, appearance in `site/themes/<id>/`, data under `$ctx['data']`, content and settings through the administration or the MCP. Never edit `app/`, `assets/`, `index.php` or the updater.
6. **Current contract:** Achievable with `eclair-extension/1` and the theme contract: cacheable public GET routes, protected administration pages, declarative blocks and settings, scheduled tasks, assets. First check that a native block or setting is not enough.
7. **Security invariant:** No button loads a third-party script or tracker. Also check server-side permissions, escaping with `e()`, data validation and the absence of any secret or personal data in public HTML or in a shared cache.
8. **Evidence:** write the positive test “Share a page from mobile and desktop” and the refusal test “No third-party request before the click”. Measure SEO and performance regressions, document the rollback.
9. **Native validation:** `php tools/validate.php <dossier> --json`, `php tests/run.php` and `php tools/measure.php --check` on an official checkout for every package produced. For a part not supported by the core, provide a gap note and a blocking test, never a fictitious pass.

## Mandatory deliverables
- Mini-specification: goal, users, flows, states, data, measurements.
- Permissions and cache matrix: route, method, session, visibility, indexing.
- Validated `extension.json`/`extension.php` package or theme package, only if a native block or setting is not enough.
- Tests for the positive cases and the refusals, a deactivation procedure that preserves the data, a compatibility note.

## Acceptance criteria
- Share a page from mobile and desktop.
- No third-party request before the click.
- Nothing is published, activated or put into production without an authorised person; no score, ranking or citation by an AI is promised.
- The parts not supported by Éclair 2.0 are explicitly flagged as **not deliverable to production**.

**Maturity status of this skill:** `native-v2-workflow`. See `references/acceptance.md` for reproducible test cases.
