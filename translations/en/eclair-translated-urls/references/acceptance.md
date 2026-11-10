# Validation plan — Translated addresses

## Data model
Address per language, redirects, canonical, hreflang.

## Expected implementation
Set an address convention per language, translate the slugs before publication, check the canonical and hreflang produced by the core.

## Tests to plan
1. Nominal: Check the canonical and hreflang of each version.
2. Refusal check: Two languages never share the same address.
3. Invariant: No published address is changed without a redirect.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
