# Validation plan — Observability and alerts

## Data model
Structured logs, errors, correlations, metrics, traces, retention.

## Expected implementation
Define useful alerts, anonymise data, monitor tasks and cache, distinguish site incident and module incident, provide a runbook.

## Tests to plan
1. Nominal: Test rise in 5xx errors, task delays and full disk.
2. Refusal check: A disabled module does not keep sending data or running tasks.
3. Invariant: No password, token, payment or raw PII in the logs; no hidden telemetry.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
