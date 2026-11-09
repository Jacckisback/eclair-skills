# Éclair CMS 2.0.x — carte du noyau vérifiée

Référence : dépôt public `Jacckisback/eclair-cms`, branche `main` vérifiée le 9 novembre 2026, commit de référence `6567d7642ea2227a598c4988e970d43e2e5e0e4f`. **Un agent doit toujours revérifier le checkout réel et `GET /<admin>/api/capabilities`** : cette note est un instantané, non une garantie de compatibilité future.

## 1. Déjà intégré au noyau : configurer, ne pas reconstruire

Avant d'écrire la moindre extension, vérifier si le besoin est couvert nativement :

- **Contenus** : pages et articles en blocs, catégories, menus, auteurs, brouillons, planning éditorial ; blocs `paragraph`, `heading`, `list`, `quote`, `image`, `video`, `table`, `code`, `button`, `callout`, `divider`, `hero`, `features`, `faq`, `team`, `contact`.
- **Médias** : images redimensionnées, ré-encodées et converties en WebP responsive, dimensions explicites, chargement différé.
- **Formulaire de contact** et boîte de réception des messages (droit `messages`).
- **SEO et GEO** : titres et descriptions avec analyse en direct, JSON-LD (organisation ou entreprise locale, article, FAQ, fil d'Ariane), sitemap avec images et `hreflang`, flux RSS, Open Graph avec image de partage, redirections 301 et gestionnaire de redirections, IndexNow, `llms.txt`, version Markdown de chaque page, politique pour les robots d'IA.
- **Vitesse** : cache statique de chaque page publique, CSS intégré, un seul script public, aucun cookie public.
- **Sécurité** : double authentification, limites de tentatives, Content-Security-Policy stricte, contenus assainis, contrôle d'intégrité, journal, mises à jour signées avec retour arrière.
- **Sauvegardes** : téléchargement et envoi planifié vers un stockage distant, restauration.
- **Boutique légère** : fiches produit, variantes, catégories, liens de paiement d'un prestataire, flux marchand ; **pas de panier, de commande ni de compte client**.
- **Fonctions livrées** : affiliation, publicité, planning, import WordPress, reprise d'un ancien site, suivi des robots d'IA.
- **Assistant IA et connecteur MCP** : brouillons et propositions seulement, jamais de publication ni de suppression.
- **Apparence** : thèmes et directions artistiques, aperçu avant enregistrement.

## 2. Où un skill peut écrire

- Code noyau : `eclair/app/`, `eclair/assets/`, `eclair/index.php` — **ne jamais éditer** pour livrer une fonctionnalité de site.
- Fonctions du site : `site/extensions/<id>/` avec `extension.json`, `extension.php`, `lib/`, `assets/`, `lang/`.
- Thèmes du site : `site/themes/<id>/` avec `theme.json`.
- Données d'une extension : `Eclair\Store`, préfixe `$ctx['data']` (`data/ext/<id>/`), secrets dans `data/ext/<id>/secrets.php`.
- Contenus et réglages : par l'administration ou le connecteur MCP uniquement.

## 3. Contrat `eclair-extension/1`

- Routes publiques d'une extension : **GET uniquement**, déclarées dans le manifeste, cacheables ou non.
- Administration : GET/POST sous `/<admin>/x/<id>/...`, droits du noyau (`content`, `media`, `menus`, `categories`, `messages`, `redirects`, `settings`, `users`, `security`) et protection CSRF.
- Blocs et réglages déclaratifs validés par le noyau ; tâches planifiées (au plus une fois par heure) ; migrations idempotentes ; actifs publiés.
- Le code d'une extension est **de confiance, sans bac à sable** : l'import et l'activation exigent une personne autorisée.
- Validation : `php tools/validate.php <dossier> --json`, puis `php tests/run.php` et `php tools/measure.php --check` dans un checkout du noyau.

## 4. Limites connues de la 2.0

- Pas de route POST publique pour les extensions (PR #19 en brouillon, non fusionnée), donc pas d'inscription, de commentaire, de commande ou de dépôt par un visiteur hors formulaire de contact natif.
- Pas d'identité publique (client, élève, membre) dans le contrat natif.
- Pas de type de contenu propre à une extension ; pas de contribution SEO ou JSON-LD par extension ; pas de politique de contenu (CSP) par extension ; pas de filtre général de rendu.
- Étiquettes, commentaires et types de contenu personnalisés de WordPress ne sont pas repris par l'import.
- Les anciens prototypes Éclair Devkit v0.x visaient le noyau 1.14 et **ne s'appliquent pas** à la 2.0.

Sources officielles :
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/EXTENSION-CONTRACT.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/THEME-CONTRACT.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/SKILLS-GUIDE.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/ARCHITECTURE-2.md
- https://github.com/Jacckisback/eclair-cms/blob/main/docs/schemas/extension.schema.json
