# Validation plan — Audio and podcast

## Data model
Episode, audio file, duration, notes, feed.

## Expected implementation
Create one page per episode with a native HTML player, generate the podcast feed in GET and host heavy files off the site if necessary.

## Tests to plan
1. Nominal: Validate the feed with a podcast validator and play an episode on mobile.
2. Refusal check: A draft episode is absent from the feed.
3. Invariant: The feed references only published episodes and public files.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
