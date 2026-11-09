# Plan de validation — Bons plans et codes promo

## Modèle de données
Offre, marchand, code, date de fin, lien.

## Mise en œuvre attendue
Afficher conditions et date de fin, retirer automatiquement les offres expirées, marquer les liens affiliés.

## Tests à prévoir
1. Nominal : Publier une offre datée et constater son retrait à l'échéance.
2. Contrôle de refus : Un lien rémunéré n'apparaît jamais sans mention.
3. Invariant : Aucune offre expirée ou invérifiable présentée comme valide.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
