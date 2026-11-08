# Éclair CMS 2.0.0 — contrat natif vérifié

Référence : dépôt public `Jacckisback/eclair-cms`, branche `main` vérifiée le 8 novembre 2026, commit de référence `0beb440655090fbd9c3b58e8c56dca7ddbb2106e`. **Un agent doit toujours revérifier le checkout réel** : cette note est un instantané, non une garantie de compatibilité future.

- Code noyau : `eclair/app/`, `eclair/assets/`, `eclair/index.php` — ne jamais éditer pour distribuer une fonctionnalité site.
- Fonctionnalités natives : `eclair/site/extensions/<id>/` (ou le `ECLAIR_SITE` configuré), avec `extension.json`, `extension.php`, `lib/*.php`, `assets/` et `lang/`.
- Données : `Eclair\Store`, préfixe `$ctx['data']` (`data/ext/<id>/`), pas de base SQL obligatoire pour le cœur.
- Thèmes : `eclair/site/themes/<id>/` et `theme.json`.
- Contrat : `eclair-extension/1` ; `docs/EXTENSION-CONTRACT.md` et `docs/schemas/extension.schema.json` ; thème : `docs/THEME-CONTRACT.md`.
- Validation autoritative : `php tools/validate.php mon-extension --json`, puis `php tests/run.php`, `php tools/measure.php --check` dans le checkout du noyau.
- Découverte : `GET /<admin>/api/capabilities`, avec une session admin disposant du droit `settings` ; ne jamais contourner ce contrôle.
- Exemple fonctionnel natif : `examples/extensions/bonjour`.
- Routes publiques d'une extension : **GET uniquement**, chemins déclarés précisément dans le manifeste. Admin : GET/POST sous `/<admin>/x/<id>/...` avec droits du noyau et CSRF.
- Données administratives : les rôles `admin/editor` et `Auth::can` protègent l'administration ; **pas d'identité client/élève/membre public dans le contrat natif**.
- Migrations des extensions : `migrate($id,$ctx)` déclarées et idempotentes ; désactiver conserve code et données selon le cycle de vie.
- Le code des extensions est **de confiance, sans sandbox**. Un skill peut proposer du code ; l'import et l'activation nécessitent la personne autorisée.
- Limites documentées v2.0 : pas de types de contenu métier personnalisés, pas de contribution SEO JSON-LD personnalisée ouverte, pas de CSP déclarative par extension, pas de filtre général de rendu.
- Les anciens prototypes Éclair Devkit v0.2–v0.8 ciblaient le noyau 1.14.2 et **ne doivent pas être appliqués à Éclair 2.0.0**. Ils sont des idées de recherche, non des API natives.

Sources officielles :
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/SKILLS-GUIDE.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/ARCHITECTURE-2.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/schemas/extension.schema.json
