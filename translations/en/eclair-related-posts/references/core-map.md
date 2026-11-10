# Éclair CMS 2.0.x — verified core map

Reference: public repository `Jacckisback/eclair-cms`, `main` branch verified on 9 November 2026, reference commit `6567d7642ea2227a598c4988e970d43e2e5e0e4f`. **An agent must always re-check the actual checkout and `GET /<admin>/api/capabilities`**: this note is a snapshot, not a guarantee of future compatibility.

## 1. Already built into the core: configure, do not rebuild

Before writing any extension at all, check whether the need is covered natively:

- **Content**: pages and posts made of blocks, categories, menus, authors, drafts, editorial schedule; blocks `paragraph`, `heading`, `list`, `quote`, `image`, `video`, `table`, `code`, `button`, `callout`, `divider`, `hero`, `features`, `faq`, `team`, `contact`.
- **Media**: images resized, re-encoded and converted to responsive WebP, explicit dimensions, lazy loading.
- **Contact form** and message inbox (`messages` permission).
- **SEO and GEO**: titles and descriptions with live analysis, JSON-LD (organisation or local business, article, FAQ, breadcrumb), sitemap with images and `hreflang`, RSS feed, Open Graph with share image, 301 redirects and redirect manager, IndexNow, `llms.txt`, Markdown version of every page, policy for AI crawlers.
- **Speed**: static cache of every public page, inlined CSS, a single public script, no public cookie.
- **Security**: two-factor authentication, attempt limits, strict Content-Security-Policy, sanitised content, integrity check, log, signed updates with rollback.
- **Backups**: download and scheduled upload to remote storage, restore.
- **Lightweight shop**: product pages, variants, categories, payment links from a provider, merchant feed; **no basket, no order and no customer account**.
- **Bundled features**: affiliation, advertising, scheduling, WordPress import, takeover of a former site, AI crawler tracking.
- **AI assistant and MCP connector**: drafts and proposals only, never publication or deletion.
- **Appearance**: themes and art directions, preview before saving.

## 2. Where a skill may write

- Core code: `eclair/app/`, `eclair/assets/`, `eclair/index.php` — **never edit** to deliver a site feature.
- Site extensions: `site/extensions/<id>/` with `extension.json`, `extension.php`, `lib/`, `assets/`, `lang/`.
- Site themes: `site/themes/<id>/` with `theme.json`.
- Extension data: `Eclair\Store`, prefix `$ctx['data']` (`data/ext/<id>/`), secrets in `data/ext/<id>/secrets.php`.
- Content and settings: through the administration or the MCP connector only.

## 3. `eclair-extension/1` contract

- Public routes of an extension: **GET only**, declared in the manifest, cacheable or not.
- Administration: GET/POST under `/<admin>/x/<id>/...`, core permissions (`content`, `media`, `menus`, `categories`, `messages`, `redirects`, `settings`, `users`, `security`) and CSRF protection.
- Declarative blocks and settings validated by the core; scheduled tasks (at most once an hour); idempotent migrations; published assets.
- The code of an extension is **trusted, with no sandbox**: import and activation require an authorised person.
- Validation: `php tools/validate.php <dossier> --json`, then `php tests/run.php` and `php tools/measure.php --check` in a checkout of the core.

## 4. Known limits of 2.0

- No public POST route for extensions (PR #19 in draft, not merged), hence no sign-up, comment, order or upload by a visitor other than through the native contact form.
- No public identity (customer, student, member) in the native contract.
- No content type specific to an extension; no SEO or JSON-LD contribution per extension; no content policy (CSP) per extension; no general rendering filter.
- WordPress tags, comments and custom content types are not carried over by the import.
- The old Éclair Devkit v0.x prototypes targeted the 1.14 core and **do not apply** to 2.0.

Official sources:
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/THEME-CONTRACT.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/SKILLS-GUIDE.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/ARCHITECTURE-2.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/schemas/extension.schema.json
