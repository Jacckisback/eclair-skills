# Validation plan — Google Analytics

## Data model
Measurement ID, consent, events.

## Expected implementation
First check whether cookieless measurement is enough; otherwise prior consent, and an acknowledgement that the native content policy is not open to extensions.

## Tests to plan
1. Nominal: Check that no request is made before consent.
2. Refusal check: After refusal, no data is sent.
3. Invariant: No measurement script loaded before consent or by bypassing the Content-Security-Policy.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
