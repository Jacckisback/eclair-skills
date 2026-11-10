# Validation plan — LMS architecture

## Data model
Courses, sections, lessons, prerequisites, enrolments, progress, permissions and possible sales.

## Expected implementation
Define public catalogues vs private lessons; choose transactional progress storage; tie access to the validated member identity; compose independent modules.

## Tests to plan
1. Nominal: Test student, teacher, administrator and visitor.
2. Refusal check: A student enrolled in one course cannot read the private content of another course.
3. Invariant: No promise of private access through a mere secret URL or a hidden block.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
