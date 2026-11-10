---
name: eclair-performance-ux
description: "Measure and reduce page weight and layout instability. Use on Éclair CMS 2.x when the user wants to: measure and reduce page weight and instability. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# Performance UX — Éclair CMS 2.x

## Trigger and expected outcome
Use this skill to **measure and reduce page weight and instability**. This feature is **achievable today** with the native contract (theme, blocks, GET routes, administration pages, tasks). This skill is an **agent workflow**, not a working PHP extension nor a guarantee of compliance.

**WordPress equivalent:** WP Rocket, Perfmatters. Family: Design & UX.

## Mandatory diagnosis before any change
1. Read `references/core-map.md` (what the core already does) and `references/native-contract.md`; check the actual CMS version and the capabilities in `GET /<admin>/api/capabilities` (if access is authorised).
2. Read `references/family-contract.md` and `references/acceptance.md`. Never copy the old v0.x pack system or WordPress PHP code into Éclair 2.
3. Identify the data model: **LCP, CLS, INP, asset weight, CSS, JS, cache and fonts**. Document what is public, what is private and where each piece of data comes from.

## Specific procedure
4. **Flow:** Measure before/after via tools/measure.php --check, Chrome Lighthouse and a slow network, optimise images and scripts. Describe the states and the errors before writing any code.
5. **Locations:** site-specific code in `site/extensions/<id>/`, appearance in `site/themes/<id>/`, data under `$ctx['data']`, content and settings through the administration or the MCP. Never edit `app/`, `assets/`, `index.php` or the updater.
6. **Current contract:** Éclair v2 exposes themes under site/themes and declarative extension blocks. Do not modify app/, index.php, the CSP or cache generation; validate themes with tools/validate.php.
7. **Security invariant:** Do not degrade the PHP cache path or disable CSP for the sake of convenience. Also check server-side permissions, escaping with `e()`, data validation and the absence of any secret or personal data in public HTML or in a shared cache.
8. **Evidence:** write the positive test “Test the public site without an extension, with an extension and on mobile” and the refusal test “A claimed improvement is accompanied by reproducible before/after measurements”. Measure SEO and performance regressions, document the rollback.
9. **Native validation:** `php tools/validate.php <dossier> --json`, `php tests/run.php` and `php tools/measure.php --check` on an official checkout for every package produced. For a part not supported by the core, provide a gap note and a blocking test, never a fictitious pass.

## Mandatory deliverables
- Mini-specification: goal, users, flows, states, data, measurements.
- Permissions and cache matrix: route, method, session, visibility, indexing.
- Validated `extension.json`/`extension.php` package or theme package, only if a native block or setting is not enough.
- Tests for the positive cases and the refusals, a deactivation procedure that preserves the data, a compatibility note.

## Acceptance criteria
- Test the public site without an extension, with an extension and on mobile.
- A claimed improvement is accompanied by reproducible before/after measurements.
- Nothing is published, activated or put into production without an authorised person; no score, ranking or citation by an AI is promised.
- The parts not supported by Éclair 2.0 are explicitly flagged as **not deliverable to production**.

**Maturity status of this skill:** `native-v2-workflow`. See `references/acceptance.md` for reproducible test cases.
