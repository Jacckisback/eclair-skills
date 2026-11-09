# Plan de validation — Frises chronologiques

## Modèle de données
Étape, date, titre, texte.

## Mise en œuvre attendue
Rendre la frise en liste ordonnée stylée en CSS, lisible en colonne sur mobile.

## Tests à prévoir
1. Nominal : Vérifier l'ordre de lecture et l'affichage mobile.
2. Contrôle de refus : Une étape sans date reste lisible et ordonnée.
3. Invariant : Les dates et faits affichés sont fournis par le client.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
