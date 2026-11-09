# Plan de validation — Filtres et tri du catalogue

## Modèle de données
Critère, valeur, combinaison, adresse filtrée.

## Mise en œuvre attendue
S'appuyer sur les filtres par catégorie natifs ; ajouter des filtres côté navigateur sur données publiques, avec adresses canoniques maîtrisées.

## Tests à prévoir
1. Nominal : Filtrer et trier un catalogue de test sur mobile.
2. Contrôle de refus : Une combinaison sans résultat affiche un message, pas une page vide indexable.
3. Invariant : Les combinaisons de filtres ne créent pas d'infinité de pages indexables.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
