# Plan de validation — UX responsive

## Modèle de données
Breakpoints, densité, largeur de texte, menu, formulaires et médias.

## Implémentation attendue
Concevoir mobile-first; garder hiérarchie de l’information; tester petits écrans, tailles de cibles et orientations.

## Tests à prévoir
1. Nominal : Tester 320px, 375px, tablette et clavier mobile.
2. Contrôle de refus : Une action primaire reste visible et utilisable sur écran étroit sans scroll horizontal.
3. Invariant : Aucun contenu essentiel caché sur mobile ou dépendant d’animation.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
