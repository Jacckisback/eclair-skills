# Validation plan — Content for applications and AI

## Data model
Markdown version, llms.txt, feeds, sitemap.

## Expected implementation
Rely on the native machine-readable outputs, document their format and freshness for the client application.

## Tests to plan
1. Nominal: Read a page in HTML and in Markdown and compare.
2. Refusal check: A draft has no accessible Markdown version.
3. Invariant: No private content is exposed by these outputs.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
