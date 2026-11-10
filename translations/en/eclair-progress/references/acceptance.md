# Validation plan — Progress tracking

## Data model
Enrolment, unit, completion state, attempt, duration, revision.

## Expected implementation
Define completion rules; record progress under access control; version units; aggregate progress calculated from authorised states.

## Tests to plan
1. Nominal: Test session resumption, two devices, removed lesson.
2. Refusal check: Two devices must not downgrade progress already validated.
3. Invariant: Progress records are individual, non-cacheable data; never accept an arbitrary member identifier.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
