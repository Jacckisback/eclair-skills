# Validation plan — Comments

## Data model
Comment, author, moderation status, post, date.

## Expected implementation
Define the moderation queue, anti-spam rules, legal notices and cached display; in the meantime, propose an external service or a contact option.

## Tests to plan
1. Nominal: Simulate the submission, moderation, publication and deletion of a comment.
2. Refusal check: A pending or rejected comment never appears in a cached page.
3. Invariant: No comment is displayed without moderation; no e-mail address is made public.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
