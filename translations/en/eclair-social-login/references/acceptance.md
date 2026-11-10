# Validation plan — Third-party account login

## Data model
Identity provider, linked account, consent.

## Expected implementation
Depends first on member accounts; design the OAuth flow with state, PKCE and explicit account linking.

## Tests to plan
1. Nominal: Simulate login, linking and unlinking.
2. Refusal check: A replayed or forged OAuth response is refused.
3. Invariant: No account is merged on the sole strength of an unverified email address.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
