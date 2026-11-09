# Plan de validation — Plateformes d'automatisation

## Modèle de données
Scénario, déclencheur, données transmises.

## Mise en œuvre attendue
Exposer en lecture ce que la plateforme peut interroger (flux, JSON public) ; concevoir la réception d'événements pour plus tard.

## Tests à prévoir
1. Nominal : Faire lire un flux public par la plateforme et déclencher un scénario.
2. Contrôle de refus : Un appel entrant non authentifié ne modifie rien sur le site.
3. Invariant : Aucune donnée personnelle n'est exposée dans un point d'accès public pour faciliter une automatisation.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
