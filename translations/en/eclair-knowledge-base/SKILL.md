---
name: eclair-knowledge-base
description: "Create documentation or a help centre. Use on Éclair CMS 2.x when the user wants to: create documentation or a help centre. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Knowledge base — Éclair CMS 2.x

## Trigger and expected outcome
Use this skill to **create documentation or a help centre**. This feature is **achievable today** with the native contract (theme, blocks, GET routes, administration pages, tasks). This skill is an **agent workflow**, not a working PHP extension nor a guarantee of compliance.

**WordPress equivalent:** BetterDocs, Echo Knowledge Base. Family: Business apps.

## Mandatory diagnosis before any change
1. Read `references/core-map.md` (what the core already does) and `references/native-contract.md`; check the actual CMS version and the capabilities in `GET /<admin>/api/capabilities` (if access is authorised).
2. Read `references/family-contract.md` and `references/acceptance.md`. Never copy the old v0.x pack system or WordPress PHP code into Éclair 2.
3. Identify the data model: **Help article, section, version, update date**. Document what is public, what is private and where each piece of data comes from.

## Specific procedure
4. **Flow:** Organise by users' problems, one answer per page, navigation by sections and internal search. Describe the states and the errors before writing any code.
5. **Locations:** site-specific code in `site/extensions/<id>/`, appearance in `site/themes/<id>/`, data under `$ctx['data']`, content and settings through the administration or the MCP. Never edit `app/`, `assets/`, `index.php` or the updater.
6. **Current contract:** Achievable with `eclair-extension/1` and the theme contract: cacheable public GET routes, protected administration pages, declarative blocks and settings, scheduled tasks, assets. First check that a native block or setting is not enough.
7. **Security invariant:** No untested procedure is published. Also check server-side permissions, escaping with `e()`, data validation and the absence of any secret or personal data in public HTML or in a shared cache.
8. **Evidence:** write the positive test “Solve three typical problems using the documentation alone” and the refusal test “An obsolete article is dated and flagged, not left as valid”. Measure SEO and performance regressions, document the rollback.
9. **Native validation:** `php tools/validate.php <dossier> --json`, `php tests/run.php` and `php tools/measure.php --check` on an official checkout for every package produced. For a part not supported by the core, provide a gap note and a blocking test, never a fictitious pass.

## Mandatory deliverables
- Mini-specification: goal, users, flows, states, data, measurements.
- Permissions and cache matrix: route, method, session, visibility, indexing.
- Validated `extension.json`/`extension.php` package or theme package, only if a native block or setting is not enough.
- Tests for the positive cases and the refusals, a deactivation procedure that preserves the data, a compatibility note.

## Acceptance criteria
- Solve three typical problems using the documentation alone.
- An obsolete article is dated and flagged, not left as valid.
- Nothing is published, activated or put into production without an authorised person; no score, ranking or citation by an AI is promised.
- The parts not supported by Éclair 2.0 are explicitly flagged as **not deliverable to production**.

**Maturity status of this skill:** `native-v2-workflow`. See `references/acceptance.md` for reproducible test cases.
