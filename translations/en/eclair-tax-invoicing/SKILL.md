---
name: eclair-tax-invoicing
description: "Prepare VAT and invoicing hooks adapted to each jurisdiction (no universal rate). Use on Éclair CMS 2.x when the user wants to: build the tax connection points suited to the jurisdiction. Agent workflow with native-contract check, security invariant and acceptance tests; not a PHP plugin."
---

# VAT and invoicing — Éclair CMS 2.x

## Trigger and expected outcome
Use this skill to **build the tax connection points suited to the jurisdiction**. This feature **requires capabilities that are absent from the 2.0 core**: the skill delivers a design, a safe mock-up and tests, not a production release. This skill is an **agent workflow**, not a working PHP extension nor a guarantee of compliance.

**WordPress equivalent:** WooCommerce taxes, PDF invoice plugins. Family: Commerce Pro.

## Mandatory diagnosis before any change
1. Read `references/core-map.md` (what the core already does) and `references/native-contract.md`; check the actual CMS version and the capabilities in `GET /<admin>/api/capabilities` (if access is authorised).
2. Read `references/family-contract.md` and `references/acceptance.md`. Never copy the old v0.x pack system or WordPress PHP code into Éclair 2.
3. Identify the data model: **Country of sale and delivery, tax location, rate in force, invoice, credit note, sequence**. Document what is public, what is private and where each piece of data comes from.

## Specific procedure
4. **Flow:** List jurisdictions and customer types; consult up-to-date rules and accounting advice; freeze taxable base/rate at the time of the order; prepare exports of invoices and credit notes. Describe the states and the errors before writing any code.
5. **Locations:** site-specific code in `site/extensions/<id>/`, appearance in `site/themes/<id>/`, data under `$ctx['data']`, content and settings through the administration or the MCP. Never edit `app/`, `assets/`, `index.php` or the updater.
6. **Current contract:** The core already provides a lightweight shop (product pages, variants, categories, payment links from a provider, merchant feed): use it first, without duplicating it. Beyond that, basket, orders and payments need public POSTs, reliable transactional storage, authenticated webhooks and idempotency; official Éclair 2.0 does not provide all of that. PR #19 is still a draft: never use an unmerged POST route as proof of compatibility.
7. **Security invariant:** Never apply a universal VAT rate or claim to ensure tax compliance without local validation. Also check server-side permissions, escaping with `e()`, data validation and the absence of any secret or personal data in public HTML or in a shared cache.
8. **Evidence:** write the positive test “Test domestic sale, cross-border sale, refund and rate change” and the refusal test “An invoice issued then cancelled must not be erased or silently renumbered”. Measure SEO and performance regressions, document the rollback.
9. **Native validation:** `php tools/validate.php <dossier> --json`, `php tests/run.php` and `php tools/measure.php --check` on an official checkout for every package produced. For a part not supported by the core, provide a gap note and a blocking test, never a fictitious pass.

## Mandatory deliverables
- Mini-specification: goal, users, flows, states, data, measurements.
- Permissions and cache matrix: route, method, session, visibility, indexing.
- Design dossier, a safe GET mock-up if useful, blocking tests and a core change request; **no production package**.
- Tests for the positive cases and the refusals, a deactivation procedure that preserves the data, a compatibility note.

## Acceptance criteria
- Test domestic sale, cross-border sale, refund and rate change.
- An invoice issued then cancelled must not be erased or silently renumbered.
- Nothing is published, activated or put into production without an authorised person; no score, ranking or citation by an AI is promised.
- The parts not supported by Éclair 2.0 are explicitly flagged as **not deliverable to production**.

**Maturity status of this skill:** `design-workflow-requires-verified-core-capabilities`. See `references/acceptance.md` for reproducible test cases.
