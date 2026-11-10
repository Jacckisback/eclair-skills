# Validation plan — Titles and meta descriptions

## Data model
Title, meta description, target phrase, result preview.

## Expected implementation
Write a unique title and description for each page, use the editor's live score as an aid without treating it as a goal.

## Tests to plan
1. Nominal: Check uniqueness and length on all pages.
2. Refusal check: Two published pages do not have the same title.
3. Invariant: No promise of position; no keyword stuffing.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
