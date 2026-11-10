# Validation plan — Core Web Vitals

## Data model
Largest element display, stability, responsiveness, per template.

## Expected implementation
Measure in the lab and on real-world data where it exists, address the main cause per template, measure again.

## Tests to plan
1. Nominal: Measure three templates on mobile before and after the fix.
2. Refusal check: An unmeasured improvement is not announced as achieved.
3. Invariant: No score is promised; only measured results are reported.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
