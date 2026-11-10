# Validation plan — Internal linking

## Data model
Source page, target page, anchor, orphan pages.

## Expected implementation
Map the links, identify orphan pages, add useful links with descriptive anchors.

## Tests to plan
1. Nominal: Check that every important page receives at least one internal link.
2. Refusal check: No internal link points to a redirect or an error.
3. Invariant: No link is added automatically without reviewing the context.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
