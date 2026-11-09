# Plan de validation — Fil d'Ariane

## Modèle de données
Niveaux, libellés, adresses.

## Mise en œuvre attendue
Contrôler la cohérence entre arborescence, fil d'Ariane affiché et données structurées du noyau.

## Tests à prévoir
1. Nominal : Comparer fil affiché et balisage sur trois niveaux de profondeur.
2. Contrôle de refus : Une page orpheline n'affiche pas de fil incohérent.
3. Invariant : Le fil d'Ariane ne révèle aucune page non publiée.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
