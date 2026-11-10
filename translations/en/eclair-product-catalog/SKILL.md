---
name: eclair-product-catalog
description: "Build a fast, indexable public product catalogue. Use on Éclair CMS 2.x when the user wants to: build a fast, indexable public catalogue. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Product catalogue — Éclair CMS 2.x

## Trigger and expected outcome
Use this skill to **build a fast, indexable public catalogue**. This feature is **already built into the Éclair 2.0 core**: the skill guides its configuration and verification, without writing an extension. This skill is an **agent workflow**, not a working PHP extension nor a guarantee of compliance.

**WordPress equivalent:** WooCommerce catalogue. Family: Commerce Pro.

## Mandatory diagnosis before any change
1. Read `references/core-map.md` (what the core already does) and `references/native-contract.md`; check the actual CMS version and the capabilities in `GET /<admin>/api/capabilities` (if access is authorised).
2. Read `references/family-contract.md` and `references/acceptance.md`. Never copy the old v0.x pack system or WordPress PHP code into Éclair 2.
3. Identify the data model: **Product, SKU, slug, title, description, display price, media, availability and category**. Document what is public, what is private and where each piece of data comes from.

## Specific procedure
4. **Flow:** First prototype a cacheable public GET page; produce a product schema and its index; keep source titles and descriptions; define pagination and canonical; preserve slugs across edits. Describe the states and the errors before writing any code.
5. **Locations:** site-specific code in `site/extensions/<id>/`, appearance in `site/themes/<id>/`, data under `$ctx['data']`, content and settings through the administration or the MCP. Never edit `app/`, `assets/`, `index.php` or the updater.
6. **Current contract:** The core already provides a lightweight shop (product pages, variants, categories, payment links from a provider, merchant feed): use it first, without duplicating it. Beyond that, basket, orders and payments need public POSTs, reliable transactional storage, authenticated webhooks and idempotency; official Éclair 2.0 does not provide all of that. PR #19 is still a draft: never use an unmerged POST route as proof of compatibility.
7. **Security invariant:** The displayed price is never taken as the authoritative source for a future order. Also check server-side permissions, escaping with `e()`, data validation and the absence of any secret or personal data in public HTML or in a shared cache.
8. **Evidence:** write the positive test “Test categories, empty lists, canonical URL, search and soft deletion” and the refusal test “A deleted or private product must not remain in the catalogue or in an old cache”. Measure SEO and performance regressions, document the rollback.
9. **Native validation:** `php tools/validate.php <dossier> --json`, `php tests/run.php` and `php tools/measure.php --check` on an official checkout for every package produced. For a part not supported by the core, provide a gap note and a blocking test, never a fictitious pass.

## Mandatory deliverables
- Mini-specification: goal, users, flows, states, data, measurements.
- Permissions and cache matrix: route, method, session, visibility, indexing.
- Settings and content prepared through the administration or as a draft through the MCP; **no extension** as long as the native features are enough.
- Tests for the positive cases and the refusals, a deactivation procedure that preserves the data, a compatibility note.

## Acceptance criteria
- Test categories, empty lists, canonical URL, search and soft deletion.
- A deleted or private product must not remain in the catalogue or in an old cache.
- Nothing is published, activated or put into production without an authorised person; no score, ranking or citation by an AI is promised.
- The parts not supported by Éclair 2.0 are explicitly flagged as **not deliverable to production**.

**Maturity status of this skill:** `core-builtin-configuration-workflow`. See `references/acceptance.md` for reproducible test cases.
