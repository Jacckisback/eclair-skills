# Plan de validation — Annonces immobilières

## Modèle de données
Bien, transaction, géolocalisation arrondie, surface, média, prix, disponibilité.

## Mise en œuvre attendue
Versionner annonces, fournir filtres bornés, gérer statut vendu/loué, images et demandes de visite.

## Tests à prévoir
1. Nominal : Tester annonces retirées, médias privés et filtres.
2. Contrôle de refus : Un bien supprimé cesse d’apparaître dans les résultats et le cache après purge.
3. Invariant : Ne pas exposer adresses exactes ou coordonnées propriétaires sans finalité et autorisation.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
