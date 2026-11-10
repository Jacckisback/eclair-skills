# Validation plan — Site pages

## Data model
Page, address, blocks, parent page, status, menu entry.

## Expected implementation
List the pages needed, fix the addresses before writing, compose each page in blocks and link the pages to one another.

## Tests to plan
1. Nominal: Create the complete tree structure and check every address, the menu and the breadcrumb trail.
2. Refusal check: A renamed page responds with a single 301 redirect, never with a 404 error.
3. Invariant: Never change the address of a published page without a verified redirect.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
