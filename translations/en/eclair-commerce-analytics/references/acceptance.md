# Validation plan — Sales measurement

## Data model
Funnel, confirmed orders, refunds, conversion rate, net revenue, consents.

## Expected implementation
Define events and metrics without reusing sensitive data; reconcile order totals, credit notes and payments; plan for an aggregated summary.

## Tests to plan
1. Nominal: Test revenue after refund and a break in counting.
2. Refusal check: The aggregation must neither count the same payment twice nor disclose an identifiable order.
3. Invariant: Personal analytics data requires a legal basis and must not leak through the cache.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
