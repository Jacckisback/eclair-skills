# Validation plan — Security headers

## Data model
HTTP headers, Content-Security-Policy, HTTPS.

## Expected implementation
Record the headers served, check HTTPS everywhere, test the web server rules shipped with the core.

## Tests to plan
1. Nominal: Analyse the headers of a public page and of the administration.
2. Refusal check: A sensitive file or data file is never served by the web server.
3. Invariant: No protective header is removed or relaxed.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
