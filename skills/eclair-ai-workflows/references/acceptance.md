# Plan de validation — Workflows IA

## Modèle de données
Brouillon, proposition, validation, modèle, coût, source et audit.

## Mise en œuvre attendue
Utiliser capacités MCP du noyau, garder humain dans la boucle, limiter accès et budget; évaluer qualité et hallucinations.

## Tests à prévoir
1. Nominal : Tester prompt injection, changement de contexte et rollback.
2. Contrôle de refus : Une instruction hostile dans un article importé ne devient pas une commande exécutée.
3. Invariant : Aucune IA ne publie, déploie, supprime ou modifie du PHP directement par MCP sans contrôle.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
