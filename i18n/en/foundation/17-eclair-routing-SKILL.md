---
name: eclair-routing
description: Use when creating Éclair CMS 2.0 extension public/admin routes and maintaining exact URLs, redirects and WordPress SEO migration compatibility.
---

# Éclair Routing — protecting URLs and compatibility

## Procedure
1. Record the existing routes and aliases, `Site.php`, `App.php`, `Aliases.php`, `Redirects.php`, `Content::byRoute`, and the reserved URLs.
2. Public extension routes `routes.public[]` are **GET only** and explicitly enumerated. No generic `/{slug}` route via an invented manifest.
3. Admin routes use `routes.admin[]`, GET/POST method, under `/<admin>/x/<id>/...` and with the native `right` permission.
4. Before activation, test collisions with posts/pages/products, reserved routes, multilingual slugs, a site in a subfolder and other extensions.
5. Preserve the exact path of a WordPress migration (trailing slash, .html, accents) through the v2 `route`/`Aliases` mechanisms, without creating several canonicals or chains of 301s.
6. For a feature requiring public POST routes (checkout, customer API), document an RFC/new secure interface instead of intercepting the core or bypassing the router.
7. Check canonicals, sitemap, JSON-LD, noindex for private interfaces, `HEAD`, 404/405 responses and cache.

## Deliverables
Route table, namespace owner, redirect plan, conflicts detected and HTTP tests.

## V1.0 — Public login route forbidden
Éclair 2.0 declarative public GETs are suited to public pages, **not** to a POST login form. No `/login` or `/register` route with side effects may be created with GET. `member-directory` declares only admin routes with the `users` permission.

## Éclair 2.0 — prototype v1.1 (experimental)
Public POST routes are **not** present in official Éclair 2.0. The proposed v1.1 patch makes a controlled exception: explicit POST method, `cache:false`, HTTPS, `Security::checkFormToken()`, `private,no-store` response, relative 303 redirect. Always run HTTP trials with the full CMS before merging.

## Éclair 2.0 — registration and recovery (experimental v1.2)

Read `references/member-email-v1.2.md` before any request to create customer/student accounts or to recover a password. The `member-directory` v0.3 module uses public POST routes **outside the official contract**; never promise a direct installation on unmodified Éclair 2.0, nor enable the email flows without a verified HTTPS URL and native tests. Prefer the v2 extension system to any modification of the old v0.x architecture. Keep public and administrator accounts separate, refuse any shared cache for member pages, and treat emails as undelivered as long as no confirmation exists.
