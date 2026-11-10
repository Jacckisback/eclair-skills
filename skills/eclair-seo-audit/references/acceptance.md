# Plan de validation — Audit SEO technique

## Modèle de données
URLs, canonicals, sitemap, redirections, titres, statuts HTTP, données structurées.

## Mise en œuvre attendue
Crawler les pages autorisées, relever divergences, prioriser causes structurelles, vérifier couverture et plan de correction.

## Tests à prévoir
1. Nominal : Tester slash, accents, paginations, 404, sitemap et robots.
2. Contrôle de refus : Aucune URL critique n’est orpheline ou redirigée en chaîne après mise à jour.
3. Invariant : Ne pas promettre de classement; ne pas modifier les URLs existantes sans plan des redirects.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
