# Validation plan — Progressive unlocking

## Data model
Lesson, unlocking rule, date or condition, enrolled member.

## Expected implementation
Describe the rules (date, delay after enrolment, previous lesson), apply them server-side on every request.

## Tests to plan
1. Nominal: Simulate the passage of time and the validation of a lesson.
2. Refusal check: A guessed locked-lesson address does not return its content.
3. Invariant: A locked lesson is never sent to the browser, even hidden.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
