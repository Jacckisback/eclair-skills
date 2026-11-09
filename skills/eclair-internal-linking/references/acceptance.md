# Plan de validation — Maillage interne

## Modèle de données
Page source, page cible, ancre, pages orphelines.

## Mise en œuvre attendue
Cartographier les liens, repérer les pages orphelines, ajouter des liens utiles avec des ancres descriptives.

## Tests à prévoir
1. Nominal : Vérifier que chaque page importante reçoit au moins un lien interne.
2. Contrôle de refus : Aucun lien interne ne pointe vers une redirection ou une erreur.
3. Invariant : Aucun lien n'est ajouté automatiquement sans relecture du contexte.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
