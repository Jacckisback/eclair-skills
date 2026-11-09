# Plan de validation — Flux produits

## Modèle de données
Produit, prix, disponibilité, image, identifiants.

## Mise en œuvre attendue
Compléter les fiches, contrôler le flux produit par le noyau, le déclarer dans l'outil marchand, corriger les rejets.

## Tests à prévoir
1. Nominal : Valider le flux et comparer trois produits avec leur fiche.
2. Contrôle de refus : Un produit indisponible n'est pas annoncé en stock.
3. Invariant : Prix et disponibilité du flux sont ceux de la fiche publique.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
