---
name: eclair-navigation-menus
description: "Build clear header and footer navigation menus. Use on Éclair CMS 2.x when the user wants to: build clear menus for the header and the footer. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Navigation menus — Éclair CMS 2.x

## Trigger and expected outcome
Use this skill to **build clear menus for the header and the footer**. This feature is **already built into the Éclair 2.0 core**: the skill guides its configuration and verification, without writing an extension. This skill is an **agent workflow**, not a working PHP extension nor a guarantee of compliance.

**WordPress equivalent:** Native WordPress menus. Family: Content & publishing.

## Mandatory diagnosis before any change
1. Read `references/core-map.md` (what the core already does) and `references/native-contract.md`; check the actual CMS version and the capabilities in `GET /<admin>/api/capabilities` (if access is authorised).
2. Read `references/family-contract.md` and `references/acceptance.md`. Never copy the old v0.x pack system or WordPress PHP code into Éclair 2.
3. Identify the data model: **Menu, entry, order, target, location**. Document what is public, what is private and where each piece of data comes from.

## Specific procedure
4. **Flow:** Limit the main menu to the essential journeys, put the rest in the footer, test with keyboard and on mobile. Describe the states and the errors before writing any code.
5. **Locations:** site-specific code in `site/extensions/<id>/`, appearance in `site/themes/<id>/`, data under `$ctx['data']`, content and settings through the administration or the MCP. Never edit `app/`, `assets/`, `index.php` or the updater.
6. **Current contract:** The feature exists in the core: configure it through the administration or, as a draft, through the MCP connector. Do not duplicate it in an extension and never modify the core to adapt it; if a need goes beyond what the core offers, report it as a gap.
7. **Security invariant:** No menu link points to a draft or to an unintended external address. Also check server-side permissions, escaping with `e()`, data validation and the absence of any secret or personal data in public HTML or in a shared cache.
8. **Evidence:** write the positive test “Compose the menus and go through them with the keyboard and on mobile” and the refusal test “An unpublished page disappears from the menu or is flagged, never served as a 404 from the navigation”. Measure SEO and performance regressions, document the rollback.
9. **Native validation:** `php tools/validate.php <dossier> --json`, `php tests/run.php` and `php tools/measure.php --check` on an official checkout for every package produced. For a part not supported by the core, provide a gap note and a blocking test, never a fictitious pass.

## Mandatory deliverables
- Mini-specification: goal, users, flows, states, data, measurements.
- Permissions and cache matrix: route, method, session, visibility, indexing.
- Settings and content prepared through the administration or as a draft through the MCP; **no extension** as long as the native features are enough.
- Tests for the positive cases and the refusals, a deactivation procedure that preserves the data, a compatibility note.

## Acceptance criteria
- Compose the menus and go through them with the keyboard and on mobile.
- An unpublished page disappears from the menu or is flagged, never served as a 404 from the navigation.
- Nothing is published, activated or put into production without an authorised person; no score, ranking or citation by an AI is promised.
- The parts not supported by Éclair 2.0 are explicitly flagged as **not deliverable to production**.

**Maturity status of this skill:** `core-builtin-configuration-workflow`. See `references/acceptance.md` for reproducible test cases.
