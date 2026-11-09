# Plan de validation — Petites annonces

## Modèle de données
Annonce, annonceur, catégorie, statut, signalement.

## Mise en œuvre attendue
Définir dépôt, modération, durée de vie, signalement et mise en relation sans exposer les coordonnées.

## Tests à prévoir
1. Nominal : Simuler dépôt, modération, expiration et signalement.
2. Contrôle de refus : Une annonce refusée ou expirée n'est plus accessible.
3. Invariant : Aucune annonce publiée sans modération ; coordonnées jamais affichées en clair.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
