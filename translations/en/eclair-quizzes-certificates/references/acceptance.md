# Validation plan — Quizzes and certificates

## Data model
Question, choices, answer key, attempt, score, time limit, certificate and verification.

## Expected implementation
Version the question bank; grade server-side; define attempts and time; generate a signed/verifiable certificate without public PII.

## Tests to plan
1. Nominal: Test cheating, end of session, certificate validation.
2. Refusal check: Submitting an attempt twice must not generate two certificates.
3. Invariant: Never send the answer key or the correct answer in the HTML of an active test.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
