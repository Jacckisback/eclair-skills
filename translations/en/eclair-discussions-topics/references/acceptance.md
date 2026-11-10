# Validation plan — Topics and replies

## Data model
Topic, reply, version, author, timestamp, pinned, closed, deleted.

## Expected implementation
Define reply parentage, pagination, edit history, mentions and permalinks; handle idempotent submissions.

## Tests to plan
1. Nominal: Test concurrent replies, deleted message and closed topic.
2. Refusal check: A member cannot edit or delete another member's reply without an explicit permission.
3. Invariant: Escape Markdown/HTML and check the permission to edit for every post.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
