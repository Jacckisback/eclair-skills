# Plan de validation — Grilles tarifaires

## Modèle de données
Offre, prix, période, caractéristiques, bouton.

## Mise en œuvre attendue
Composer les offres en cartes comparables, afficher prix TTC ou HT sans ambiguïté et relier chaque bouton à la bonne action.

## Tests à prévoir
1. Nominal : Comparer trois offres sur mobile et vérifier chaque lien.
2. Contrôle de refus : Une offre sans prix validé n'est pas affichée.
3. Invariant : Aucun prix, remise ou mention légale inventés.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
