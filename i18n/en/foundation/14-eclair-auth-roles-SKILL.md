---
name: eclair-auth-roles
description: Use when reviewing Éclair v2 admin rights or designing member, student, customer and moderator authentication beyond the admin-only built-in roles.
---

# Éclair Auth & Roles — distinguishing admin and members

## The v2 reality
`Eclair\Auth` and `Users` control **the administration** with its permissions (`content`, `settings`, `security`, etc.). They are not a directory of customers, students or members, and must not be misused as `customer/student` roles.

## Procedure
1. Consult `Users`, `Auth`, `Admin`, `Security`, `Session`, `RateLimit` and the permission required by each `eclair-extension/1` admin route.
2. For an administration feature, declare `routes.admin[]` with the exact `right` and rely on the core's CSRF verification. Check access for each existing role.
3. For a public customer/student area: produce an identity-provider RFC or a dedicated, audited server component with suitable storage; **do not** expose sensitive routes via public GET.
4. Define the independent member session, the `Secure/HttpOnly/SameSite` cookies, step-up authentication, rate limiting, recovery and email verification.
5. Permissions: systematically identify the subject through a verified server session, then check the object and the scope (IDOR/BOLA) on every request.
6. Test the absence of privileges inherited from the admin, role change, revocation, reset, session races, cross-account access, CSRF and deny-by-default.

## Native demonstrator v1.0
The extension `examples/extensions/member-directory/` provides an **admin-only** example for Éclair 2.0:
- `routes.admin`: GET + POST (`users`) with reinforced checks in the handlers; `routes.public`: empty array.
- `MemberAccounts` and `MemberSessions` remain independent of `Eclair\Users/Auth/Session`; a `pending` account is mandatory at provisioning.
- The data resides exclusively under `data/ext/member-directory/` via `Store`. Never in `data/users.php`.
- `MemberPermissions::allows` takes a verified session token, not an identity supplied by the caller.
- Neither public registration, nor any email sent, nor password recovery, nor real HTTP session management is enabled.
- The public POST API requires an RFC/new core contract and end-to-end validation before deployment.
Read `references/member-directory-v1.md` before building an LMS, a forum or a shop.

## Deliverables
Permissions and resources matrix, threat model, identity plan, test sets and a “native / RFC required” indication.

## Éclair 2.0 — prototype v1.1 (experimental)
The v1.1 prototype has public handlers: GET form + POST login/logout + GET private area. They are valid only after the approved addition of the POST contract. Member sessions distinct from admin sessions, opaque token, double-submit CSRF and session CSRF on logout; no admin/editor role granted.

## Éclair 2.0 — registration and recovery (experimental v1.2)

Read `references/member-email-v1.2.md` before any request to create customer/student accounts or to recover a password. The `member-directory` v0.3 module uses public POST routes **outside the official contract**; never promise a direct installation on unmodified Éclair 2.0, nor enable the email flows without a verified HTTPS URL and native tests. Prefer the v2 extension system to any modification of the old v0.x architecture. Keep public and administrator accounts separate, refuse any shared cache for member pages, and treat emails as undelivered as long as no confirmation exists.
