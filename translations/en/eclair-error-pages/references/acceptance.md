# Validation plan — Error pages

## Data model
Error page, useful links, log of addresses not found.

## Expected implementation
Compose a useful 404 page in the site theme, offer the home page and key pages, handle frequent 404s by redirect.

## Tests to plan
1. Nominal: Request a non-existent address and check the 404 status and content.
2. Refusal check: A page not found never responds with a 200 status.
3. Invariant: The error page displays no technical trace.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
