# Plan de validation — Cookies et consentement

## Modèle de données
Traceur, finalité, consentement, preuve.

## Mise en œuvre attendue
Inventorier les traceurs réels ; sans traceur, pas de bandeau ; sinon consentement préalable, refus aussi simple que l'accord et page d'information.

## Tests à prévoir
1. Nominal : Inspecter cookies et requêtes avant et après choix.
2. Contrôle de refus : Après un refus, aucun traceur tiers n'est chargé.
3. Invariant : Aucun traceur soumis à consentement n'est déposé avant l'accord.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
