# Plan de validation — Tableaux de données

## Modèle de données
Tableau, en-têtes, lignes, légende.

## Mise en œuvre attendue
Utiliser le bloc tableau natif, ajouter légende et en-têtes, prévoir le défilement horizontal maîtrisé.

## Tests à prévoir
1. Nominal : Lire le tableau sur mobile et au lecteur d'écran.
2. Contrôle de refus : Un tableau large ne provoque pas de défilement horizontal de toute la page.
3. Invariant : Aucune donnée personnelle dans un tableau public sans accord.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
