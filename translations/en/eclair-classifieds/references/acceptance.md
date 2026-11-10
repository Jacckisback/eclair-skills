# Validation plan — Classified ads

## Data model
Ad, advertiser, category, status, report.

## Expected implementation
Define submission, moderation, lifetime, reporting and putting parties in touch without exposing contact details.

## Tests to plan
1. Nominal: Simulate submission, moderation, expiry and reporting.
2. Refusal check: A rejected or expired ad is no longer accessible.
3. Invariant: No ad published without moderation; contact details never displayed in clear text.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
