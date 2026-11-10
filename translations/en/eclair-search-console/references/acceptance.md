# Validation plan — Search Console

## Data model
Property, verification method, submitted sitemap, reports.

## Expected implementation
Verify the domain by DNS record, submit the native sitemap, read coverage and queries every month.

## Tests to plan
1. Nominal: Verify the property and that the sitemap has been taken into account.
2. Refusal check: A coverage error is explained, not hidden.
3. Invariant: No owner access given to a third party without the client's agreement.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
