# Plan de validation — Téléchargements

## Modèle de données
Fichier, titre, version, taille, page porteuse.

## Mise en œuvre attendue
Ranger les fichiers publics dans la médiathèque, afficher poids et format, versionner les fichiers remplacés.

## Tests à prévoir
1. Nominal : Télécharger chaque fichier et vérifier type et taille annoncés.
2. Contrôle de refus : Un fichier remplacé ne laisse pas l'ancienne version accessible par erreur.
3. Invariant : Aucun fichier privé ou payant n'est placé à une adresse publique devinable.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
