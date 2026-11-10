# Validation plan — Newsletter sign-up

## Data model
E-mail address, consent, date, source.

## Expected implementation
Use a sign-up page hosted by the e-mailing service or a link, as long as the site cannot receive sign-ups itself; double opt-in.

## Tests to plan
1. Nominal: Sign up, confirm, unsubscribe.
2. Refusal check: An unconfirmed sign-up receives no mailing.
3. Invariant: No address is added to a list without explicit consent and proof.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
