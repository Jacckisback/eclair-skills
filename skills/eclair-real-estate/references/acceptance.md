# Plan de validation — Annonces immobilières

## Modèle de données
Bien, transaction, géolocalisation arrondie, surface, média, prix, disponibilité.

## Implémentation attendue
Versionner annonces, fournir filtres bornés, gérer statut vendu/loué, images et demandes de visite.

## Tests à prévoir
1. Nominal : Tester annonces retirées, médias privés et filtres.
2. Contrôle de refus : Un bien supprimé cesse d’apparaître dans les résultats et le cache après purge.
3. Invariant : Ne pas exposer adresses exactes ou coordonnées propriétaires sans finalité et autorisation.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
