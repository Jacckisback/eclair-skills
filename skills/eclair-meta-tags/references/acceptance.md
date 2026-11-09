# Plan de validation — Titres et méta-descriptions

## Modèle de données
Titre, méta-description, expression visée, aperçu de résultat.

## Mise en œuvre attendue
Rédiger pour chaque page un titre et une description uniques, s'aider du score en direct de l'éditeur sans le traiter comme un objectif.

## Tests à prévoir
1. Nominal : Contrôler unicité et longueur sur toutes les pages.
2. Contrôle de refus : Deux pages publiées n'ont pas le même titre.
3. Invariant : Aucune promesse de position ; aucun bourrage de mots-clés.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
