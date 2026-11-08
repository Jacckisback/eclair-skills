# Plan de validation — Stocks et réservations

## Modèle de données
SKU, entrepôt, stock physique, réservé, disponible, mouvements immuables.

## Implémentation attendue
Concevoir les mouvements d’entrée/sortie; verrouiller la réservation; gérer expiration et compensation; tracer toutes les corrections manuelles.

## Tests à prévoir
1. Nominal : Tester achats simultanés du dernier exemplaire et libération après expiration.
2. Contrôle de refus : Deux acheteurs ne peuvent pas réserver le même dernier stock.
3. Invariant : La lecture cacheable de disponibilité est informative; toute vente relit le stock dans une transaction.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
