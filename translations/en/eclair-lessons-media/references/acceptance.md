# Validation plan — Teaching media

## Data model
Lesson, media, transcript, downloadable files, permissions and duration.

## Expected implementation
Prepare accessible media and subtitles; plan delivery with server-side authorisation or a short-lived signed URL; separate public CDN and restricted content.

## Tests to plan
1. Nominal: Test expired media, access without enrolment and mobile.
2. Refusal check: A private document URL copied into another browser is refused or expires.
3. Invariant: Hiding a link in the HTML is not protection; do not place private media in the public /media.
4. GET/HEAD: public cache only without session state or sensitive data; canonical, HTTP status, SEO and GEO unchanged or improved.
5. POST: never any shared cache; CSRF, TLS, permissions, attempt limiting, idempotency. Do not run if the core does not officially support it.
6. Activation and deactivation: content is preserved and public routes are removed without any leak.
7. Checks: native validator, PHP and HTTP tests, budgets; record the commands run, their results and what was not tested.

## Proof of availability
Status of the feature or extension, CI logs, test matrix, rollback procedure, and refusal of any unverified promise.
