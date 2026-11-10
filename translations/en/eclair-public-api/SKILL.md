---
name: eclair-public-api
description: "Expose public site data as JSON. Use on Éclair CMS 2.x when the user wants to: expose public site data as JSON. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Read-only public API — Éclair CMS 2.x

## Trigger and expected outcome
Use this skill to **expose public site data as JSON**. The **public read-only part is achievable today**; writes by visitors require more than the current contract. This skill is an **agent workflow**, not a working PHP extension nor a guarantee of compliance.

**WordPress equivalent:** WordPress REST API. Family: Development & tools.

## Mandatory diagnosis before any change
1. Read `references/core-map.md` (what the core already does) and `references/native-contract.md`; check the actual CMS version and the capabilities in `GET /<admin>/api/capabilities` (if access is authorised).
2. Read `references/family-contract.md` and `references/acceptance.md`. Never copy the old v0.x pack system or WordPress PHP code into Éclair 2.
3. Identify the data model: **Resource, public fields, pagination, version**. Document what is public, what is private and where each piece of data comes from.

## Specific procedure
4. **Flow:** Declare cacheable GET routes that return bounded, versioned JSON; document that writing is not open. Describe the states and the errors before writing any code.
5. **Locations:** site-specific code in `site/extensions/<id>/`, appearance in `site/themes/<id>/`, data under `$ctx['data']`, content and settings through the administration or the MCP. Never edit `app/`, `assets/`, `index.php` or the updater.
6. **Current contract:** Public reading (GET, cacheable) is achievable today. Any write by a visitor requires a public POST route that the 2.0 core does not open to extensions (PR #19 in draft, not merged): do not simulate it.
7. **Security invariant:** Only content that is already public is exposed; no sensitive internal identifier. Also check server-side permissions, escaping with `e()`, data validation and the absence of any secret or personal data in public HTML or in a shared cache.
8. **Evidence:** write the positive test “Read list and detail, pagination and empty case” and the refusal test “Unpublished content is returned by no route”. Measure SEO and performance regressions, document the rollback.
9. **Native validation:** `php tools/validate.php <dossier> --json`, `php tests/run.php` and `php tools/measure.php --check` on an official checkout for every package produced. For a part not supported by the core, provide a gap note and a blocking test, never a fictitious pass.

## Mandatory deliverables
- Mini-specification: goal, users, flows, states, data, measurements.
- Permissions and cache matrix: route, method, session, visibility, indexing.
- Validated read-only package (GET routes), and a written plan for the write part, clearly marked as not delivered.
- Tests for the positive cases and the refusals, a deactivation procedure that preserves the data, a compatibility note.

## Acceptance criteria
- Read list and detail, pagination and empty case.
- Unpublished content is returned by no route.
- Nothing is published, activated or put into production without an authorised person; no score, ranking or citation by an AI is promised.
- The parts not supported by Éclair 2.0 are explicitly flagged as **not deliverable to production**.

**Maturity status of this skill:** `public-read-only-prototype-possible`. See `references/acceptance.md` for reproducible test cases.
