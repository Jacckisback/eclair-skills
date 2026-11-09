# Plan de validation — Polices

## Modèle de données
Police, graisses, fichier auto-hébergé, repli système.

## Mise en œuvre attendue
Utiliser les polices système ou la police de titre auto-hébergée des directions artistiques, limiter les graisses.

## Tests à prévoir
1. Nominal : Vérifier l'absence de requête tierce et de saut de texte.
2. Contrôle de refus : Une police indisponible laisse un repli lisible.
3. Invariant : Aucune police n'est chargée depuis un service tiers.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
