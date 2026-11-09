# Plan de validation — Galeries d'images

## Modèle de données
Galerie, images, légendes, ordre.

## Mise en œuvre attendue
Composer la galerie en grille CSS à partir des images de la médiathèque, avec légendes et textes alternatifs.

## Tests à prévoir
1. Nominal : Afficher une galerie de vingt images sur mobile et mesurer son poids.
2. Contrôle de refus : Une image retirée de la médiathèque ne laisse pas de vignette cassée.
3. Invariant : Aucune image n'est chargée depuis un domaine tiers.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
