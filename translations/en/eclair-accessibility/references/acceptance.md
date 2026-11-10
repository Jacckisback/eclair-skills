# Validation plan — WCAG accessibility

## Data model
Heading structure, keyboard navigation, focus, forms, media, contrasts.

## Expected implementation
Carry out a keyboard and screen reader audit, check axe-core, contrasts, error messages and reduced motion.

## Tests to plan
1. Nominal: Test mouse-free journeys, form errors and 200% zoom.
2. Refusal check: A form remains understandable without colour and from the keyboard.
3. Invariant: Do not remove visible focus or make a feature depend solely on colour or gesture.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
