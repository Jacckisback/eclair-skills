# Plan de validation — Création de parcours

## Modèle de données
Cours, module, leçon, ordre, brouillon, version publiée et auteur.

## Implémentation attendue
Établir schéma hiérarchique; prévisualiser avant publication; préserver les identifiants lors du réordonnancement; documenter archivage.

## Tests à prévoir
1. Nominal : Tester permutation de leçons, dépublication et édition concurrente.
2. Contrôle de refus : Changer l’ordre ne réinitialise pas la progression des étudiants.
3. Invariant : Les brouillons de formateur ne doivent pas être indexés ou exposés publiquement.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
