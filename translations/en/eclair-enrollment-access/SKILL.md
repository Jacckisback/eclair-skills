---
name: eclair-enrollment-access
description: "Link a purchase or approval to an enrollment and its permissions. Use on Éclair CMS 2.x when the user wants to: tie a purchase or validation to an enrolment and its authorisations. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Course enrolments — Éclair CMS 2.x

## Trigger and expected outcome
Use this skill to **tie a purchase or validation to an enrolment and its authorisations**. This feature **requires capabilities that are absent from the 2.0 core**: the skill delivers a design, a safe mock-up and tests, not a production release. This skill is an **agent workflow**, not a working PHP extension nor a guarantee of compliance.

**WordPress equivalent:** LearnDash enrolments, MemberPress Courses. Family: LMS.

## Mandatory diagnosis before any change
1. Read `references/core-map.md` (what the core already does) and `references/native-contract.md`; check the actual CMS version and the capabilities in `GET /<admin>/api/capabilities` (if access is authorised).
2. Read `references/family-contract.md` and `references/acceptance.md`. Never copy the old v0.x pack system or WordPress PHP code into Éclair 2.
3. Identify the data model: **Member, course, enrolment, state, origin, date and revocation**. Document what is public, what is private and where each piece of data comes from.

## Specific procedure
4. **Flow:** Create idempotent enrolment; handle permissions per object; distinguish free/paid enrolment; revoke after refund according to an explicit rule. Describe the states and the errors before writing any code.
5. **Locations:** site-specific code in `site/extensions/<id>/`, appearance in `site/themes/<id>/`, data under `$ctx['data']`, content and settings through the administration or the MCP. Never edit `app/`, `assets/`, `index.php` or the updater.
6. **Current contract:** Course presentation pages can be public GET. Paid courses, progress and assessments require a qualified member identity, object-level access checks and private, non-cacheable writes.
7. **Security invariant:** Never an automatic enrolment on a mere payment provider return URL. Also check server-side permissions, escaping with `e()`, data validation and the absence of any secret or personal data in public HTML or in a shared cache.
8. **Evidence:** write the positive test “Test double purchase, refund, account suspension” and the refusal test “A removed member can no longer access previously authorised lessons”. Measure SEO and performance regressions, document the rollback.
9. **Native validation:** `php tools/validate.php <dossier> --json`, `php tests/run.php` and `php tools/measure.php --check` on an official checkout for every package produced. For a part not supported by the core, provide a gap note and a blocking test, never a fictitious pass.

## Mandatory deliverables
- Mini-specification: goal, users, flows, states, data, measurements.
- Permissions and cache matrix: route, method, session, visibility, indexing.
- Design dossier, a safe GET mock-up if useful, blocking tests and a core change request; **no production package**.
- Tests for the positive cases and the refusals, a deactivation procedure that preserves the data, a compatibility note.

## Acceptance criteria
- Test double purchase, refund, account suspension.
- A removed member can no longer access previously authorised lessons.
- Nothing is published, activated or put into production without an authorised person; no score, ranking or citation by an AI is promised.
- The parts not supported by Éclair 2.0 are explicitly flagged as **not deliverable to production**.

**Maturity status of this skill:** `design-workflow-requires-verified-core-capabilities`. See `references/acceptance.md` for reproducible test cases.
