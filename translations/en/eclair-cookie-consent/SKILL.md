---
name: eclair-cookie-consent
description: "Stay banner-free when possible, and compliant when a tracker is added. Use on Éclair CMS 2.x when the user wants to: stay banner-free whenever possible, and compliant when a tracker is added. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Cookies and consent — Éclair CMS 2.x

## Trigger and expected outcome
Use this skill to **stay banner-free whenever possible, and compliant when a tracker is added**. This feature is **achievable today** with the native contract (theme, blocks, GET routes, administration pages, tasks). This skill is an **agent workflow**, not a working PHP extension nor a guarantee of compliance.

**WordPress equivalent:** CookieYes, Complianz, Cookie Notice. Family: Security & privacy.

## Mandatory diagnosis before any change
1. Read `references/core-map.md` (what the core already does) and `references/native-contract.md`; check the actual CMS version and the capabilities in `GET /<admin>/api/capabilities` (if access is authorised).
2. Read `references/family-contract.md` and `references/acceptance.md`. Never copy the old v0.x pack system or WordPress PHP code into Éclair 2.
3. Identify the data model: **Tracker, purpose, consent, proof**. Document what is public, what is private and where each piece of data comes from.

## Specific procedure
4. **Flow:** Inventory the actual trackers; without a tracker, no banner; otherwise prior consent, refusal as simple as acceptance and an information page. Describe the states and the errors before writing any code.
5. **Locations:** site-specific code in `site/extensions/<id>/`, appearance in `site/themes/<id>/`, data under `$ctx['data']`, content and settings through the administration or the MCP. Never edit `app/`, `assets/`, `index.php` or the updater.
6. **Current contract:** Achievable with `eclair-extension/1` and the theme contract: cacheable public GET routes, protected administration pages, declarative blocks and settings, scheduled tasks, assets. First check that a native block or setting is not enough.
7. **Security invariant:** No tracker subject to consent is set before acceptance. Also check server-side permissions, escaping with `e()`, data validation and the absence of any secret or personal data in public HTML or in a shared cache.
8. **Evidence:** write the positive test “Inspect cookies and requests before and after the choice” and the refusal test “After a refusal, no third-party tracker is loaded”. Measure SEO and performance regressions, document the rollback.
9. **Native validation:** `php tools/validate.php <dossier> --json`, `php tests/run.php` and `php tools/measure.php --check` on an official checkout for every package produced. For a part not supported by the core, provide a gap note and a blocking test, never a fictitious pass.

## Mandatory deliverables
- Mini-specification: goal, users, flows, states, data, measurements.
- Permissions and cache matrix: route, method, session, visibility, indexing.
- Validated `extension.json`/`extension.php` package or theme package, only if a native block or setting is not enough.
- Tests for the positive cases and the refusals, a deactivation procedure that preserves the data, a compatibility note.

## Acceptance criteria
- Inspect cookies and requests before and after the choice.
- After a refusal, no third-party tracker is loaded.
- Nothing is published, activated or put into production without an authorised person; no score, ranking or citation by an AI is promised.
- The parts not supported by Éclair 2.0 are explicitly flagged as **not deliverable to production**.

**Maturity status of this skill:** `native-v2-workflow`. See `references/acceptance.md` for reproducible test cases.
