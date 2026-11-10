# Plan de validation — Suivi de progression

## Modèle de données
Inscription, unité, état de complétion, tentative, durée, révision.

## Mise en œuvre attendue
Définir règles complétion; enregistrer progrès sous contrôle d’accès; versionner unités; agréger progression calculée depuis des états autorisés.

## Tests à prévoir
1. Nominal : Tester reprise session, deux appareils, leçon retirée.
2. Contrôle de refus : Deux appareils ne doivent pas rétrograder la progression déjà validée.
3. Invariant : Les progrès sont des données individuelles non cacheables; ne jamais accepter un identifiant membre arbitraire.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
