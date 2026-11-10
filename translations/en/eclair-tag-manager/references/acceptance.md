# Validation plan — Tag manager

## Data model
Container, tags, triggers, consent.

## Expected implementation
List the tags that are really necessary, look for a server-side alternative, document the blocking by the native content policy.

## Tests to plan
1. Nominal: Draw up the inventory of tags and their alternative.
2. Refusal check: An unjustified tag is not added.
3. Invariant: No container allowing arbitrary code to be injected without review.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
