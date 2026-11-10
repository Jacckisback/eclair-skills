# Validation plan — E-mail campaigns

## Data model
List, segment, campaign, mailing, unsubscription.

## Expected implementation
Entrust sending to a specialised service, prepare the content from the site, define segments, frequency and unsubscription.

## Tests to plan
1. Nominal: Send a test campaign to an internal list.
2. Refusal check: An unsubscribed address no longer receives anything.
3. Invariant: Every e-mail contains a working unsubscribe link; no purchased list.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
