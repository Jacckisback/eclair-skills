# Plan de validation — Catégories

## Modèle de données
Catégorie, adresse, description, contenus rattachés.

## Mise en œuvre attendue
Définir peu de catégories stables, rédiger leur description, rattacher chaque contenu à une catégorie principale.

## Tests à prévoir
1. Nominal : Créer les catégories, rattacher les contenus et vérifier les pages de catégorie et leur pagination.
2. Contrôle de refus : Une catégorie sans contenu publié n'est pas proposée dans la navigation.
3. Invariant : Ne pas créer de catégories vides ou en double qui diluent le site.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
