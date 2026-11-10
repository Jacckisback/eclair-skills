---
name: eclair-xml-sitemaps
description: "Check the native sitemap and submit it to search engines. Use on Éclair CMS 2.x when the user wants to: check the native sitemap and declare it to search engines. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# XML sitemap — Éclair CMS 2.x

## Trigger and expected outcome
Use this skill to **check the native sitemap and declare it to search engines**. This feature is **already built into the Éclair 2.0 core**: the skill guides its configuration and verification, without writing an extension. This skill is an **agent workflow**, not a working PHP extension nor a guarantee of compliance.

**WordPress equivalent:** Yoast sitemaps, Google XML Sitemaps. Family: SEO, GEO & migration.

## Mandatory diagnosis before any change
1. Read `references/core-map.md` (what the core already does) and `references/native-contract.md`; check the actual CMS version and the capabilities in `GET /<admin>/api/capabilities` (if access is authorised).
2. Read `references/family-contract.md` and `references/acceptance.md`. Never copy the old v0.x pack system or WordPress PHP code into Éclair 2.
3. Identify the data model: **Sitemap entries, dates, images, languages**. Document what is public, what is private and where each piece of data comes from.

## Specific procedure
4. **Flow:** Check the sitemap produced by the core, declare it in the search engines' tools, monitor coverage errors. Describe the states and the errors before writing any code.
5. **Locations:** site-specific code in `site/extensions/<id>/`, appearance in `site/themes/<id>/`, data under `$ctx['data']`, content and settings through the administration or the MCP. Never edit `app/`, `assets/`, `index.php` or the updater.
6. **Current contract:** The feature exists in the core: configure it through the administration or, as a draft, through the MCP connector. Do not duplicate it in an extension and never modify the core to adapt it; if a need goes beyond what the core offers, report it as a gap.
7. **Security invariant:** The sitemap lists only published and indexable pages. Also check server-side permissions, escaping with `e()`, data validation and the absence of any secret or personal data in public HTML or in a shared cache.
8. **Evidence:** write the positive test “Validate the sitemap and compare it with the number of published pages” and the refusal test “A draft or redirected page does not appear in it”. Measure SEO and performance regressions, document the rollback.
9. **Native validation:** `php tools/validate.php <dossier> --json`, `php tests/run.php` and `php tools/measure.php --check` on an official checkout for every package produced. For a part not supported by the core, provide a gap note and a blocking test, never a fictitious pass.

## Mandatory deliverables
- Mini-specification: goal, users, flows, states, data, measurements.
- Permissions and cache matrix: route, method, session, visibility, indexing.
- Settings and content prepared through the administration or as a draft through the MCP; **no extension** as long as the native features are enough.
- Tests for the positive cases and the refusals, a deactivation procedure that preserves the data, a compatibility note.

## Acceptance criteria
- Validate the sitemap and compare it with the number of published pages.
- A draft or redirected page does not appear in it.
- Nothing is published, activated or put into production without an authorised person; no score, ranking or citation by an AI is promised.
- The parts not supported by Éclair 2.0 are explicitly flagged as **not deliverable to production**.

**Maturity status of this skill:** `core-builtin-configuration-workflow`. See `references/acceptance.md` for reproducible test cases.
