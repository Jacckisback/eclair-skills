# Plan de validation — Création de parcours

## Modèle de données
Cours, module, leçon, ordre, brouillon, version publiée et auteur.

## Mise en œuvre attendue
Établir schéma hiérarchique; prévisualiser avant publication; préserver les identifiants lors du réordonnancement; documenter archivage.

## Tests à prévoir
1. Nominal : Tester permutation de leçons, dépublication et édition concurrente.
2. Contrôle de refus : Changer l’ordre ne réinitialise pas la progression des étudiants.
3. Invariant : Les brouillons de formateur ne doivent pas être indexés ou exposés publiquement.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
