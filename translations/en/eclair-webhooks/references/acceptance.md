# Validation plan — Incoming and outgoing webhooks

## Data model
Source, secret, event, signature, timestamp, unique ID, attempt, result.

## Expected implementation
Specify the contract, verify the signature on raw bytes, anti-replay and durable queue; document retries/dlq and private POST endpoint.

## Tests to plan
1. Nominal: Test double sending, delay, reversed order and changed secret.
2. Refusal check: Two attempts of the same webhook trigger only a single business mutation.
3. Invariant: Never publish a webhook with a secret in the URL nor process an unsigned financial event.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
