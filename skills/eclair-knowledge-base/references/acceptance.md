# Plan de validation — Base de connaissances

## Modèle de données
Article d'aide, rubrique, version, date de mise à jour.

## Mise en œuvre attendue
Organiser par problèmes des utilisateurs, une réponse par page, navigation par rubriques et recherche interne.

## Tests à prévoir
1. Nominal : Résoudre trois problèmes types uniquement avec la documentation.
2. Contrôle de refus : Un article obsolète est daté et signalé, pas laissé comme valide.
3. Invariant : Aucune procédure non testée n'est publiée.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
