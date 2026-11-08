# Plan de validation — Tableau de bord pédagogique

## Modèle de données
Inscriptions, progression, résultats agrégés, événements de cours.

## Implémentation attendue
Définir métriques utiles aux formateurs, filtrer par cours et autorisation; réduire collecte; prévoir rétention et export.

## Tests à prévoir
1. Nominal : Tester visibilité formateur sur cours A vs B.
2. Contrôle de refus : Une requête de statistiques agrégées ne doit pas exposer l’identité d’un étudiant tiers.
3. Invariant : Les statistiques d’un élève ne sont visibles qu’aux parties autorisées.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
