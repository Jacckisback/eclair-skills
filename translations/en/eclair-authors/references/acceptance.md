# Validation plan — Authors and bylines

## Data model
Author, biography, job title, links, bylined content.

## Expected implementation
Complete the real profiles, link each post to its author, check the author page and the structured data produced by the core.

## Tests to plan
1. Nominal: Fill in a profile and check the byline, author page and markup.
2. Refusal check: An account that is disabled or has no published content exposes no author page.
3. Invariant: Never invent an author, a qualification or experience.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
