---
name: eclair-security-audit
description: Use when auditing Éclair CMS 2.0 native extensions, package supply chain, admin actions, member data and future commerce/LMS security.
---

# Éclair Security Audit — review before activation

## Scope
1. Establish the core version, the provenance of the extension, the executable files and the permissions requested.
2. Require a conforming `extension.json` contract and SHA-256 fingerprints for the files; check symlinks, path traversal, unexpected scripts, ZIP bombs, sizes, methods and reserved routes.
3. Check separately the native `right` of an admin route and the business authorisations on objects; a `content` permission does not authorise reading another customer's order.
4. Test CSRF, rate limiting, session fixation, direct file access, XSS in returned HTML, SQL injection, SSRF through external URLs, and secrets management.
5. Public pages with `cache:true`: absence of personal data and of per-user variants. Admin pages: headers, authentication and deny-by-default.
6. For a checkout: signed webhook with server-side verification, idempotency, amounts, currency, VAT and transactional state transitions before delivery.
7. For business events: point out that v2 does not include a standard bus/outbox; a separate project with failure tests and no promise of exactly-once for remote effects.
8. Never run unaudited modules with the trust of the PHP process.

## Minimum evidence
`php tools/validate.php chemin/extension --json`, `php tests/run.php`, `php tools/measure.php --check` and negative HTTP scenarios on a test installation. No security report is an automatic certification.

## Deliverables
List of ranked risks, reproducible demonstrations, fixes, remaining limits and an explicit Go/No-Go decision.

## V1.0 — Identity tests
Audit the `member-directory` prototype: no member account in `data/users.php`, password never returned, `pending` status by default, `admin/editor` roles forbidden, revocation epoch, own/other object check, `__Host-` HTTPS cookie. Local tests are not equivalent to a production audit.

## Éclair 2.0 — prototype v1.1 (experimental)
The v1.1 prototype has `RateLimit::attempt` limiting before hashing, a strict members/admin separation and 256-bit session tokens. Assess the security of `Origin` handling, of TLS behind a reverse proxy, CSRF, IDOR, account enumeration, information leaks and concurrency. Do not confuse isolated tests with a production audit.

## Éclair 2.0 — registration and recovery (experimental v1.2)

Read `references/member-email-v1.2.md` before any request to create customer/student accounts or to recover a password. The `member-directory` v0.3 module uses public POST routes **outside the official contract**; never promise a direct installation on unmodified Éclair 2.0, nor enable the email flows without a verified HTTPS URL and native tests. Prefer the v2 extension system to any modification of the old v0.x architecture. Keep public and administrator accounts separate, refuse any shared cache for member pages, and treat emails as undelivered as long as no confirmation exists.
