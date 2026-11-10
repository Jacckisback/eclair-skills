# Validation plan — Job listings

## Data model
Job listing, company, status, closing date, application and attachments.

## Expected implementation
Build public filters, automatic expiry, secure forms and a retention cycle for applications.

## Tests to plan
1. Nominal: Test expired advert, spam and applicant export.
2. Refusal check: A recruiter cannot read an application intended for another company.
3. Invariant: CVs and attachments are never placed in a web-accessible directory.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
