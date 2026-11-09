# Plan de validation — Onglets

## Modèle de données
Onglet, titre, panneau.

## Mise en œuvre attendue
Construire un bloc d'onglets avec rôles ARIA, navigation aux flèches et repli en sections empilées.

## Tests à prévoir
1. Nominal : Parcourir les onglets au clavier et au lecteur d'écran.
2. Contrôle de refus : Sans JavaScript, tous les panneaux sont visibles.
3. Invariant : Tout le contenu reste dans le HTML, donc lisible sans JavaScript.
4. GET/HEAD : cache public uniquement sans état de session ni donnée sensible ; canonical, statut HTTP, SEO et GEO inchangés ou améliorés.
5. POST : jamais de cache partagé ; CSRF, TLS, permissions, limitation des tentatives, idempotence. Ne pas exécuter si le noyau ne le prend pas en charge officiellement.
6. Activation et désactivation : les contenus sont conservés et les routes publiques retirées sans fuite.
7. Contrôles : validateur natif, tests PHP et HTTP, budgets ; consigner les commandes lancées, leurs résultats et ce qui n'a pas été testé.

## Preuve de disponibilité
État de la fonction ou de l'extension, journaux de CI, matrice des tests, procédure de retour arrière, et refus de toute promesse non vérifiée.
