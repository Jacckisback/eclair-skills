# Validation plan — Announcement bars

## Data model
Message, link, start and end dates.

## Expected implementation
Render the bar on the server side with validity dates, with no layout shift, removed automatically at expiry.

## Tests to plan
1. Nominal: Display, close and let a bar expire.
2. Refusal check: After the end date, the bar no longer appears on any page.
3. Invariant: No expired announcement remains served by the cache.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
