# Plan de validation — Optimisation des images

## Modèle de données
Image source, variantes responsives, dimensions, poids.

## Mise en œuvre attendue
Fournir des sources de bonne taille, laisser le noyau produire les variantes, contrôler le poids réel servi sur mobile.

## Tests à prévoir
1. Nominal : Mesurer poids et dimensions servis sur mobile et ordinateur.
2. Contrôle de refus : Aucune image n'est servie sans dimensions explicites.
3. Invariant : Les métadonnées sensibles (géolocalisation) ne sont pas publiées.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
