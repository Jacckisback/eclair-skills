---
name: eclair-structured-data
description: "Add or check schema.org data consistent with the visible content. Use on Éclair CMS 2.x when the user wants to: add or check schema.org that is consistent with the content. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Structured data — Éclair CMS 2.x

## Trigger and expected outcome
Use this skill to **add or check schema.org that is consistent with the content**. This feature is **partly blocked by the core contract**: the skill delivers what is native and documents the gap. This skill is an **agent workflow**, not a working PHP extension nor a guarantee of compliance.

**WordPress equivalent:** Schema Pro, Rank Math Schema. Family: SEO, GEO & migration.

## Mandatory diagnosis before any change
1. Read `references/core-map.md` (what the core already does) and `references/native-contract.md`; check the actual CMS version and the capabilities in `GET /<admin>/api/capabilities` (if access is authorised).
2. Read `references/family-contract.md` and `references/acceptance.md`. Never copy the old v0.x pack system or WordPress PHP code into Éclair 2.
3. Identify the data model: **WebPage, Article, Product, relevant FAQ, Organization, BreadcrumbList**. Document what is public, what is private and where each piece of data comes from.

## Specific procedure
4. **Flow:** Inspect the native JSON-LD before adding a type; avoid duplication; align each field with the visible data and the search engines' guidelines. Describe the states and the errors before writing any code.
5. **Locations:** site-specific code in `site/extensions/<id>/`, appearance in `site/themes/<id>/`, data under `$ctx['data']`, content and settings through the administration or the MCP. Never edit `app/`, `assets/`, `index.php` or the updater.
6. **Current contract:** Basic SEO/GEO is native. Extensions do not yet have a universal API for injecting JSON-LD; document the contract gap rather than hacking the HTML or scripts.
7. **Security invariant:** Éclair v2 does not yet expose all JSON-LD contributions to extensions; propose an RFC rather than opaque injection. Also check server-side permissions, escaping with `e()`, data validation and the absence of any secret or personal data in public HTML or in a shared cache.
8. **Evidence:** write the positive test “Test valid JSON, canonical, identifiers and displayed content” and the refusal test “No price/review/product that is invented or absent from the page appears in JSON-LD”. Measure SEO and performance regressions, document the rollback.
9. **Native validation:** `php tools/validate.php <dossier> --json`, `php tests/run.php` and `php tools/measure.php --check` on an official checkout for every package produced. For a part not supported by the core, provide a gap note and a blocking test, never a fictitious pass.

## Mandatory deliverables
- Mini-specification: goal, users, flows, states, data, measurements.
- Permissions and cache matrix: route, method, session, visibility, indexing.
- Package or settings for the native part, and a precise gap note for the blocked part.
- Tests for the positive cases and the refusals, a deactivation procedure that preserves the data, a compatibility note.

## Acceptance criteria
- Test valid JSON, canonical, identifiers and displayed content.
- No price/review/product that is invented or absent from the page appears in JSON-LD.
- Nothing is published, activated or put into production without an authorised person; no score, ranking or citation by an AI is promised.
- The parts not supported by Éclair 2.0 are explicitly flagged as **not deliverable to production**.

**Maturity status of this skill:** `partly-blocked-by-core-contract`. See `references/acceptance.md` for reproducible test cases.
