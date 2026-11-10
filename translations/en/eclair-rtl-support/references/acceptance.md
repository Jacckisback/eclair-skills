# Validation plan — Right-to-left languages

## Data model
Text direction, CSS logical properties, directional icons.

## Expected implementation
Use CSS logical properties in the site theme, test each template in dir=rtl.

## Tests to plan
1. Nominal: Display the typical pages right to left with no overflow.
2. Refusal check: A mix of languages does not break the reading order.
3. Invariant: No user text is injected without escaping, including direction characters.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
