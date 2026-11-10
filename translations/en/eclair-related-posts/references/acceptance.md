# Validation plan — Related content

## Data model
Content, category, shared words, computed list of links.

## Expected implementation
Compute the associations on publication or with a task, render them with a cacheable static block, limit to a few links.

## Tests to plan
1. Nominal: Check the links offered on several posts from different categories.
2. Refusal check: A deleted post is no longer offered after regeneration.
3. Invariant: No association points to unpublished content.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
