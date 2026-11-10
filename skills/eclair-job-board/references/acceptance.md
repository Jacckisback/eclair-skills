# Plan de validation — Offres d’emploi

## Modèle de données
Offre, entreprise, statut, échéance, candidature et pièces jointes.

## Mise en œuvre attendue
Construire filtres publics, expiration automatique, formulaires sécurisés et cycle de rétention des candidatures.

## Tests à prévoir
1. Nominal : Tester annonce expirée, spam et export candidat.
2. Contrôle de refus : Un recruteur ne peut pas lire une candidature destinée à une autre entreprise.
3. Invariant : CV et pièces jointes ne sont jamais placés dans un répertoire web accessible.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
