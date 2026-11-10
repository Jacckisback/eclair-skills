# Validation plan — Tabs

## Data model
Tab, title, panel.

## Expected implementation
Build a tabs block with ARIA roles, arrow-key navigation and a fallback to stacked sections.

## Tests to plan
1. Nominal: Go through the tabs with the keyboard and a screen reader.
2. Refusal check: Without JavaScript, all the panels are visible.
3. Invariant: All the content stays in the HTML, and is therefore readable without JavaScript.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
