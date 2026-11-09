# Plan de validation — Listes de souhaits

## Modèle de données
Liste, produit, propriétaire.

## Mise en œuvre attendue
Commencer par un stockage dans le navigateur sans compte ; concevoir la version avec compte pour plus tard.

## Tests à prévoir
1. Nominal : Ajouter, retirer et retrouver des favoris.
2. Contrôle de refus : Un produit supprimé disparaît proprement des listes.
3. Invariant : Aucune liste n'est partagée ou visible par un tiers sans action du propriétaire.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
