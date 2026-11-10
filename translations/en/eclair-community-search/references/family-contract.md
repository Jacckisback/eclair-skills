# Contract for the Forum & community family

Target: **Éclair CMS 2.0.x**, extension **`eclair-extension/1`**, identifiers and version discovered before any change.

**Native capabilities to favour:** features already built into the core (see `core-map.md`), themes in `site/themes/`, extensions in `site/extensions/`, `Store` data under `$ctx['data']`, public GET routes and protected administration GET/POST routes, scheduled tasks, migrations, `tools/validate.php` validation, PHP suite, measurements.

**Production limitations:** Public categories and lists can be GET; posts, reports, private profiles and moderation require an identity and safe write routes, anti-spam and suitable storage.

**Agent policy:** use what is native first, generate the minimum of code, keep the core intact, refuse to present a mock-up as a feature in service; request a core change when one is needed. High-impact changes (payment, private content, emails, personal or health data) require real tests and human validation before activation.

**Security points:** check every object and every write; protect forms, secrets, signatures and personal data; verify errors and rollback; keep in the public cache only HTML that contains no user data. Do not confuse `eclair-extension/1` with the earlier experimental APIs.
