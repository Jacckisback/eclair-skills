# Plan de validation — Budget de poids

## Modèle de données
Budget par type de ressource, mesure, écart.

## Mise en œuvre attendue
Fixer des budgets par page type, mesurer avec l'outil du noyau, refuser tout ajout qui les dépasse sans justification.

## Tests à prévoir
1. Nominal : Lancer la mesure des budgets sur le site et sur le paquet produit.
2. Contrôle de refus : Un paquet qui dépasse le budget n'est pas livré tel quel.
3. Invariant : Aucune dépendance tierce chargée pour une fonction décorative.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
