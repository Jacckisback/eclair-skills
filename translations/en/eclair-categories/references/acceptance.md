# Validation plan — Categories

## Data model
Category, address, description, attached content.

## Expected implementation
Define a small number of stable categories, write their descriptions, attach each piece of content to a main category.

## Tests to plan
1. Nominal: Create the categories, attach the content and check the category pages and their pagination.
2. Refusal check: A category with no published content is not offered in the navigation.
3. Invariant: Do not create empty or duplicate categories that dilute the site.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
