# Plan de validation — Devoirs et corrections

## Modèle de données
Devoir, dépôt, note, commentaire, apprenant.

## Mise en œuvre attendue
Définir dépôt, délais, correction et retour ; cloisonner chaque copie à son auteur et au correcteur.

## Tests à prévoir
1. Nominal : Simuler dépôt, correction et consultation de la note.
2. Contrôle de refus : Un apprenant ne peut pas accéder à la copie d'un autre.
3. Invariant : Une copie n'est lisible que par son auteur et les correcteurs désignés.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
