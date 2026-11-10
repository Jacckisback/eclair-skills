# Technical reference — Member Directory v0.3.0 (Éclair v2.0.0, experimental POST contract)

## Available flows (all cache:false)

| Method | Route | Role |
|---|---|---|
| GET/POST | `/membres/connexion` | Form / login for an active account |
| GET | `/membres/espace` | Private profile specific to the session token |
| POST | `/membres/deconnexion` | Logout with session-specific CSRF |
| GET/POST | `/membres/inscription` | Invitation email, only if `registration_enabled=true` |
| GET/POST | `/membres/verification` | Choose the password with single-use email proof |
| GET/POST | `/membres/recuperation` | Request a recovery email if `recovery_enabled=true` |
| GET/POST | `/membres/reinitialisation` | Replace the password with single-use proof |

## Mechanisms

- No CMS account/`Auth::can` for customers. `member` profiles never contain `admin` or `editor` roles.
- `MemberAccounts::provision` requires a random temporary password and creates a `pending` account. The email link asks the person to choose their own password. The verification token expires after 30 minutes and a receipt can be used only once.
- `MemberAccounts::issueReset` issues only for an `active` member, then `confirmReset` performs the mutation under lock and increments `epoch`. All previous session tokens become invalid.
- `Mail::send` (Éclair service) is used, but it is not a delivery receipt. Do not promise the user any successful delivery.
- To send an email, the configured canonical URL must be HTTPS and verified. The domain of the HTTP request is excluded from the recovery link.
- GET pages perform no business processing; POST requires HTTPS and `Security::checkFormToken`, and the core patch itself also checks these conditions.
- Limiters per network / email, generic messages on requests, proofs validated twice (preflight before the hash, then under the storage lock).
- No personal resource goes into the public static cache. Token links must be excluded from the logs and from any external page loaded from the confirmation forms.

## Explicit limits

- A pending account whose email is accepted by the transport but never received requires a new-invitation/support flow, which is not provided here.
- Generic messages do not entirely remove the possibility of inferring the existence of an account from the execution time.
- Email tokens in URLs may appear in the browser history or in logs: an infrastructure audit is mandatory.
- The `Store` prototype is limited to 1,000 members and is not a multi-file transactional relational database.
- The official `eclair-extension/1` contract does **not** allow public POST without the patch. Any installation on a real site awaits its validation.
