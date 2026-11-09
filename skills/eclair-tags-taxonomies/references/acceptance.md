# Plan de validation — Étiquettes et taxonomies

## Modèle de données
Terme, type de taxonomie, contenus liés, adresse d'archive.

## Mise en œuvre attendue
Inventorier les taxonomies existantes, fusionner celles qui font doublon avec les catégories, proposer des pages de regroupement en GET pour le reste et rediriger les anciennes archives.

## Tests à prévoir
1. Nominal : Convertir un jeu d'étiquettes en catégories ou en pages de regroupement et vérifier les redirections.
2. Contrôle de refus : Une ancienne archive d'étiquette supprimée redirige vers la page la plus proche, sans chaîne.
3. Invariant : Ne pas générer des centaines d'archives pauvres indexables.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
