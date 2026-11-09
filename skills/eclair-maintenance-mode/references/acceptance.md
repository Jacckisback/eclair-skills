# Plan de validation — Mode maintenance

## Modèle de données
État de maintenance, message, durée prévue, accès de l'équipe.

## Mise en œuvre attendue
Servir une page statique avec le bon statut HTTP temporaire au niveau du serveur, garder l'accès à l'administration, prévoir la remise en ligne.

## Tests à prévoir
1. Nominal : Activer, vérifier statut 503 et en-tête de réessai, désactiver.
2. Contrôle de refus : Les robots ne reçoivent jamais la page de maintenance avec un statut 200.
3. Invariant : La page de maintenance ne révèle ni version ni chemin du serveur.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
