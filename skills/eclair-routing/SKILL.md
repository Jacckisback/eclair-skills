---
name: eclair-routing
description: Use when creating Éclair CMS 2.0 extension public/admin routes and maintaining exact URLs, redirects and WordPress SEO migration compatibility.
---

# Éclair Routing — protéger les URL et la compatibilité

## Procédure
1. Relever les routes et alias existants, `Site.php`, `App.php`, `Aliases.php`, `Redirects.php`, `Content::byRoute`, et les URL réservées.
2. Les routes publiques d'extension `routes.public[]` sont **GET seulement** et explicitement énumérées. Pas de route générique `/{slug}` via un manifeste inventé.
3. Les routes admin utilisent `routes.admin[]`, méthode GET/POST, sous `/<admin>/x/<id>/...` et avec le droit `right` natif.
4. Tester avant activation les collisions avec articles/pages/produits, routes réservées, slug multilingue, site en sous-dossier et autres extensions.
5. Préserver le chemin exact d'une migration WordPress (slash final, .html, accents) par les mécanismes v2 `route`/`Aliases`, sans créer plusieurs canonicals ni cascades de 301.
6. Pour une fonction nécessitant routes publiques POST (checkout, API client), documenter une RFC/nouvelle interface sécurisée au lieu d'intercepter le noyau ou de contourner le routeur.
7. Vérifier canonicals, sitemap, JSON-LD, noindex pour les interfaces privées, `HEAD`, réponses 404/405 et cache.

## Livrables
Table des routes, propriétaire du namespace, plan de redirections, conflits détectés et tests HTTP.

## V1.0 — Route publique de connexion interdite
Les GET publics déclaratifs Éclair 2.0 sont adaptés à des pages publiques, **pas** à un formulaire POST de connexion. Aucune route `/login` ni `/register` à effets de bord ne doit être créée avec GET. `member-directory` ne déclare que des routes admin avec droit `users`.

## Éclair 2.0 — prototype v1.1 (experimental)
Les routes publiques POST ne sont **pas** présentes dans Éclair 2.0 officiel. Le patch proposé v1.1 fait une exception contrôlée : méthode POST explicite, `cache:false`, HTTPS, `Security::checkFormToken()`, réponse `private,no-store`, redirection 303 relative. Toujours faire des essais HTTP avec le CMS complet avant fusion.

## Éclair 2.0 — inscription et récupération (v1.2 expérimentale)

Lire `references/member-email-v1.2.md` avant toute demande de création de comptes clients/élèves ou de récupération de mot de passe. Le module `member-directory` v0.3 utilise des routes publiques POST **hors contrat officiel** ; ne jamais promettre une installation directe sur Éclair 2.0 non modifié ni activer les flux email sans URL HTTPS vérifiée et tests natifs. Préférer le système d'extensions v2 à toute modification de l'ancienne architecture v0.x. Garder séparés les comptes publics et administrateurs, refuser tout cache partagé pour les pages membres, et traiter les emails comme non livrés tant qu'aucune confirmation n'existe.
