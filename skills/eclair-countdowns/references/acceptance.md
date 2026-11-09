# Plan de validation — Comptes à rebours

## Modèle de données
Date cible, fuseau horaire, message de fin.

## Mise en œuvre attendue
Écrire la date dans le HTML, animer en amélioration progressive, prévoir l'état après échéance et l'invalidation du cache.

## Tests à prévoir
1. Nominal : Tester avant, pendant et après l'échéance et dans deux fuseaux.
2. Contrôle de refus : Après l'échéance, la page en cache n'affiche plus d'offre expirée.
3. Invariant : Aucune fausse urgence : la date correspond à un événement réel.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
