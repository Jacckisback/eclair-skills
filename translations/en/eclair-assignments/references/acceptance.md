# Validation plan — Assignments and marking

## Data model
Assignment, submission, mark, comment, learner.

## Expected implementation
Define submission, deadlines, marking and feedback; restrict each submission to its author and the marker.

## Tests to plan
1. Nominal: Simulate submission, marking and viewing of the mark.
2. Refusal check: A learner cannot access another learner's submission.
3. Invariant: A submission is readable only by its author and the designated markers.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
