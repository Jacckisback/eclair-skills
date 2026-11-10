# Validation plan — Share buttons

## Data model
Network, sharing address, label.

## Expected implementation
Use simple sharing links and the browser's share API as a progressive enhancement.

## Tests to plan
1. Nominal: Share a page from mobile and desktop.
2. Refusal check: No third-party request before the click.
3. Invariant: No button loads a third-party script or tracker.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
