# Validation plan — Performance UX

## Data model
LCP, CLS, INP, asset weight, CSS, JS, cache and fonts.

## Expected implementation
Measure before/after via tools/measure.php --check, Chrome Lighthouse and a slow network, optimise images and scripts.

## Tests to plan
1. Nominal: Test the public site without an extension, with an extension and on mobile.
2. Refusal check: A claimed improvement is accompanied by reproducible before/after measurements.
3. Invariant: Do not degrade the PHP cache path or disable CSP for the sake of convenience.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
