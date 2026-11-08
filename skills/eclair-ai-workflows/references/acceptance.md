# Plan de validation — Workflows IA

## Modèle de données
Brouillon, proposition, validation, modèle, coût, source et audit.

## Implémentation attendue
Utiliser capacités MCP du noyau, garder humain dans la boucle, limiter accès et budget; évaluer qualité et hallucinations.

## Tests à prévoir
1. Nominal : Tester prompt injection, changement de contexte et rollback.
2. Contrôle de refus : Une instruction hostile dans un article importé ne devient pas une commande exécutée.
3. Invariant : Aucune IA ne publie, déploie, supprime ou modifie du PHP directement par MCP sans contrôle.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
