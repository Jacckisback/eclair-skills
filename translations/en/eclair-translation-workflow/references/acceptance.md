# Validation plan — Translation workflow

## Data model
Source content, target version, translator, state, update date.

## Expected implementation
Keep a table of the content to translate, produce the translations as drafts, have them reviewed by a speaker of the language, flag outdated versions.

## Tests to plan
1. Nominal: Translate a page, have it reviewed, publish, then modify the source and check the flag.
2. Refusal check: An unreviewed translation remains a draft.
3. Invariant: No legal or medical translation published without qualified validation.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
