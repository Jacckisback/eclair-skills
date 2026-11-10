# Plan de validation — UX responsive

## Modèle de données
Breakpoints, densité, largeur de texte, menu, formulaires et médias.

## Mise en œuvre attendue
Concevoir mobile-first; garder hiérarchie de l’information; tester petits écrans, tailles de cibles et orientations.

## Tests à prévoir
1. Nominal : Tester 320px, 375px, tablette et clavier mobile.
2. Contrôle de refus : Une action primaire reste visible et utilisable sur écran étroit sans scroll horizontal.
3. Invariant : Aucun contenu essentiel caché sur mobile ou dépendant d’animation.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
