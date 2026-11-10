# Plan de validation — Bibliothèque de blocs

## Modèle de données
Type namespacé, déclaration des champs, limites, rendu et données conservées.

## Mise en œuvre attendue
Privilégier blocs natifs; déclarer champs autorisés; générer rendu échappé, valeurs par défaut et préservation après désactivation.

## Tests à prévoir
1. Nominal : Tester champs invalides, suppression de la fonction et réinstallation.
2. Contrôle de refus : Le bloc désactivé est conservé mais ni exécuté ni rendu.
3. Invariant : Refuser l’exécution de HTML/JS issu de champs; aucune perte de données lorsque le bloc manque.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
