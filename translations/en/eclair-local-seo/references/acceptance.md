# Validation plan — Local SEO

## Data model
Name, address, telephone, opening hours, service area.

## Expected implementation
Enter the exact contact details in the settings, check the local business markup produced by the core, align the business listing and the site.

## Tests to plan
1. Nominal: Compare the contact details of the site, the markup and the business listing.
2. Refusal check: Unconfirmed opening hours are not published.
3. Invariant: No invented address, review or service area.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
