# Validation plan — Advertising

## Data model
Placement, consent, ads.txt file.

## Expected implementation
Use the native Advertising page, limit the placements, check consent, label and impact on speed.

## Tests to plan
1. Nominal: Measure the page with and without advertising and check consent.
2. Refusal check: Pages other than posts display no advertising.
3. Invariant: No advertising loaded before the required consent.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
