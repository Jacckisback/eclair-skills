# Validation plan — Updates and rollback

## Data model
Installed version, announced version, signature, rollback point.

## Expected implementation
Back up, read the release notes, run the one-click update, check the site, know how to return to the previous version.

## Tests to plan
1. Nominal: Update a copy of the site, then roll back.
2. Refusal check: An update announcement not signed by the maintainer is refused.
3. Invariant: Never install an archive whose signature is not verified by the core.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
