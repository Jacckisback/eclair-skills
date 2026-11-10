# Validation plan — Portfolio and projects

## Data model
Project, client, context, result, images.

## Expected implementation
Write up each project as problem, solution, result, with lightweight images and the client's agreement.

## Tests to plan
1. Nominal: Browse list and detail on mobile.
2. Refusal check: A project without recorded agreement remains a draft.
3. Invariant: No client, figure or result published without agreement.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
