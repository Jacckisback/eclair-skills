# Validation plan — Delivery and shipping

## Data model
Validated address, zone, carrier, parcel, weight, service, fees, tracking.

## Expected implementation
Model zones and incompatibilities; calculate quotes on the server side; plan for split shipments and partial delivery; anonymise shipping data in logs.

## Tests to plan
1. Nominal: Test an unserved zone, weight limit, two parcels and lost status.
2. Refusal check: One customer's tracking number must not be visible from another account.
3. Invariant: Address and tracking are private; no personal data in the public cache, detailed logs or URLs.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
