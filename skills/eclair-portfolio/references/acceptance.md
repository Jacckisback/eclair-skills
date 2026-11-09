# Plan de validation — Portfolio et réalisations

## Modèle de données
Réalisation, client, contexte, résultat, images.

## Mise en œuvre attendue
Rédiger chaque réalisation en problème, solution, résultat, avec images légères et accord du client.

## Tests à prévoir
1. Nominal : Parcourir liste et détail sur mobile.
2. Contrôle de refus : Une réalisation sans accord consigné reste en brouillon.
3. Invariant : Aucun client, chiffre ou résultat publié sans accord.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
