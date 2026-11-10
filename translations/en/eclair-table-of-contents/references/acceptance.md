# Validation plan — Automatic table of contents

## Data model
Subheadings, anchors, levels.

## Expected implementation
Generate the table of contents from the subheadings at server rendering, with stable anchors and no mandatory JavaScript.

## Tests to plan
1. Nominal: Check the table of contents on content with three levels of subheadings.
2. Refusal check: Short content with no subheading displays no empty table of contents.
3. Invariant: The generated anchors are escaped and unique.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
