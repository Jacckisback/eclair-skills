# Plan de validation — Carte de restaurant

## Modèle de données
Plat, prix, allergènes, catégorie, disponibilité.

## Mise en œuvre attendue
Saisir la carte fournie par le restaurateur, afficher prix et allergènes, garder une version HTML lisible plutôt qu'un PDF seul.

## Tests à prévoir
1. Nominal : Relire la carte publiée avec le restaurateur, sur mobile.
2. Contrôle de refus : Un plat sans information d'allergènes validée est signalé, pas complété.
3. Invariant : Aucun prix ni allergène inventé ou déduit.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
