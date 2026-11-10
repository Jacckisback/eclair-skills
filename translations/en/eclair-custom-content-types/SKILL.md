---
name: eclair-custom-content-types
description: "Model business content (projects, listings, events) without core custom post types. Use on Éclair CMS 2.x when the user wants to: model business content (projects, properties, events) without a custom content type in the core. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Custom content types — Éclair CMS 2.x

## Trigger and expected outcome
Use this skill to **model business content (projects, properties, events) without a custom content type in the core**. This feature is **partly blocked by the core contract**: the skill delivers what is native and documents the gap. This skill is an **agent workflow**, not a working PHP extension nor a guarantee of compliance.

**WordPress equivalent:** Custom Post Types (CPT UI, ACF). Family: Content & publishing.

## Mandatory diagnosis before any change
1. Read `references/core-map.md` (what the core already does) and `references/native-contract.md`; check the actual CMS version and the capabilities in `GET /<admin>/api/capabilities` (if access is authorised).
2. Read `references/family-contract.md` and `references/acceptance.md`. Never copy the old v0.x pack system or WordPress PHP code into Éclair 2.
3. Identify the data model: **Business record, fields, list, address, status**. Document what is public, what is private and where each piece of data comes from.

## Specific procedure
4. **Flow:** Choose between pages with dedicated blocks and an extension with its own storage and GET routes, fix the addresses, plan for list and record. Describe the states and the errors before writing any code.
5. **Locations:** site-specific code in `site/extensions/<id>/`, appearance in `site/themes/<id>/`, data under `$ctx['data']`, content and settings through the administration or the MCP. Never edit `app/`, `assets/`, `index.php` or the updater.
6. **Current contract:** One part depends on a hook that is absent from the 2.0 contract (content types, SEO or JSON-LD contribution, per-extension content policy, rendering filter). Deliver the native part and document the gap precisely, without any workaround.
7. **Security invariant:** Never write to the core's content files from an extension. Also check server-side permissions, escaping with `e()`, data validation and the absence of any secret or personal data in public HTML or in a shared cache.
8. **Evidence:** write the positive test “Create a record type through an extension, with list and detail in GET, then validate the package” and the refusal test “An unpublished record is served neither in the list nor at its direct address”. Measure SEO and performance regressions, document the rollback.
9. **Native validation:** `php tools/validate.php <dossier> --json`, `php tests/run.php` and `php tools/measure.php --check` on an official checkout for every package produced. For a part not supported by the core, provide a gap note and a blocking test, never a fictitious pass.

## Mandatory deliverables
- Mini-specification: goal, users, flows, states, data, measurements.
- Permissions and cache matrix: route, method, session, visibility, indexing.
- Package or settings for the native part, and a precise gap note for the blocked part.
- Tests for the positive cases and the refusals, a deactivation procedure that preserves the data, a compatibility note.

## Acceptance criteria
- Create a record type through an extension, with list and detail in GET, then validate the package.
- An unpublished record is served neither in the list nor at its direct address.
- Nothing is published, activated or put into production without an authorised person; no score, ranking or citation by an AI is promised.
- The parts not supported by Éclair 2.0 are explicitly flagged as **not deliverable to production**.

**Maturity status of this skill:** `partly-blocked-by-core-contract`. See `references/acceptance.md` for reproducible test cases.
