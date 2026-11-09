# Plan de validation — Cache de pages

## Modèle de données
Page en cache, invalidation, variantes interdites.

## Mise en œuvre attendue
Mesurer la réponse en cache, repérer ce qui empêche la mise en cache d'une route d'extension, vérifier l'invalidation à la modification.

## Tests à prévoir
1. Nominal : Mesurer le temps de réponse avant et après une modification.
2. Contrôle de refus : Une route d'extension déclarée non cacheable n'est jamais servie depuis le cache.
3. Invariant : Aucune page contenant des données de session ou personnelles n'entre dans le cache partagé.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
