# Validation plan — Professional practice website

## Data model
Service, practitioner, indicative fees, contact request.

## Expected implementation
Present real areas of practice and career backgrounds, comply with the profession's communication rules, offer contact or an appointment.

## Tests to plan
1. Nominal: Have the content reviewed by the professional.
2. Refusal check: An unrecognised specialism is not displayed as a title.
3. Invariant: No promise of results and no statement forbidden by the profession's code of ethics.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
