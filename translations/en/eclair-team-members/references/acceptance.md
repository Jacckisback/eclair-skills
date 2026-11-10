# Validation plan — Team

## Data model
Person, job title, photo, short biography.

## Expected implementation
Use the native team block with consistent photos and texts provided by the people themselves.

## Tests to plan
1. Nominal: Display the team on mobile with correct alternative texts.
2. Refusal check: A removed person also disappears from the cached pages.
3. Invariant: No photo or information is published without the person's consent.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
