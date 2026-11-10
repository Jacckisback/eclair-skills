# Plan de validation — Tableau de bord pédagogique

## Modèle de données
Inscriptions, progression, résultats agrégés, événements de cours.

## Mise en œuvre attendue
Définir métriques utiles aux formateurs, filtrer par cours et autorisation; réduire collecte; prévoir rétention et export.

## Tests à prévoir
1. Nominal : Tester visibilité formateur sur cours A vs B.
2. Contrôle de refus : Une requête de statistiques agrégées ne doit pas exposer l’identité d’un étudiant tiers.
3. Invariant : Les statistiques d’un élève ne sont visibles qu’aux parties autorisées.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
