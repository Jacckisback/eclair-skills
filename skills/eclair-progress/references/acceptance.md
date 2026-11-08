# Plan de validation — Suivi de progression

## Modèle de données
Inscription, unité, état de complétion, tentative, durée, révision.

## Implémentation attendue
Définir règles complétion; enregistrer progrès sous contrôle d’accès; versionner unités; agréger progression calculée depuis des états autorisés.

## Tests à prévoir
1. Nominal : Tester reprise session, deux appareils, leçon retirée.
2. Contrôle de refus : Deux appareils ne doivent pas rétrograder la progression déjà validée.
3. Invariant : Les progrès sont des données individuelles non cacheables; ne jamais accepter un identifiant membre arbitraire.
4. GET/HEAD : cache public uniquement sans état de session ni données sensibles; canonical, statut HTTP, SEO/GEO.
5. POST : jamais de cache partagé; CSRF, TLS, permissions, limitation des tentatives, idempotence si mutation. Ne pas exécuter si non supporté officiellement.
6. Activation/désactivation : les contenus sont préservés et les routes publiques retirées sans fuite.
7. Contrôles : validator natif, tests PHP/HTTP, budgets; enregistrer commandes et résultats exécutés et ceux non testés.

## Preuve de disponibilité
État de l'extension / contrat, logs de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non validée.
