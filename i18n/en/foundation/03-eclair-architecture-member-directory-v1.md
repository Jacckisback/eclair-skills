# Éclair Member Directory — v1.0 reference

A native Éclair 2.0 demonstrator is provided in `examples/extensions/member-directory/` at the root of the source distribution; it is not included when the skill is copied on its own.

- `schema`: `eclair-extension/1`; `requires.eclair`: `>=2.0.0`.
- `admin` routes: GET root, POST `/create`, POST `/disable`; `users` permission.
- No public route. No public login, and no validation email is sent.
- `Store`: keys `ext/member-directory/...`, writes under lock, limit of 1,000 members on an experimental basis.
- Member session distinct from the administration sessions, opaque 256-bit token hashed at rest, revocation by epoch.
- Activation after proof of email: not provided by the HTTP surface. A member role cannot be `admin` or `editor`.
- Installer: copy the extension to `site/extensions/member-directory`, pass the 2.0 core's `tools/validate.php`, import and activate manually in a lab only.
- For active accounts intended for the public: RFC for a safe public POST, email validation, rate limiting, reset flow and native tests. No GET route may create/modify an account or a session.
