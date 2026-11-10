# Validation plan — RSS feeds

## Data model
Feed, items, date, full content or excerpt.

## Expected implementation
Check the feed produced by the core, declare it in the pages, offer it to subscribers and aggregators.

## Tests to plan
1. Nominal: Validate the feed with a reader and a validator.
2. Refusal check: Unpublished content disappears from the feed on regeneration.
3. Invariant: The feed contains only published content.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
