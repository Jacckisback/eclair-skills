# Plan de validation — Demandes relatives aux données

## Modèle de données
Demande, personne, données concernées, délai, réponse.

## Mise en œuvre attendue
Cartographier où sont les données (messages, comptes, journaux, sauvegardes), écrire la procédure d'accès et d'effacement, tenir un registre.

## Tests à prévoir
1. Nominal : Dérouler une demande d'accès puis d'effacement sur un jeu de test.
2. Contrôle de refus : Une demande sans vérification d'identité n'aboutit à aucune divulgation.
3. Invariant : L'identité du demandeur est vérifiée avant toute communication de données.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
