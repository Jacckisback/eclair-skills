# Validation plan — Change of host or domain

## Data model
Backup, new hosting, DNS, domain redirects.

## Expected implementation
Back up, restore at the new host, check, switch the DNS, redirect the old domain page by page.

## Tests to plan
1. Nominal: Rehearse the move on a test domain.
2. Refusal check: No old address responds with a 404 after the switch.
3. Invariant: The site's secrets never travel by email or messaging.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
