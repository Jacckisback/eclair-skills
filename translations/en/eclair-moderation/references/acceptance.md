# Validation plan — Moderation and reports

## Data model
Report, reason, targeted item, decision, moderator, audit.

## Expected implementation
Plan a processing queue, abusive reports, thresholds/quotas, rollback and reasons; log decisions and restrict powers by role.

## Tests to plan
1. Nominal: Test moderator without global permission, suspended user and appeal.
2. Refusal check: A moderator of one category cannot see the private reports of another.
3. Invariant: No automatic permanent deletion triggered by a report without review and evidence.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
