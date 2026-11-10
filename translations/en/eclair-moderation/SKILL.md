---
name: eclair-moderation
description: "Build removal, reporting and appeal tools. Use on Éclair CMS 2.x when the user wants to: build removal, reporting and appeal tools. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Moderation and reports — Éclair CMS 2.x

## Trigger and expected outcome
Use this skill to **build removal, reporting and appeal tools**. This feature **requires capabilities that are absent from the 2.0 core**: the skill delivers a design, a safe mock-up and tests, not a production release. This skill is an **agent workflow**, not a working PHP extension nor a guarantee of compliance.

**WordPress equivalent:** bbPress and BuddyPress moderation tools. Family: Forum & community.

## Mandatory diagnosis before any change
1. Read `references/core-map.md` (what the core already does) and `references/native-contract.md`; check the actual CMS version and the capabilities in `GET /<admin>/api/capabilities` (if access is authorised).
2. Read `references/family-contract.md` and `references/acceptance.md`. Never copy the old v0.x pack system or WordPress PHP code into Éclair 2.
3. Identify the data model: **Report, reason, targeted item, decision, moderator, audit**. Document what is public, what is private and where each piece of data comes from.

## Specific procedure
4. **Flow:** Plan a processing queue, abusive reports, thresholds/quotas, rollback and reasons; log decisions and restrict powers by role. Describe the states and the errors before writing any code.
5. **Locations:** site-specific code in `site/extensions/<id>/`, appearance in `site/themes/<id>/`, data under `$ctx['data']`, content and settings through the administration or the MCP. Never edit `app/`, `assets/`, `index.php` or the updater.
6. **Current contract:** Public categories and lists can be GET; posts, reports, private profiles and moderation require an identity and safe write routes, anti-spam and suitable storage.
7. **Security invariant:** No automatic permanent deletion triggered by a report without review and evidence. Also check server-side permissions, escaping with `e()`, data validation and the absence of any secret or personal data in public HTML or in a shared cache.
8. **Evidence:** write the positive test “Test moderator without global permission, suspended user and appeal” and the refusal test “A moderator of one category cannot see the private reports of another”. Measure SEO and performance regressions, document the rollback.
9. **Native validation:** `php tools/validate.php <dossier> --json`, `php tests/run.php` and `php tools/measure.php --check` on an official checkout for every package produced. For a part not supported by the core, provide a gap note and a blocking test, never a fictitious pass.

## Mandatory deliverables
- Mini-specification: goal, users, flows, states, data, measurements.
- Permissions and cache matrix: route, method, session, visibility, indexing.
- Design dossier, a safe GET mock-up if useful, blocking tests and a core change request; **no production package**.
- Tests for the positive cases and the refusals, a deactivation procedure that preserves the data, a compatibility note.

## Acceptance criteria
- Test moderator without global permission, suspended user and appeal.
- A moderator of one category cannot see the private reports of another.
- Nothing is published, activated or put into production without an authorised person; no score, ranking or citation by an AI is promised.
- The parts not supported by Éclair 2.0 are explicitly flagged as **not deliverable to production**.

**Maturity status of this skill:** `design-workflow-requires-verified-core-capabilities`. See `references/acceptance.md` for reproducible test cases.
