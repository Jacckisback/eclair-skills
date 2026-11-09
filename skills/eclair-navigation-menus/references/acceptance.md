# Plan de validation — Menus de navigation

## Modèle de données
Menu, entrée, ordre, cible, emplacement.

## Mise en œuvre attendue
Limiter le menu principal aux parcours essentiels, ranger le reste en pied de page, tester clavier et mobile.

## Tests à prévoir
1. Nominal : Composer les menus et les parcourir au clavier et sur mobile.
2. Contrôle de refus : Une page dépubliée disparaît du menu ou est signalée, jamais servie en 404 depuis la navigation.
3. Invariant : Aucun lien de menu ne pointe vers un brouillon ou une adresse externe non voulue.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
