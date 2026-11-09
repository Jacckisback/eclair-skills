# Plan de validation — Connecteur MCP

## Modèle de données
Client autorisé, jeton, outils disponibles, brouillons créés.

## Mise en œuvre attendue
Faire activer le connecteur par le propriétaire, autoriser le client, travailler en brouillons et propositions, savoir couper l'accès.

## Tests à prévoir
1. Nominal : Créer un brouillon par le connecteur puis révoquer l'accès.
2. Contrôle de refus : Après révocation, toute requête du client est refusée.
3. Invariant : Le connecteur ne publie ni ne supprime ; l'accès est révocable à tout moment.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
