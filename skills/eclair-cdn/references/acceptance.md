# Plan de validation — Réseau de diffusion (CDN)

## Modèle de données
Zone DNS, règles de cache, purge.

## Mise en œuvre attendue
Régler DNS et HTTPS de bout en bout, exclure l'administration du cache du CDN, définir la purge à la publication.

## Tests à prévoir
1. Nominal : Vérifier en-têtes de cache des pages publiques et de l'administration.
2. Contrôle de refus : Après modification, l'ancienne version n'est plus servie passé la purge.
3. Invariant : L'administration et toute réponse privée ne sont jamais mises en cache par le CDN.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
