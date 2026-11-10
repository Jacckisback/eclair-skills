# Validation plan — Multilingual content

## Data model
Content, language, linked version, address per language.

## Expected implementation
Check the languages supported by the site in the capabilities, organise a tree structure per language, link the versions and check hreflang.

## Tests to plan
1. Nominal: Create a page in two languages and check cross-links and hreflang.
2. Refusal check: A language without a translation does not lead to an empty page.
3. Invariant: No machine translation published without human review.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
