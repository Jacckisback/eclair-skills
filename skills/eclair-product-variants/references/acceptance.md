# Plan de validation — Variantes et attributs

## Modèle de données
Produit parent, variantes à SKU unique, combinaisons d’attributs, prix/stock propres, média et statut.

## Mise en œuvre attendue
Définir le nombre maximal de combinaisons; assurer unicité SKU; projeter variantes dans le rendu GET; préparer sélection validée au serveur lors du checkout.

## Tests à prévoir
1. Nominal : Tester variantes absentes, épuisées et désactivées.
2. Contrôle de refus : Deux combinaisons créent le même SKU => refus explicite avant publication.
3. Invariant : Ne jamais accepter prix, poids ou stock envoyés par le navigateur comme données fiables.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
