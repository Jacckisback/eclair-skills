# Plan de validation — Audit SEO technique

## Modèle de données
URLs, canonicals, sitemap, redirections, titres, statuts HTTP, données structurées.

## Implémentation attendue
Crawler les pages autorisées, relever divergences, prioriser causes structurelles, vérifier couverture et plan de correction.

## Tests à prévoir
1. Nominal : Tester slash, accents, paginations, 404, sitemap et robots.
2. Contrôle de refus : Aucune URL critique n’est orpheline ou redirigée en chaîne après mise à jour.
3. Invariant : Ne pas promettre de classement; ne pas modifier les URLs existantes sans plan des redirects.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
