# Plan de validation — Stocks et réservations

## Modèle de données
SKU, entrepôt, stock physique, réservé, disponible, mouvements immuables.

## Mise en œuvre attendue
Concevoir les mouvements d’entrée/sortie; verrouiller la réservation; gérer expiration et compensation; tracer toutes les corrections manuelles.

## Tests à prévoir
1. Nominal : Tester achats simultanés du dernier exemplaire et libération après expiration.
2. Contrôle de refus : Deux acheteurs ne peuvent pas réserver le même dernier stock.
3. Invariant : La lecture cacheable de disponibilité est informative; toute vente relit le stock dans une transaction.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
