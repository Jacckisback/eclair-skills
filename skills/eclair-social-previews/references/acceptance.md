# Plan de validation — Aperçus de partage

## Modèle de données
Titre de partage, description, image de partage.

## Mise en œuvre attendue
Vérifier les balises de partage et l'image générée par le noyau, tester l'aperçu sur les principales plateformes.

## Tests à prévoir
1. Nominal : Tester l'aperçu d'un article et d'une page.
2. Contrôle de refus : Une page sans image dédiée garde un aperçu correct par défaut.
3. Invariant : L'image de partage ne contient aucune donnée personnelle ni texte trompeur.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
