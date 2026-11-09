# Plan de validation — Recherche sur le site

## Modèle de données
Index des contenus publiés, titre, extrait, adresse.

## Mise en œuvre attendue
Générer un index statique des contenus publics par tâche planifiée, le servir en GET cacheable et chercher côté navigateur avec une page de repli sans JavaScript.

## Tests à prévoir
1. Nominal : Chercher un terme présent, absent, accentué et vérifier le temps de réponse.
2. Contrôle de refus : Un brouillon ou une page privée n'apparaît jamais dans l'index.
3. Invariant : L'index ne contient que des contenus publics ; aucune requête de visiteur n'est journalisée avec son identité.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
