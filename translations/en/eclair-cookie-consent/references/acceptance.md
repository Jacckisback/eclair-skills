# Validation plan — Cookies and consent

## Data model
Tracker, purpose, consent, proof.

## Expected implementation
Inventory the actual trackers; without a tracker, no banner; otherwise prior consent, refusal as simple as acceptance and an information page.

## Tests to plan
1. Nominal: Inspect cookies and requests before and after the choice.
2. Refusal check: After a refusal, no third-party tracker is loaded.
3. Invariant: No tracker subject to consent is set before acceptance.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
