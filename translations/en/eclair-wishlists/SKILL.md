---
name: eclair-wishlists
description: "Design favourites lists for visitors. Use on Éclair CMS 2.x when the user wants to: design lists of favourites for visitors. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Wishlists — Éclair CMS 2.x

## Trigger and expected outcome
Use this skill to **design lists of favourites for visitors**. This feature **requires capabilities that are absent from the 2.0 core**: the skill delivers a design, a safe mock-up and tests, not a production release. This skill is an **agent workflow**, not a working PHP extension nor a guarantee of compliance.

**WordPress equivalent:** YITH WooCommerce Wishlist. Family: Commerce Pro.

## Mandatory diagnosis before any change
1. Read `references/core-map.md` (what the core already does) and `references/native-contract.md`; check the actual CMS version and the capabilities in `GET /<admin>/api/capabilities` (if access is authorised).
2. Read `references/family-contract.md` and `references/acceptance.md`. Never copy the old v0.x pack system or WordPress PHP code into Éclair 2.
3. Identify the data model: **List, product, owner**. Document what is public, what is private and where each piece of data comes from.

## Specific procedure
4. **Flow:** Start with storage in the browser, without an account; design the account-based version for later. Describe the states and the errors before writing any code.
5. **Locations:** site-specific code in `site/extensions/<id>/`, appearance in `site/themes/<id>/`, data under `$ctx['data']`, content and settings through the administration or the MCP. Never edit `app/`, `assets/`, `index.php` or the updater.
6. **Current contract:** This feature requires visitor writes, public accounts, transactions or signed events that `eclair-extension/1` does not provide in 2.0. Deliver the design, a safe GET mock-up and blocking tests; never announce a production release.
7. **Security invariant:** No list is shared with or visible to a third party without action by its owner. Also check server-side permissions, escaping with `e()`, data validation and the absence of any secret or personal data in public HTML or in a shared cache.
8. **Evidence:** write the positive test “Add, remove and retrieve favourites” and the refusal test “A deleted product disappears cleanly from the lists”. Measure SEO and performance regressions, document the rollback.
9. **Native validation:** `php tools/validate.php <dossier> --json`, `php tests/run.php` and `php tools/measure.php --check` on an official checkout for every package produced. For a part not supported by the core, provide a gap note and a blocking test, never a fictitious pass.

## Mandatory deliverables
- Mini-specification: goal, users, flows, states, data, measurements.
- Permissions and cache matrix: route, method, session, visibility, indexing.
- Design dossier, a safe GET mock-up if useful, blocking tests and a core change request; **no production package**.
- Tests for the positive cases and the refusals, a deactivation procedure that preserves the data, a compatibility note.

## Acceptance criteria
- Add, remove and retrieve favourites.
- A deleted product disappears cleanly from the lists.
- Nothing is published, activated or put into production without an authorised person; no score, ranking or citation by an AI is promised.
- The parts not supported by Éclair 2.0 are explicitly flagged as **not deliverable to production**.

**Maturity status of this skill:** `design-workflow-requires-verified-core-capabilities`. See `references/acceptance.md` for reproducible test cases.
