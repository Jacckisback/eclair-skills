# Validation plan — Transactional emails

## Data model
Template, language, consent, recipient, domain, event, delivery.

## Expected implementation
Prepare text/HTML templates, DKIM/SPF/DMARC and deliverability; distinguish transactional and marketing, log without secrets, unsubscription required.

## Tests to plan
1. Nominal: Test SMTP error, address error, retry and token expiry.
2. Refusal check: An SMTP failure does not mark an email as delivered nor block an account permanently.
3. Invariant: Do not send a recovery token through an unverified URL; never spam without consent.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
