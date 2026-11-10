# Validation plan — PDF documents

## Data model
Document, title, summary, presentation page, file.

## Expected implementation
Create one HTML presentation page per document with a summary, a download link and an accessible alternative.

## Tests to plan
1. Nominal: Check the link, weight, document title and presentation page.
2. Refusal check: A removed PDF returns a clean response and not a broken link in the pages.
3. Invariant: No PDF containing personal data is published without consent.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
