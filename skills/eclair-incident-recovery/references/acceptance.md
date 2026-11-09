# Plan de validation — Réponse à incident

## Modèle de données
Incident, chronologie, comptes touchés, sauvegarde saine.

## Mise en œuvre attendue
Isoler, conserver les preuves, changer les secrets, contrôler l'intégrité, restaurer une sauvegarde saine, informer les personnes concernées si nécessaire.

## Tests à prévoir
1. Nominal : Jouer l'exercice sur une copie : détection, restauration, contrôle.
2. Contrôle de refus : Un site restauré n'est pas remis en ligne avant le changement de tous les secrets.
3. Invariant : Ne jamais supprimer les traces avant de les avoir copiées.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
