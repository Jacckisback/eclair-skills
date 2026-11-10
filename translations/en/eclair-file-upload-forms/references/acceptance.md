# Validation plan — Forms with attachments

## Data model
Uploaded file, type, size, owner, retention period.

## Expected implementation
Define accepted types and sizes, storage outside the public root, scanning and automatic deletion.

## Tests to plan
1. Nominal: Upload a valid file and find it on the admin side.
2. Refusal check: A file that is too heavy, disguised or executable is rejected.
3. Invariant: No uploaded file is executable or served directly to the public.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
