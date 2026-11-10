# Validation plan — Property listings

## Data model
Property, transaction, rounded geolocation, floor area, media, price, availability.

## Expected implementation
Version listings, provide bounded filters, handle sold/let status, images and viewing requests.

## Tests to plan
1. Nominal: Test withdrawn listings, private media and filters.
2. Refusal check: A deleted property stops appearing in the results and in the cache after purging.
3. Invariant: Do not expose exact addresses or owners' contact details without a purpose and authorisation.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
