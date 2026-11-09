# Plan de validation — Formulaires conditionnels

## Modèle de données
Champ, condition, branche, validation.

## Mise en œuvre attendue
Décrire les règles en données, les appliquer côté serveur et côté navigateur, tester chaque branche.

## Tests à prévoir
1. Nominal : Parcourir chaque branche jusqu'à l'envoi.
2. Contrôle de refus : Un champ requis d'une branche active ne peut pas être contourné.
3. Invariant : La validation serveur ne fait jamais confiance aux champs masqués côté navigateur.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
