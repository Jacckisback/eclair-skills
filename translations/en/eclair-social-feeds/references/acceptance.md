# Validation plan — Social media feeds

## Data model
Post, image, link, retrieval date.

## Expected implementation
Retrieve the posts with a server-side scheduled task when the network allows it, render them as static HTML; otherwise simple links to the profiles.

## Tests to plan
1. Nominal: Check the static rendering and the update by task.
2. Refusal check: If the network is unavailable, the last valid version remains displayed.
3. Invariant: No third-party widget is loaded in visitors' browsers.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
