# Validation plan — Course enrolments

## Data model
Member, course, enrolment, state, origin, date and revocation.

## Expected implementation
Create idempotent enrolment; handle permissions per object; distinguish free/paid enrolment; revoke after refund according to an explicit rule.

## Tests to plan
1. Nominal: Test double purchase, refund, account suspension.
2. Refusal check: A removed member can no longer access previously authorised lessons.
3. Invariant: Never an automatic enrolment on a mere payment provider return URL.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
