# Plan de validation — Flux de traduction

## Modèle de données
Contenu source, version cible, traducteur, état, date de mise à jour.

## Mise en œuvre attendue
Tenir un tableau des contenus à traduire, produire les traductions en brouillon, faire relire par un locuteur, signaler les versions périmées.

## Tests à prévoir
1. Nominal : Traduire une page, la faire relire, publier, puis modifier la source et vérifier le signalement.
2. Contrôle de refus : Une traduction non relue reste en brouillon.
3. Invariant : Aucune traduction juridique ou médicale publiée sans validation qualifiée.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
