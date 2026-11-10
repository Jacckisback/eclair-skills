# Validation plan — VAT and invoicing

## Data model
Country of sale and delivery, tax location, rate in force, invoice, credit note, sequence.

## Expected implementation
List jurisdictions and customer types; consult up-to-date rules and accounting advice; freeze taxable base/rate at the time of the order; prepare exports of invoices and credit notes.

## Tests to plan
1. Nominal: Test domestic sale, cross-border sale, refund and rate change.
2. Refusal check: An invoice issued then cancelled must not be erased or silently renumbered.
3. Invariant: Never apply a universal VAT rate or claim to ensure tax compliance without local validation.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
