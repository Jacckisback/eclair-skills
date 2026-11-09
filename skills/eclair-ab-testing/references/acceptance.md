# Plan de validation — Tests A/B

## Modèle de données
Variante, répartition, objectif, résultat.

## Mise en œuvre attendue
Tester par périodes successives ou par adresses distinctes plutôt que par variantes dans le cache ; fixer hypothèse, durée et mesure à l'avance.

## Tests à prévoir
1. Nominal : Dérouler un test sur deux pages d'atterrissage distinctes.
2. Contrôle de refus : Un résultat sans volume suffisant n'est pas présenté comme concluant.
3. Invariant : Aucune variante n'est stockée dans le cache partagé selon le visiteur.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
