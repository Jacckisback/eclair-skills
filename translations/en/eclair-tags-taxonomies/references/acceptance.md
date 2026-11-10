# Validation plan — Tags and taxonomies

## Data model
Term, taxonomy type, linked content, archive address.

## Expected implementation
Inventory the existing taxonomies, merge those that duplicate the categories, propose GET grouping pages for the rest and redirect the old archives.

## Tests to plan
1. Nominal: Convert a set of tags into categories or grouping pages and check the redirects.
2. Refusal check: A deleted old tag archive redirects to the closest page, with no chain.
3. Invariant: Do not generate hundreds of thin indexable archives.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
